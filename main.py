from strategies import strategies as str
import os
import shutil

def main(): 

    if os.path.exists('temp'):
            shutil.rmtree('temp')
    os.mkdir('temp')

    sp500_allocations, orders = str.sp500_top_10(10000)
    print(sp500_allocations)
    print(orders)

if __name__ == '__main__': main() 