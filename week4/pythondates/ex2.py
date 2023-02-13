from datetime import datetime, timedelta

current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print("Yesterday date:", yesterday.strftime("%Y-%m-%d"))
print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow date:", tomorrow.strftime("%Y-%m-%d"))