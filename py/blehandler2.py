#!/usr/bin/env python3

import sys
import asyncio
import requests
import warnings
import logger
from datetime import datetime
from bleak import BleakClient

ESP32_CHARACTERISTIC_UUID = "2049779d-88a9-403a-9c59-c7df79e1dd7c"

class BleHandler():
    """ble handler.
    """
    SLEEP_TIME = 1
    TIME_OUT = 20
    global logger

    def __init__(self, address:str) -> None:
        self.address:str = address
        self.logger = logger.Logger()

    async def __call__(self) -> None:
        """when call, connect to target address device.
        """
        print(f'connect to device({self.address}) start.')
        await self.connect_to_device()

    def _esp32_notification_handler(self, sender, data:bytearray):
        """Esp32 notification handler."""
        print(f'Esp32 notification handler: {data.decode()}')

    def _disconnect_callback(self, client: BleakClient):
        """disconnect callback. only logging message."""
        print(f'Client with address {client.address} got disconnected. try to reconnect.')

    async def connect_to_device(self):
        while True:
            print("Waiting connect to device.")
            async with BleakClient(self.address) as client:
                try:
                    await client.connect()
                    print("Connect to device successfuly.")
                    self.logger.write()

                except Exception as e:
                    print(f"Exception when connect: {e}")

                finally:
                    await client.disconnect()
