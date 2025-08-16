You’re absolutely right! Let’s create a detailed PyPI description for your package that shows its unique functionality. Your package is different - it’s synchronous (not async), focuses specifically on fund transaction data, and exports to CSV. Let’s create a comprehensive README:

Updated README.md for PyPI with detailed explanations:

        
        markdown
        
    
  
      # FipiranFunds

A Python library for fetching and exporting Iranian fund transaction data from Fipiran API to CSV files.

**Note**: This library focuses on fund transaction data and provides easy CSV export functionality for data analysis.

## Installation

Requires Python 3.6+.

```bash
$ pip install fipiranfunds
    
    
  
  
Usage

        
        python
        
    
  
      from fipiranfunds import export_fund_data

# Export fund transaction data to CSV
export_fund_data()
    
    
  
  
This library provides a simple interface to fetch fund transaction data and save it to CSV files on your desktop.

Quick Start

Use Python REPL or create a script to run the code samples below.

Example 1: Basic Usage

        
        python
        
    
  
      >>> from fipiranfunds import export_fund_data
>>> export_fund_data()
Enter start date (Jalali format YYYY/MM/DD): 1403/01/01
Enter end date (Jalali format YYYY/MM/DD): 1403/01/05
Fetching fund data from 2024-03-20 to 2024-03-24...
Found 313 funds to process
Processing funds: 100%|████████████| 313/313 [02:45<00:00, 1.89funds/s]
Data saved to: C:\Users\Desktop\fund_transactions_20240324_143022.csv
    
    
  
  
Example 2: Understanding the Output

The CSV file contains comprehensive fund transaction data with the following columns:


regNo - Fund registration number

fundTitle - Fund name

isCompleted - Transaction completion status

calcDate - Calculation date

licenseTitle - License type

fundSize - Size of the fund

fundType - Type of fund (equity, fixed income, etc.)

initiationDate - Fund initiation date

dailyEfficiency - Daily return percentage

weeklyEfficiency - Weekly return percentage

monthlyEfficiency - Monthly return percentage

quarterlyEfficiency - Quarterly return percentage

sixMonthEfficiency - Six-month return percentage

annualEfficiency - Annual return percentage

statisticalNav - Statistical Net Asset Value

efficiency - Overall efficiency

cancelNav - Cancellation NAV

issueNav - Issue NAV

dividendPeriodEfficiency - Dividend period efficiency

netAsset - Total net assets

unitBalance - Number of units

accountsNo - Number of accounts

articlesOfAssociationEfficiency - Articles of association efficiency


Example 3: Sample Output Data

        
        apache
        
    
  
      regNo,fundTitle,calcDate,dailyEfficiency,weeklyEfficiency,monthlyEfficiency,...
11726,جسورانه فیروزه,2024-03-20,0.25,1.20,5.43,...
11603,جسورانه فناوری بازنشستگی,2024-03-20,0.18,0.89,4.21,...
    
    
  
  
Features


Simple Interface: Just one function call to fetch and export data

Jalali Date Support: Enter dates in Jalali (Persian) calendar format

Automatic CSV Export: Saves data directly to your desktop

Progress Tracking: Shows real-time progress during data fetching

Error Handling: Automatic retry mechanism for failed requests

Comprehensive Data: Fetches 20+ data points for each fund


Advanced Usage

Programmatic Date Input

        
        python
        
    
  
      from fipiranfunds.core import FundDataFetcher
from fipiranfunds.utils import jalali_to_gregorian

# Create fetcher instance
fetcher = FundDataFetcher()

# Convert Jalali dates to Gregorian
start_date = jalali_to_gregorian("1403/01/01")
end_date = jalali_to_gregorian("1403/01/31")

# Fetch data
fund_data = fetcher.fetch_fund_data(start_date, end_date)
print(f"Fetched {len(fund_data)} records")
    
    
  
  
Custom Output Location

        
        python
        
    
  
      import os
from fipiranfunds import export_fund_data

# Change to a different directory before running
os.chdir("C:\\MyDataFolder")
export_fund_data()
    
    
  
  
Differences from Other Libraries


Synchronous: Unlike fipiran which is async, this library uses synchronous operations

CSV Export Focus: Specifically designed for data export and analysis

Transaction Data: Focuses on fund transaction and efficiency metrics

Desktop Integration: Automatically saves to desktop for easy access


Requirements


Python 3.6 or higher

Active internet connection

Windows/Mac/Linux operating system


Dependencies


requests - For API calls

pandas - For data manipulation

jdatetime - For Jalali date conversion


License

MIT License

Author

Kimia Salehi Delarestaghi

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

See Also


fipiran - Async library for Fipiran API

tsetmc - Tehran Stock Exchange data


Support

For issues and feature requests, please visit: https://github.com/Kimiaslhd/fipiranfunds/issues

        
        applescript
        
    
  
      
This README:
1. **Clearly shows what makes your library unique** (CSV export, synchronous, fund transaction focus)
2. **Provides detailed examples** with actual output
3. **Explains all the data columns** users will get
4. **Shows it's different** from the async `fipiran` library
5. **Gives credit** to related projects without claiming to copy them

Your library has its own unique value proposition - it's a specialized tool for fund transaction data export, which is different from the general-purpose async library you showed me!    
    
  
  

