import pandas as pd

def position_adjustments(new_allocations: dict):
    current_positions_df = pd.read_csv('positions.csv') # Temporary position storage, to be replaced with either database or exchange call
    new_allocations_df = pd.DataFrame(list(new_allocations.items()), columns=['Ticker','New Position'])

    positions_allocations_df = pd.merge(current_positions_df, new_allocations_df, on='Ticker', how='outer')
    positions_allocations_df = positions_allocations_df.fillna(0)

    positions_allocations_df['Order Size'] = positions_allocations_df['New Position'] - positions_allocations_df['Position']
    positions_allocations_df['Order Type'] = positions_allocations_df['Order Size'].apply(lambda order: 'Buy' if order > 0 else ('Sell' if order < 0 else 'Hold'))
    positions_allocations_df['Order Size'] = positions_allocations_df['Order Size'].abs()

    orders_df = positions_allocations_df[positions_allocations_df['Order Size'] > 0]
    orders_df = orders_df[['Ticker', 'Order Type', 'Order Size']].reset_index(drop=True)

    return orders_df


def close_all_positions():
    current_positions_df = pd.read_csv('positions.csv') # Temporary position storage, to be replaced with either database or exchange call

    current_positions_df['Order Type'] = 'Sell'
    current_positions_df.rename(columns={'Position':'Order Size'}, inplace=True)

    return current_positions_df[['Ticker','Order Type','Order Size']]








