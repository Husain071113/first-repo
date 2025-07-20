files = open('diaries.txt', 'r')
content = files.read()
print("Using read():")
print(content)
files.close()

files = open('diaries.txt', 'r')
line1 = files.readline()
line2 = files.readline()
print(line1, end='')
print(line2, end='')
files.close()

files = open('diaries.txt', 'a')
line = ["\n hye there\n", "wasap"]
files.writelines(line)
files.close()

files = open('diaries.txt', 'r+')
files.seek(10)
files.read()