
# building a reminder: 
import schedule
import time

def breakfast_reminder():
    print("🍔 Time for breakfast")


def lunch_reminder():
    print("🥗 Time for lunch")


def supper_reminder():
    print("🍛 Time for supper" )


schedule.every().day.at("20:16").do(breakfast_reminder)

schedule.every().day.at("20:17").do(lunch_reminder)

schedule.every().day.at("20:18").do(supper_reminder)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
run_scheduler()