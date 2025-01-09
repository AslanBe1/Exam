# 7-masala

import asyncio
import time


async def download_data():
    print("Downloading data...")
    time.sleep(3)
    print("Downloaded")

async def sending_email():
    print("Sending email...")
    time.sleep(1)
    print("Email sent")

async def process_data():
    print("Processing data...")
    time.sleep(2)
    print("Processed")

async def main():
    await asyncio.gather(download_data())
    await asyncio.gather(sending_email())
    await asyncio.gather(process_data())

if __name__ == '__main__':
    asyncio.run(main())
