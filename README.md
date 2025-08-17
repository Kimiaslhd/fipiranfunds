FipiranFunds یک کتابخانه پایتون برای دریافت و ذخیره داده‌های معاملات و بازدهی صندوق‌های سرمایه‌گذاری از API فپیران و خروجی گرفتن به فرمت CSV است. این راهنما شامل توضیحات فارسی و مثال‌های کدنویسی انگلیسی است.

**پیش‌نیازها:**

*   پایتون: نسخه 3.6+ (توصیه می‌شود: 3.8+)
*   الزامات اصلی:
    *   `requests >= 2.25.0`
    *   `pandas >= 1.2.0`
    *   `jdatetime >= 3.6.0`
    *   `beautifulsoup4`
*   کتابخانه‌های اختیاری:
    *   `pyodbc` (برای اتصال به SQL Server - نیازمند درایور ODBC)
    *   `pytse-client` (برای استفاده از داده‌های TSETMC)
    *   `tqdm` (برای نمایش نوار پیشرفت)
    *   `python-dateutil` (برای پردازش تاریخ‌ها)

**نصب:**

*   نصب ساده (الزامات اصلی): `pip install fipiranfunds`
*   نصب کامل (شامل تمام کتابخانه‌های اختیاری): `pip install fipiranfunds requests pandas jdatetime beautifulsoup4 pyodbc pytse-client tqdm python-dateutil`
*   نصب از گیت‌هاب (برای توسعه): `pip install git+https://github.com/Kimiaslhd/fipiranfunds.git`

**شروع سریع:**

این کتابخانه امکان دریافت داده‌های صندوق‌های سرمایه‌گذاری ایرانی از API فپیران و خروجی به CSV را فراهم می‌کند. مثال زیر تاریخ شمسی را از کاربر دریافت و فایل CSV را روی دسکتاپ ذخیره می‌کند:

```python
from fipiranfunds import export_fund_data

export_fund_data()
# برنامه تاریخ شروع و پایان را به فرمت YYYY/MM/DD می‌پرسد.
# فایل CSV در دسکتاپ ذخیره می‌شود (مانند: fipiranfunds_export_20240321_123456.csv).
```

**عیب‌یابی:**

*   خطای تاریخ: فرمت ورودی باید YYYY/MM/DD باشد.
*   خطای API (مانند 500 یا IP-block): چند دقیقه صبر کنید و دوباره امتحان کنید.
*   تداخل نسخه‌ها: در صورت تداخل `jdatetime`، نسخه سازگار را مشخص کنید (مثلاً `pip install jdatetime==3.6.0`).
*   توصیه: برای تست، از محیط مجازی (virtualenv) استفاده کنید.
