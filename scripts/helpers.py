DECIMALS = 1000000000

def print_row(text1, value, text2=""):
    print(f"{text1 : <25}{value : >15} {text2}")


def print_all_rows(block_num, num_of_txs, gas_mean, gas_max, gas_min, process_time):
    gas_mean = round(gas_mean/DECIMALS) if gas_mean > 0 else gas_mean
    gas_max = round(gas_max/DECIMALS) if gas_max > 0 else gas_max
    gas_min = round(gas_min/DECIMALS) if gas_min > 0 else gas_min
    avg_time = round(process_time/num_of_txs, 2) if num_of_txs > 0 else 0   

    print("")
    print_row("Block number:", block_num)
    print_row("Number of TXs:", num_of_txs)
    print_row("Gas price - mean:", gas_mean, "gwei")
    print_row("Gas price - max:", gas_max, "gwei")
    print_row("Gas price - min:", gas_min, "gwei")
    print_row("Total execution time:", process_time, "sec")
    print_row("Average execution time:", avg_time, "sec/tx")
    print("")


def print_dictionary(dict):
    for key, item in dict.items():
        print(f"{key}: {item}")