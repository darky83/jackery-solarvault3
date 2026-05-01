#!/usr/bin/env python3
"""Test script for Jackery API debugging."""

import logging
import sys

from api import JackeryAPI, JackeryAuthenticationError

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def print_flattened(data, prefix=""):
    """Print flattened key-value pairs from nested dictionaries."""
    for key, value in data.items():
        full_key = f"{prefix}-{key}" if prefix else key
        if isinstance(value, dict):
            print_flattened(value, full_key)
        else:
            print(f"  - {full_key}: {value}")


def test_jackery_api(username, password):
    """Test the Jackery API connection."""
    print(f"Testing Jackery API with username: {username}")

    try:
        # Create API instance
        api = JackeryAPI(account=username, password=password)

        # Test login
        print("Testing login...")
        if api.login():
            print("✅ Login successful!")
        else:
            print("❌ Login failed!")
            return False

        # Test device list
        print("Testing device list...")
        device_list = api.get_device_list()
        devices = device_list.get("data", [])
        print(f"✅ Found {len(devices)} devices")

        for device in devices:
            device_id = device.get("deviceId")
            device_name = device.get("deviceName", "Unknown")
            print(f"  - Device: {device_name} (ID: {device_id})")

        # Test device detail for first device
        if devices:
            first_device = devices[0]
            device_id = first_device["deviceId"]
            print(f"Testing device detail for {device_id}...")

            device_detail = api.get_device_detail(device_id)
            properties = device_detail.get("data", {}).get("properties", {})
            print(f"✅ Device detail retrieved with {len(properties)} properties")

            print("#############################################")

            print_flattened(properties)

            device_stat = api.get_device_stat(device_id)
            data = device_stat.get("data", {})
            print(f"✅ Device stats retrieved with {len(data)} properties")

            print_flattened(data)



        return True

    except JackeryAuthenticationError as e:
        print(f"❌ Authentication error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test_api.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    success = test_jackery_api(username, password)
    sys.exit(0 if success else 1)
