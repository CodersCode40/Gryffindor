
# building a reminder: 
import schedule
import time

def lesson_starts():
    print("Lession One begins")

def second_lesson():
    print("Second lesson begins")

def third_lesson():
    print("Third lesson begins" )

def first_break():
    print("Break time")

def forth_lesson():
    print("Forth lesson begins")

def fifth_lesson():
    print("Fifth lesson begins")

def sixth_lesson():
    print("Sixth lesson begins")

def second_break():
    print("Break time")

def seventh_lesson():
    print("Seventh lesson begins")

def clossing():
    print("Closing time")
    


schedule.every().day.at("7:00").do(lesson_starts)

schedule.every().day.at("8:00").do(second_lesson)

schedule.every().day.at("9:00").do(third_lesson)

schedule.every().day.at("10:00").do(first_break)

schedule.every().day.at("10:30").do(forth_lesson)

schedule.every().day.at("11:30").do(fifth_lesson)

schedule.every().day.at("12:30").do(sixth_lesson)

schedule.every().day.at("13:30").do(second_break)

schedule.every().day.at("14:00").do(seventh_lesson)

schedule.every().day.at("15:00").do(clossing)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
run_scheduler()