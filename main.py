import os
from tkinter import Tk
from tkinter import filedialog

liste = list()

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/", title = "Dosya Seç", filetypes = (("txt files","*.txt"),("all files","*.*")))
print("seçilen dosya: "+root.filename)

dosya = open(root.filename,"r",encoding="utf-8")

for satir in dosya:
    if satir.startswith("http"):
        liste.append(satir)

path = os.getcwd()
path += "\\"
path += "index.html"

html = open(path,"w",encoding="utf-8")

for index,item in enumerate(liste):
    html.write('<li><a href="'+item+'">'+str(index)+'</a></li>')

html.close()

print("index.html oluşturuldu...")