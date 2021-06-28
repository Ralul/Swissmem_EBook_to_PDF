import os.path

fh = open("temp/" + "HTML_Download.HTML")

line = fh.read()

line = line.replace("localhost", "localhost:7211")


line = line.replace("Ã¶", "ö")
line = line.replace("􀀀", "ü")


save_path = 'Temp'
name_of_file = "HTML_defragmentation.html"

completeName = os.path.join(save_path, name_of_file)

file1 = open(completeName, "w")

file1.write(line)
file1.close()


