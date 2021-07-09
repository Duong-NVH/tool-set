# pip install googletrans == 3.1.0a0
from googletrans import Translator
translator = Translator()

assfile = open("trans.txt", "r", encoding='utf-8')
lines = assfile.readlines()

trans = []
for i, line in enumerate(lines):
    a = translator.translate(line[50:], src="vi", dest="en")
    trans.append(line[:50]+a.text+"\n")
    print(f"Translated {i+1}/{len(lines)} lines : {a.text}")

print("Writing to result.txt")
result = open('result.txt', 'w', encoding='utf-8')
result.writelines(trans)
result.close()
print("DONE!")
