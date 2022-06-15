import numpy as np
from datetime import date
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def show_plot():
    return


def parse(stock, start_date):
    return


def profit():
    return


def main():
    today = date.today()
    todayStr = today.strftime("%Y-%m-%d")
    print("todayStr =", todayStr)
    info = yf.download('TSLA', start="2021-01-01", end=todayStr)
    print(info.columns)
    df = pd.DataFrame({'Date': info.index, 'Values': info["Adj Close"]})
    print(df)

    x = df['Date'].tolist()
    y = df['Values'].tolist()

    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.ylabel('Price($)')
    plt.xlabel('Date', rotation=0)
    plt.show()


if __name__ == "__main__":
    main()
