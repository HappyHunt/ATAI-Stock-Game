import sys
import plotly.graph_objects as grObj
import pandas as pd
from datetime import datetime

DATA_FILEPATH = './client/charter/data/BTCUSDT-1m-2023-03-13.csv'

def main():
    try:
        df = pd.read_csv(DATA_FILEPATH)
        print(f'{DATA_FILEPATH} : File opened successfully.')
    except FileNotFoundError as e:
        print(f'{DATA_FILEPATH} : File not Found!')
        sys.exit(1)

    print('Processing...', end=' ')
    dfc = df['open_time'].copy()
    for i in range(df['open_time'].size):
        dfc[i] = datetime.fromtimestamp(float(df['open_time'][i])/1000)

    fig = grObj.Figure(data=[grObj.Candlestick(x=dfc,
                             open=df['open'],
                             high=df['high'],
                             low=df['low'],
                             close=df['close'])])
    print('Done.')

    fig.show()

    sys.exit(0)

if __name__ == '__main__':
    main()