FipiranFunds  
یک کتابخانه پایتون برای دریافت و ذخیره‌سازی داده‌های معاملات و بازدهی صندوق‌ها از API فپیران (Fipiran) و خروجی گرفتن به فرمت CSV. این README شامل توضیحات فارسی برای کاربران ایرانی و نمونه‌های کدنویسی کاربردی به انگلیسی است.

### پیش‌نیازها  
- پایتون 3.8+  
- کتابخانه‌های اصلی:  
  - `requests >= 2.25`  
  - `pandas >= 1.2`  
  - `jdatetime >= 3.6`  
  - `beautifulsoup4`  
- کتابخانه‌های اختیاری:  
  - `pyodbc` (برای اتصال به SQL Server)  
  - `pytse-client` (برای داده‌های TSETMC)  
  - `tqdm` (نوار پیشرفت)  
  - `python-dateutil` (پردازش تاریخ‌ها)  

### نصب  
برای استفاده ساده:  
```bash
pip install fipiranfunds
```  
برای نصب آخرین نسخه از گیت‌هاب:  
```bash
pip install git+https://github.com/Kimiaslhd/fipiranfunds.git
```  

### شروع سریع  
مثال تعاملی:  
```python
from fipiranfunds import export_fund_data
export_fund_data()
```  
برنامه تاریخ‌های شروع و پایان شمسی را دریافت کرده و خروجی CSV را روی Desktop ذخیره می‌کند.

### قابلیت‌های کلیدی  
- `export_fund_data()`: دریافت تعاملی داده‌ها و ذخیره به CSV.  
- `core.FundDataFetcher`: کلاس برای استفاده برنامه‌نویسی (خروجی `pandas.DataFrame`).  
- `utils.jalali_to_gregorian(date_str)`: تبدیل تاریخ شمسی به میلادی.  

### مثال‌ها  
1. استفاده از `FundDataFetcher`:  
```python
from fipiranfunds.core import FundDataFetcher
from fipiranfunds.utils import jalali_to_gregorian

fetcher = FundDataFetcher()
start = jalali_to_gregorian("1403/01/01")
end = jalali_to_gregorian("1403/01/31")
df = fetcher.fetch_fund_data(start, end)
df.to_csv("funds_local.csv", index=False)
```  

2. تبدیل تاریخ:  
```python
from fipiranfunds.utils import jalali_to_gregorian
print(jalali_to_gregorian("1403/01/01"))  # مثال: "2024-03-21"
```  

### ساختار CSV خروجی  
فایل خروجی با نام `fipiranfunds_export_<YYYYMMDD_HHMMSS>.csv` و شامل ستون‌هایی مانند `regNo`, `fundTitle`, `dailyEfficiency`, و غیره.

### اتصال به SQL Server (اختیاری)  
```python
import pyodbc
conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.1.131;DATABASE=LotusibBI;UID=user;PWD=pass"
conn = pyodbc.connect(conn_str)
# استفاده از pandas.to_sql برای ذخیره داده‌ها
```  

### نکات خطاها  
- فرمت تاریخ باید `YYYY/MM/DD` باشد.  
- در صورت خطای 500 یا محدودیت IP، چند دقیقه صبر کنید.  

### توسعه و مشارکت  
مسائل و درخواست‌ها را در [گیت‌هاب](https://github.com/Kimiaslhd/fipiranfunds) مطرح کنید.  

### مجوز  
MIT  

### نویسنده  
Kimia Salehi Delarestaghi  
- ایمیل: kimiaslhd@gmail.com  
- [LinkedIn](https://www.linkedin.com/in/kimia-salehy-delarestaghy/)  
- [GitHub](https://github.com/Kimiaslhd/fipiranfunds)  
- [PyPI](https://pypi.org/project/fipiranfunds/)
