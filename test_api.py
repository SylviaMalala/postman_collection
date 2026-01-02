#!/usr/bin/env python3
"""Quick test script for the API endpoints"""

import requests
import json

BASE_URL = "http://127.0.0.1:5555"

def test_get_heroes():
    print("Testing GET /heroes...")
    response = requests.get(f"{BASE_URL}/heroes")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json()[:2], indent=2)}")  # Show first 2
    print()

def test_get_hero_by_id():
    print("Testing GET /heroes/1...")
    response = requests.get(f"{BASE_URL}/heroes/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_get_powers():
    print("Testing GET /powers...")
    response = requests.get(f"{BASE_URL}/powers")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_get_power_by_id():
    print("Testing GET /powers/1...")
    response = requests.get(f"{BASE_URL}/powers/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_patch_power():
    print("Testing PATCH /powers/1...")
    data = {"description": "Updated description that is long enough to pass validation"}
    response = requests.patch(f"{BASE_URL}/powers/1", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_create_hero_power():
    print("Testing POST /hero_powers...")
    data = {"strength": "Average", "power_id": 1, "hero_id": 3}
    response = requests.post(f"{BASE_URL}/hero_powers", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

if __name__ == "__main__":
    try:
        print("="*50)
        print("API ENDPOINT TESTS")
        print("="*50)
        print()
        
        test_get_heroes()
        test_get_hero_by_id()
        test_get_powers()
        test_get_power_by_id()
        test_patch_power()
        test_create_hero_power()
        
        print("="*50)
        print("ALL TESTS COMPLETED")
        print("="*50)
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to the API. Make sure the Flask server is running on port 5555.")
    except Exception as e:
        print(f"ERROR: {e}")
