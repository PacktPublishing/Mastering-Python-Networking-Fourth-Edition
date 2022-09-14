#!/usr/bin/env python3
# Modified from 
# https://github.com/carlmontanari/scrapli/blob/main/examples/async_usage/async_multiple_connections.py
import asyncio
from scrapli.driver.core import AsyncNXOSDriver


async def gather_cor_device_version(ip, username, password):
    device = {
        "host": ip,
        "auth_username": username,
        "auth_password": password,
        "auth_strict_key": False,
        "ssh_config_file": True,
        "transport": "asyncssh",
        "driver": AsyncNXOSDriver
    }

    driver = device.pop("driver")
    conn = driver(**device)
    await conn.open()
    response = await conn.send_command("show version")
    await conn.close()
    return response

async def main():
    results = await asyncio.gather(
                        gather_cor_device_version('192.168.2.50', 'cisco', 'cisco'),
                        gather_cor_device_version('192.168.2.60', 'cisco', 'cisco')
                    )
    for result in results: 
        print(result.result)


if __name__ == "__main__": 
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds.")
