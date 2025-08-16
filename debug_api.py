import requests
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fipiranfunds.utils import jalali_to_gregorian

print("=== API DEBUG TEST ===")

# Test date conversion
jalali_date = "1403/01/01"
try:
    gregorian_date = jalali_to_gregorian(jalali_date)
    print(f"Date conversion: {jalali_date} -> {gregorian_date}")
except Exception as e:
    print(f"Date conversion failed: {e}")
    exit()

# Test API directly
regno = 11098
url = f"https://api.fipiran.com/api/v1/fund/{regno}/nav/{gregorian_date}"
print(f"Testing URL: {url}")

try:
    response = requests.get(url, timeout=10)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Response data: {data}")
        if data and len(data) > 0:
            print("✓ API is working and returned data")
        else:
            print("✗ API returned empty data")
    else:
        print(f"✗ API returned error: {response.text}")
        
except Exception as e:
    print(f"✗ API request failed: {e}")

print("\n=== DEBUG COMPLETE ===")
input("Press Enter to exit...")