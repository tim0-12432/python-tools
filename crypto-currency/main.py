import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplfinance
import seaborn as sns
import datetime
import PySimpleGUI as sg
import cfgparser as config
import analysis
import matplotlib
matplotlib.use("TkAgg")

#analysis.plot_proportionalities_graph()
#analysis.plot_proportionalities_map()
#analysis.plot_worths()
#analysis.plot_graph("ETH")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def main():
    sg.theme("dark grey 10")
    tab1_layout = [
        [sg.Text("Currency comparison")],
        [sg.Canvas(key="-CANVAS-COMBINED-")],
        [sg.Text("Crypto heatmap")],
        [sg.Canvas(key="-CANVAS-HEATMAP-")],
        [sg.Text("Values in comparison")],
        [sg.Canvas(key="-CANVAS-WORTHS-")]
    ]
    tab2_layout = [
        [sg.Text("BTC")],
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
    draw_figure(window["-CANVAS-GRAPH-"].TKCanvas, analysis.plot_graph("BTC"))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
    window.close()

if __name__ == '__main__':
    main()
