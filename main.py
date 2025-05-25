import time
from plyer import notification

while True:
    print("please Drink some water")
    notification.notify(
        title="Water Reminder",
        message="It's time to drink some water!",
        app_name="Water Reminder App",
        timeout=1
    )
    time.sleep(10)