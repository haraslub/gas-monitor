from web3.auto.infura import w3
from scripts.listener import process_block
import time

BEHIND_BLOCK_THRESHOLD = 10


def run():
    last_block = 0  # last block processed
    behind_block = 0    # difference between current block and the last one processed
    start_of_process = True  
    block_equality = False
    
    try:
        while True:
            # get the current block (=latest block)
            current_block = w3.eth.get_block_number()
            
            # init setting of the process
            if (start_of_process == True):
                print("")
                last_block = current_block - 1
                start_of_process = False

            # if the current block and the lastly one processed are equal, not print
            # the following statements again.
            if block_equality == False:
                behind_block = current_block - last_block
                print(f"Current block: {current_block}")
                print(f"Last processed block: {last_block}")
                print(f"Behind blocks: {behind_block}")
            
            # if there is too much (over the threshold) unprocessed blocks, skip them
            # in order to sync.
            if isinstance(BEHIND_BLOCK_THRESHOLD, int):
                if behind_block > BEHIND_BLOCK_THRESHOLD:
                    print(f"\nSkiping {behind_block} blocks to sync. Thus:")
                    last_block = current_block - 1
                    print(f"\nCurrent block: {current_block}")
                    print(f"Last processed block: {last_block}")

            # check if the current block and the lastly one processed are equal;
            if (last_block == current_block):
                block_equality = True
                time.sleep(1)
                continue
            
            # set block equality to False and get the blocks numbers to be processed
            block_equality = False
            start = last_block
            end = current_block
            diff = end - start

            # if the lastly processed block is behind more than two blocks 
            # from the current block, processed them each
            if (diff > 1):
                for i in range(start, end):
                    current_block = last_block + 1
                    print(f"Next block in the loop: {current_block}")
                    last_block = process_block(current_block)
            else:
                last_block = process_block(current_block)
      
    except KeyboardInterrupt:
        pass


def main():
    run()