from data import equities_data_fetch as edf

def main(): 

    data = edf.fetch_prices('AAPL', '2021-01-01', '2021-12-31')

    print(data.tail())


if __name__ == '__main__': main() 