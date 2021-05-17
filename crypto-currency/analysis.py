import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance
import cfgparser as config
import fetcher

def show_plot_graph(crypto):
    plt.style.use("dark_background")
    colors = mplfinance.make_marketcolors(up="#00ff00", down="#ff0000", wick="inherit", edge="inherit", volume="in")
    style = mplfinance.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)
    mplfinance.plot(fetcher.fetch(crypto), type="candle", style=style, volume=True)

def plot_graph(crypto):
    plt.style.use("dark_background")
    colors = mplfinance.make_marketcolors(up="#00ff00", down="#ff0000", wick="inherit", edge="inherit", volume="in")
    style = mplfinance.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)
    figure = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    axes = figure.subplots()
    mplfinance.plot(fetcher.fetch(crypto), type="candle", style=style, ax=axes)
    return figure

def show_plot_proportionalities_graph():
    plt.style.use("dark_background")
    plt.yscale("log")
    for crypto in config.CRYPTO:
        plt.plot(fetcher.fetch_combined()[crypto], label=crypto)
    plt.legend(loc="lower left")
    plt.show()

def plot_proportionalities_graph():
    plt.style.use("dark_background")
    data = fetcher.fetch_combined()
    figure = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    for crypto in config.CRYPTO:
        figure.add_subplot(111, yscale="log", label="crypto").plot(data[crypto], label=crypto)
    figure.legend(loc="lower left")
    return figure

def show_plot_proportionalities_map():
    plt.style.use("dark_background")
    combined = fetcher.fetch_combined().pct_change().corr(method="pearson")
    sns.heatmap(combined, annot=True, cmap="coolwarm")
    plt.show()

def plot_proportionalities_map():
    plt.style.use("dark_background")
    combined = fetcher.fetch_combined().pct_change().corr(method="pearson")
    figure = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    axes = figure.subplots()
    sns.heatmap(combined, annot=True, cmap="coolwarm", ax=axes)
    return figure

def show_plot_worths():
    plt.style.use("dark_background")
    sns.barplot(x="currency", y="value", data=fetcher.fetch_worths(), palette="Blues_d")
    plt.show()

def plot_worths():
    plt.style.use("dark_background")
    data = fetcher.fetch_worths()
    figure = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    axes = figure.subplots()
    bars = sns.barplot(x="currency", y="value", data=data, palette="Blues_d", ax=axes)
    print(data)
    for crypto_index in range(len(config.CRYPTO)):
        bars.text(crypto_index, data["value"][crypto_index], str(round(data["value"][crypto_index], 3)), color="white", ha="center")
    return figure
