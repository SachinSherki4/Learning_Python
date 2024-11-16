from datetime import datetime

current_date_time=datetime.now()
date=datetime.today().date()
current_time=datetime.now().time()
formatting_time=current_date_time.strftime("%Y-%m-%d : %H:%M:%S")
print(f"Current date and time : {current_date_time}")
print(f"Current date : {date}")
print(f"Current Time : {current_time}")
print(f"Formated Date and Time : {formatting_time}")
print(f"Date and Time in ISO Format : {current_date_time.isoformat()}")
print(f"Unix Format : {current_date_time.timestamp()}")
