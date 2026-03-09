import schedule
import time
import random
import logging
import os
from PIL import Image
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        bbase_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

IMAGE_FOLDER = resource_path("images")    


# ----------------------------
# CONFIGURATION
# ----------------------------

POST_TIMES = ["13:30", "13:16", "13:17"]

IMAGE_FOLDER = "images"



# ----------------------------
# LOGGER SETUP
# ----------------------------

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ----------------------------
# CAPTION GENERATOR
# ----------------------------

captions = [
    "Checkout the new cars available 🚗!",
    "New cars under way 🚀",
    "Find you perfect car according to your budget.",
    "Follow us for more cars updates!"
]

def generate_caption():
    return random.choice(captions)

# ----------------------------
# HASHTAG GENERATOR
# ----------------------------

hashtags = [
    "#MercedesBenz",
    "#Toyota",
    "#Jaguar",
    "#Marza",
    "bugatti",
    "#Fellari"
]

def generate_hashtags():
    selected = random.sample(hashtags, 3)
    return " ".join(selected)

# ----------------------------
# IMAGE SELECTOR
# ----------------------------

def get_random_image():

    if not os.path.exists(IMAGE_FOLDER):
        return "No image folder found"

    images = [img for img in os.listdir(IMAGE_FOLDER) 
              if img.endswith((".jpg",".jpeg",".png"))]


    if not images:
        return "No images available"

    selected_image = random.choice(images)
    image_path = os.path.join(IMAGE_FOLDER, selected_image)

    img = Image.open(image_path)
    img.show()

    return image_path

# ----------------------------
# POST FUNCTION
# ----------------------------

def post():

    caption = generate_caption()
    tags = generate_hashtags()
    image = get_random_image()

    message = f"{caption}\n\n{tags}"

    print("\nPosting Content...")
    print(message)
    print("Image:", image)

    logging.info(f"Posted: {message} | Image: {image}")

# ----------------------------
# SCHEDULER
# ----------------------------

def start_bot():

    for t in POST_TIMES:
        schedule.every().day.at(t).do(post)

    print("🤖 This my official platform")

    while True:
        schedule.run_pending()
        time.sleep(1)

# ----------------------------
# MAIN PROGRAM
# ----------------------------
def main():


    print("🚀 High Tech cars available always")

    start_bot()


if __name__ == "__main__":
    main()