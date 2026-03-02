# sad = open("./mock.csv")

# for line in sad.readlines():
#     print(line)

# sad.close()    


#Example 2
# sad = open("./mock.csv")

# print(sad.readlines()[:10])
# for line in sad.readlines():
#     pass

# Another example

with open(file="mock.csv", mode="r", encoding="utf-8") as file:
    content = file.readlines()
    for cc in content:
        print(cc)



# content = sad.readline()
# for line in content:
#     print(line)

# print(content[:1])

# from PIL import Image, ImageChops
# img1 = Image.open('newton2.jpeg')
# img2 = Image.open('newton3.jpeg')

# diff = ImageChops.difference(img1,img2)
# diff.show()
