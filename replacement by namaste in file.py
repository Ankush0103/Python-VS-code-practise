words = ['donkey', 'kaddu', 'mote']

with open("sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "Namaste")
    with open("sample.txt", "w") as f:
     f.write(content)