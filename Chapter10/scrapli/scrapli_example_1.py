#!/usr/bin/env python3
# Modified from https://github.com/carlmontanari/scrapli
from scrapli import Scrapli

device = {
   "host": "192.168.2.50",
   "auth_username": "cisco",
   "auth_password": "cisco",
   "auth_strict_key": False,
   "ssh_config_file": True,
   "platform": "cisco_nxos",
}

conn = Scrapli(**device)
conn.open()
response = conn.send_command("show version")
print(response.result)


