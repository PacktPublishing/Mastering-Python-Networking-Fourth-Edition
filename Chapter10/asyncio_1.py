#!/usr/bin/env python3
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    await asyncio.sleep(2)
    print('... and again.')


asyncio.run(main())

