from web3.auto.infura import w3
from timeit import default_timer as timer
from scripts.block_functions import (extract_block_transactions, get_gas_prices_in_block, evaluate_data)
from scripts.helpers import (print_all_rows)


def process_block(block_number="latest"):
    
    start = timer() # to start measuring the process
    
    # get transactions in the given block 
    transactions_data = extract_block_transactions(block_number)
    # get gas prices of the all transactions in the given block
    gas_prices = get_gas_prices_in_block(transactions_data)
    # get stats of the gas prices in the given block
    gas_mean, gas_max, gas_min = evaluate_data(gas_prices)
    
    end = timer() # to stop measuring the process

    # dump results to the console
    print_all_rows(
        block_num=transactions_data[0], # the block number
        num_of_txs=len(gas_prices), # the number of transactions in the block
        gas_mean=gas_mean, # mean of gas price in the txs in the block
        gas_max=gas_max, # max of gas price in the txs in the block
        gas_min=gas_min, # min of gas price in the txs in the block
        process_time=round(end - start), 
    )
    
    # return the block number 
    return transactions_data[0]


def main():
    print("\nChecking connection: {}".format(w3.isConnected()))
    if w3.isConnected():
        process_block()
    else:
        print("Cannot connect to the web3 endpoint.")


if __name__ == '__main__':
    main()