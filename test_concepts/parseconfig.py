configuration = open('/Users/thatcher/Desktop/config.txt', "r")

files = []
for line in configuration:
    research = line.strip()
    research = research.split(':')
    files.append(research)
print(files[0][1].strip())
