import requests
from bs4 import BeautifulSoup
import os

reallinklist = [
    'https://doctruyen3q.net/truyen-tranh/co-vo-mang-thai-mot-tang-mot/chapter-109/214695']
# r = requests.get(
#     "https://doctruyen3q.net/truyen-tranh/co-vo-mang-thai-mot-tang-mot/337")

# soup1 = BeautifulSoup(r.text, 'html.parser')
# linklist = soup1.find_all('a')
# for link in linklist:
#     try:
#         if(link["href"][0:73] == "https://doctruyen3q.net/truyen-tranh/co-vo-mang-thai-mot-tang-mot/chapter"):
#             reallinklist.append(link["href"])
#     except:
#         pass
# reallinklist.reverse()
# print(reallinklist)


index = 1
chapter_id = 1
chapterlist = reallinklist

base_folder = "mangthai"
try:
    os.mkdir(os.path.join(os.getcwd(), base_folder))
except:
    pass
os.chdir(os.path.join(os.getcwd(), base_folder))


for chapter in chapterlist:
    r = requests.get(chapter)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    print(f"Start Chapter {chapter_id}")
    for image in images:
        name = str(index)
        try:
            link = image["src"]
            with open(name + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print(f'Writing: ',
                      f"{name}-c{chapter_id}-raw | {link}")
                index += 1
        except:
            pass
    print(f"End Chapter {chapter_id}")
    chapter_id += 1
