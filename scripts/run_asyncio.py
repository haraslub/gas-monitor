"""
NOT RECOMMENDED for this approach process only the latest blocks
and thus not all of them.
"""

from web3.auto.infura import w3
from scripts.listener import process_block
import asyncio


async def log_loop(block_filter, poll_interval):
    while True:
        process_block(block_filter)
        await asyncio.sleep(poll_interval)
    

def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop("", 2)
            )
        )
    finally:
        loop.close()


if __name__ == "__main__":
    main()