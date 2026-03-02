# def collection():
#     arr = []
#     num = 40
#     while num != 0:
#         amount = input("Put something in the collection bowl: ")
#         arr.append(amount)
#         print(amount)
#         num = - 1
#         print(arr)
# collection()

#files
# open('./text,txt')
# open('../lecture/text.txt')
# file = open('./text.txt')
# print("I Love you")
# file.close()
              

from yt_dlp import YoutubeDL


url = "https://youtu.be/nfstvFhWQXQ?si=lf2uneXJ2xg8mc0R"
yt_opts = {}

with YoutubeDL(yt_opts) as dd:
    dd.download(url)



