import schedule
import time
import random
import logging
import os
from PIL import Image
import sys


# RESOURCE PATH (FOR PYINSTALLER)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# CONFIGURATION

IMAGE_FOLDER = resource_path("images")

POST_TIMES = ["13:50", "13:51", "13:52"]


# LOGGER SETUP

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


# CAPTION GENERATOR

captions = [
    "Check out the new cars available 🚗!",
    "New cars on the way 🚀",
    "Find your perfect car according to your budget.",
    "Follow us for more car updates!"
]

def generate_caption():
    return random.choice(captions)



# HASHTAG GENERATOR

hashtags = [
    "#MercedesBenz",
    "#Toyota",
    "#Jaguar",
    "#Mazda",
    "#Bugatti",
    "#Ferrari"
]

def generate_hashtags():
    selected = random.sample(hashtags, 3)
    return " ".join(selected)



# IMAGE SELECTOR

def get_random_image():

    if not os.path.exists(IMAGE_FOLDER):
        print("❌ Image folder not found")
        return None

    images = [img for img in os.listdir(IMAGE_FOLDER)
              if img.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not images:
        print("❌ No images available")
        return None

    selected_image = random.choice(images)
    image_path = os.path.join(IMAGE_FOLDER, selected_image)

    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print("Error opening image:", e)

    return image_path



# POST FUNCTION

def post():

    caption = generate_caption()
    tags = generate_hashtags()
    image = get_random_image()

    message = f"{caption}\n\n{tags}"

    print("\n📢 Posting Content...")
    print(message)
    print("🖼 Image:", image)

    logging.info(f"Posted: {message} | Image: {image}")



# SCHEDULER

def start_bot():

    for t in POST_TIMES:
        schedule.every().day.at(t).do(post)

    print("🤖 Bot started successfully")

    while True:
        schedule.run_pending()
        time.sleep(1)



# MAIN PROGRAM

def main():

    print("🚀 High Tech Cars Available Always")

    start_bot()


if __name__ == "__main__":
    main()