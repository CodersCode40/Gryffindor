from PIL import Image

# Open the two images
image1 = Image.open("am.jpg")
image2 = Image.open("you.jpg")

# Make sure both images are the same size
image2 = image2.resize(image1.size)

frames = [image1, image2]

# Save as GIF
frames[0].save(
    "two_image_animation.gif",
    save_all = True,
    append_images = frames[1:],
    duration = 1000,  # 1 second per image
    loop = 0
)

