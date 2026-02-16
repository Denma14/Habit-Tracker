from datetime import datetime, timedelta

# Create a date object
# For a specific date:
day = datetime.today() - timedelta(days=0)

print(day.strftime("%A"))
