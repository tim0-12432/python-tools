import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import cfgparser as config
import analysis
import matplotlib
matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def refresh_current_currency(window, figure, value):
    if figure != None:
        figure.get_tk_widget().forget()
        plt.close('all')
    window.Element("-TEXT-CURR-").Update(value)
    return draw_figure(window["-CANVAS-GRAPH-"].TKCanvas, analysis.plot_graph(value))

def main():
    sg.theme("dark grey 10")
    tab1_layout = [
        [sg.Canvas(key="-CANVAS-COMBINED-")],
        [sg.Canvas(key="-CANVAS-HEATMAP-")],
        [sg.Canvas(key="-CANVAS-WORTHS-")]
    ]
    tab2_layout = [
        [sg.Combo(config.CRYPTO, default_value=config.CRYPTO[0], enable_events=True, key="-COMBO-CURR-")],
        [sg.Text(text=config.CRYPTO[0], key="-TEXT-CURR-")],
        [sg.Canvas(key="-CANVAS-GRAPH-")]
    ]

    layout = [[sg.TabGroup([[
        sg.Tab("Analysis", tab1_layout),
        sg.Tab("Currencies", tab2_layout)
    ]])]]
    window = sg.Window("Crypto Currency Analysis", layout, finalize=True)

    draw_figure(window["-CANVAS-COMBINED-"].TKCanvas, analysis.plot_proportionalities_graph())
    draw_figure(window["-CANVAS-HEATMAP-"].TKCanvas, analysis.plot_proportionalities_map())
    draw_figure(window["-CANVAS-WORTHS-"].TKCanvas, analysis.plot_worths())

    figure = None
    while True:
        event, values = window.read()
        if figure == None:
            figure = refresh_current_currency(window, figure, values["-COMBO-CURR-"])
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "-COMBO-CURR-":
            figure = refresh_current_currency(window, figure, values["-COMBO-CURR-"])
    window.close()

if __name__ == '__main__':
    main()
