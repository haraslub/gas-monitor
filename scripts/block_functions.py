import pandas as pd
import numpy as np

from web3.auto.infura import w3
from scripts.helpers import export_data
from statistics import mean


def extract_block_transactions(block_number="latest"):
    """
    Extract hashes of transactions from the given block. If block_number is not
    given, the latest block is processed.
    """
    block = w3.eth.get_block(block_number)
    
    return (block.number, block.transactions)


def extract_gas_price(tx_hash=None):
    """
    Extract gas price from the given transaction. 
    Transaction hash is required.
    """
    if tx_hash:
        try:
            tx = w3.eth.get_transaction(tx_hash)
            return tx.gasPrice
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print("Error appeared during getting gas price of tx: {}".format(w3.toHex(tx_hash)))
            return np.nan
    else:
        raise ValueError("Missing hash of the transaction!")
    

def get_gas_prices_in_block(block_data):
    """
    Get gas prices of all transactions in the block.
    """
    gas_data = []
    _, transactions = block_data

    if transactions:
        for tx_hash in transactions:
            gas_price = extract_gas_price(tx_hash)
            gas_data.append(gas_price)
    
    return gas_data


def evaluate_data(ls=None):
    """
    Get max, min, and mean from the input list.
    """
    if isinstance(ls, list):
        if ls:
            gas_price_mean = np.nanmean(ls)
            gas_price_max = np.nanmax(ls)
            gas_price_min = np.nanmin(ls)
        else:
            gas_price_mean = gas_price_max = gas_price_min = 0
    else:
        gas_price_mean = gas_price_max = gas_price_min = np.nan

    return gas_price_mean, gas_price_max, gas_price_min