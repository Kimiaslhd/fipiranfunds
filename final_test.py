import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Test the library
from fipiranfunds import export_fund_data

print("=== FIPIRANFUNDS LIBRARY TEST ===")
print("Testing with minimal data...")

try:
    result = export_fund_data(
        start_jalali="1403/01/01",
        end_jalali="1403/01/01", # Just one day
        regnos=[11098] # Just one fund
    )
    
    if result:
        print(f"SUCCESS! CSV file created: {result}")
        print("Library is working correctly!")
        
        # Check if file exists
        if os.path.exists(result):
            print(f"File confirmed to exist on desktop")
        else:
            print("File not found on desktop")
    else:
        print("FAILED: No data exported")
        
except Exception as e:
    print(f"FAILED with error: {e}")
    import traceback
    traceback.print_exc()

print("\n=== TEST COMPLETE ===")
input("Press Enter to exit...")