#!/usr/bin/env python3
#
# derived from https://devnet-pubhub-site.s3.amazonaws.com/media/pyats/docs/getting_started/index.html
#
from pyats.topology import loader

# load testbed
testbed = loader.load('chapter16_pyats_testbed_1.yml')

# access the device
testbed.devices
lax_edg_r1 = testbed.devices['lax-edg-r1']

# establish connectivity
lax_edg_r1.connect()

# issue command
print(lax_edg_r1.execute('show version'))

# disconnect
lax_edg_r1.disconnect()


