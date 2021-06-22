file = open("HTML_Download.HTML")


line = file.read().replace("localhost", "localhost:7211")


print(line)

with open('HTML_def.html', 'w') as file:
    file.write(line)



