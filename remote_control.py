#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xmlrpc.client import ServerProxy
import time
xmlrpc_control_client = ServerProxy('http://'+'localhost'+':8000')
freq_steps = [0, 50000000, -50000000, 100000000, -100000000]
while True:
    for freq in freq_steps:
        print("retuning to: ",freq," Hz")
        xmlrpc_control_client.set_rmt_delta_freq(freq)
        time.sleep(2)
