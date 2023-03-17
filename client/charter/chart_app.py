import sys
import plotly.graph_objects as gr_obj
import pandas as pd

from datetime import datetime
from chart.collect_data import Charter
from server.models.crypto import IntervalBinance


def main():
    c = Charter('BTC', IntervalBinance.W1)
    try:
        df = pd.DataFrame(c.get_data())
    except Exception as e:
        print("Wystąpił błąd: ", e)
        sys.exit(-1)
    # try:
    #     df = pd.read_csv(DATA_FILEPATH)
    #     print(f'{DATA_FILEPATH} : File opened successfully.')
    # except FileNotFoundError as e:
    #     print(f'{DATA_FILEPATH} : File not Found!')
    #     sys.exit(1)

    print('Processing...', end=' ')
    dfc = df['timestamp'].copy()
    for i in range(df['timestamp'].size):
        dfc[i] = datetime.fromtimestamp(float(df['timestamp'][i])/1000)

    fig = gr_obj.Figure(data=[gr_obj.Candlestick(x=dfc,
                                                 open=df['entry_price'],
                                                 high=df['highest_price'],
                                                 low=df['lowest_price'],
                                                 close=df['close_price'])])
    print('Done.')

    fig.show()
    # new_names = {
    #     'timestamp': 'date',
    #     'entry_price': 'open',
    #     'highest_price': 'high',
    #     'lowest_price': 'low',
    #     'close_price': 'close',
    #     'volume': 'volume',
    #     # Add more mappings as needed
    # }
    # df = df.rename(columns=new_names)
    #
    # for i in range(df['date'].size):
    #     df['date'][i] = datetime.fromtimestamp(float(df['date'][i])/1000)
    # df = df.set_index('date')
    # df.head()
    #
    # # Plot the chart with the specified style
    # mpf.plot(
    #     df,
    #     type='candle',
    #     title='BTC',
    #     ylabel='Price ($)')

    sys.exit(0)


if __name__ == '__main__':
    main()
