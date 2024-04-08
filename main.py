# Add seconds to datetime in Python 

from datetime import datetime, timedelta

# ✅ Add seconds to a datetime object
dt = datetime(2023, 9, 24, 9, 30, 35)
print(dt)  # 👉️ 2023-09-24 09:30:35

result = dt + timedelta(seconds=24)
print(result)  # 👉️ 2023-09-24 09:30:59

# ------------------------------

# ✅ Add seconds to the current time

now = datetime.today()
print(now)  # 👉️ 2023-07-20 17:40:43.310804

result = now + timedelta(seconds=15)
print(result)  # 👉️ 2023-07-20 17:40:58.310804
