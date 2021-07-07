import os.path

with open("Temp/HTML_Download.html") as f:
    lines = f.read()

print(lines)


lines = lines.replace("localhost", "localhost:7211")


lines= lines.replace("Ã¶", "ö")
lines = lines.replace("Ã¼", "ü")
lines = lines.replace("Ã¤", "ä")
lines = lines.replace("ÃŸ", "ß")
lines = lines.replace("Ã„", "Ä")



save_path = 'Temp/'
name_of_file = "HTML_defragmentation.html"

completeName = os.path.join(save_path, name_of_file)

file1 = open(completeName, "w")

file1.write(lines)
file1.close()



