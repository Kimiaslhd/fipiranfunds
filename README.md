FipiranFunds

کتابخانه پایتون برای دریافت و ذخیره داده‌های معاملات و بازدهی صندوق‌ها از API فپیران و خروجی گرفتن به فرمت CSV. این راهنما شامل توضیحات فارسی و مثال‌های کدنویسی انگلیسی است.

## پیش‌نیازها

*   پایتون: نسخه 3.6+ (توصیه می‌شود: 3.8+).
*   الزامات اصلی (نصب خودکار):
    *   `requests >= 2.25.0`
    *   `pandas >= 1.2.0`
    *   `jdatetime >= 3.6.0`
    *   `beautifulsoup4` (برای تجزیه HTML).
*   کتابخانه‌های اختیاری:
    *   `pyodbc` (اتصال به SQL Server، نیازمند نصب درایور ODBC).
    *   `pytse-client` (استفاده از داده‌های TSETMC).
    *   `tqdm` (نمایش نوار پیشرفت).
    *   `python-dateutil` (پردازش تاریخ‌ها).

**نصب:**

نصب ساده (الزامات اصلی):

```
pip install fipiranfunds
```

نصب کامل (شامل تمام کتابخانه‌های اختیاری):

```
pip install fipiranfunds requests pandas jdatetime beautifulsoup4 pyodbc pytse-client tqdm python-dateutil
```

نصب از گیت‌هاب (برای توسعه):

```
pip install git+https://github.com/Kimiaslhd/fipiranfunds.git
```

## شروع سریع

این کتابخانه امکان دریافت داده‌های صندوق‌های سرمایه‌گذاری ایرانی از API فپیران و خروجی به CSV را فراهم می‌کند. مثال زیر تاریخ شمسی را از کاربر دریافت و فایل CSV را روی دسکتاپ ذخیره می‌کند.

```python
from fipiranfunds import export_fund_data

export_fund_data()
# برنامه تاریخ شروع و پایان را به فرمت YYYY/MM/DD می‌پرسد.
# فایل CSV در دسکتاپ ذخیره می‌شود (مانند: fipiranfunds_export_20240321_123456.csv).
```

## قابلیت‌ها
  
نکات خطاها و راهنمایی‌ها / Troubleshooting & Tips


خطای تاریخ: ورودی را بررسی کنید؛ فرمت باید YYYY/MM/DD باشد.

خطای API (مانند 500 یا IP-block): چند دقیقه صبر کنید و دوباره امتحان کنید — سایت ممکن است درخواست‌ها را موقتاً محدود کند.

تداخل نسخه‌ها: اگر jdatetime با دیگر پکیج‌ها تداخل دارد، نسخه سازگار را پین کنید (مثلاً pip install jdatetime==3.6.0).

نکته عمومی: برای تست، از محیط مجازی (virtualenv) استفاده کنید تا وابستگی‌ها ایزوله شوند.


CLI (در صورت وجود) / CLI (If Available)

اگر پکیج CLI را پشتیبانی کند:

        
        nginx
        
    
  
      python -m fipiranfunds.cli
# یا اگر entry point تعریف شده باشد:
fipiranfunds
    
    
  
  
توسعه و مشارکت / Contributing

خوشحال می‌شویم از کمک شما!


مسائل (issues) یا درخواست‌های pull را در گیت‌هاب باز کنید.

قبل از ارسال PR: تست‌های محلی را اجرا کنید، کد را با black فرمت کنید، و سبک PEP 8 را رعایت کنید.

برای شروع: repo را fork کنید، تغییرات را اعمال کنید، و PR ارسال کنید.


تغییرات / Changelog


0.1.14: بهبود README، رفع مشکلات رندرینگ PyPI، و صادرات API در سطح بالا.

0.1.13: نسخه اولیه با پشتیبانی پایه API و CSV.


برای تغییرات کامل، به گیت‌هاب commits مراجعه کنید.

مجوز / License

MIT License. جزئیات در فایل LICENSE.

نویسنده و تماس / Author & Contact


نام: Kimia Salehi Delarestaghy

ایمیل: kimiaslhd@gmail.com

لینکدین: https://www.linkedin.com/in/kimia-salehy-delarestaghy/

گیت‌هاب: https://github.com/Kimiaslhd/fipiranfunds

PyPI: https://pypi.org/project/fipiranfunds/


اگر سؤالی دارید، issue باز کنید یا ایمیل بزنید!

[![PyPI version](https://img.shields.io/pypi/v/fipiranfunds.svg)](https://pypi.org/project/fipiranfunds/)
[![Python Version](https://img.shields.io/pypi/pyversions/fipiranfunds.svg)](https://pypi.org/project/fipiranfunds/)
[![License](https://img.shields.io/pypi/l/fipiranfunds.svg)](https://pypi.org/project/fipiranfunds/)
[![GitHub Issues](https://img.shields.io/github/issues/Kimiaslhd/fipiranfunds.svg)](https://github.com/Kimiaslhd/fipiranfunds/issues)
[![GitHub Stars](https://img.shields.io/github/stars/Kimiaslhd/fipiranfunds.svg)](https://github.com/Kimiaslhd/fipiranfunds/stargazers)

    
    
  
  




