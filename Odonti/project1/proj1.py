import schedule
import time

def promote_product():
    print("Posting to facebook: New cars alert! check out https://jiji.com.gh/cars")
    print("Posting to Telegram: out latest cars is finally here! https://jiji.com.gh/cars")

# schedule the promotional social media post for everyday at 10:00
schedule.every().day.at("19:41").do(promote_product)

# schedule the promotional social media post for everyday at 16:00
schedule.every().day.at("19:42").do(promote_product)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
run_scheduler()