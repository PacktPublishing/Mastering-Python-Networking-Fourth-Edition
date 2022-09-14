#!/usr/bin/env python3
# Modified from 
# https://github.com/carlmontanari/scrapli/blob/main/examples/async_usage/async_multiple_connections.py
import asyncio
# from scrapli.driver.core import Paramiko
from scrapli.driver import GenericDriver


def gather_cor_device_version(ip, username, password):
    device = {
        "host": ip,
        "auth_username": username,
        "auth_password": password,
        "auth_strict_key": False,
        "ssh_config_file": True,
        "driver": GenericDriver
    }

    driver = device.pop("driver")
    conn = driver(**device)
    conn.open()
    response = conn.send_command("show version")
    conn.close()
    return response

def main():
    results = []
    for device in [
                    '192.168.2.50', 
                    '192.168.2.60',
                    '192.168.2.50', 
                    '192.168.2.60',
                    '192.168.2.50', 
                    '192.168.2.60',
                    '192.168.2.50', 
                    '192.168.2.60',
                  ]:
        results.append(gather_cor_device_version(device, 'cisco', 'cisco'))
    return results


if __name__ == "__main__": 
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds.")
