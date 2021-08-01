from tkinter import *
import pyqrcode
from PIL import ImageTk,Image

root=Tk()

def generate():
    imagename=image_entry.get()#facebook
    updatedimagename=imagename+".png"#facebook.png
    url=link_entry.get()#https://www.facebook.com
    QRdata=pyqrcode.create(url)
    QRdata.png(updatedimagename,scale=4)
    image=ImageTk.PhotoImage(Image.open(updatedimagename))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,340,window=image_label)



canvas=Canvas(root,width=400,height=450)
canvas.pack()

image_label=Label(text="Enter the image name")
canvas.create_window(200,40,window=image_label)

image_entry=Entry(root)
canvas.create_window(200,60,window=image_entry)


link_label=Label(root,text="Enter yor website link")
canvas.create_window(200,120,window=link_label)

link_entry=Entry(root)
canvas.create_window(200,140,window=link_entry)

generate_button=Button(root,text="Generate QR",command=generate)
canvas.create_window(200,210,window=generate_button)


final_label=Label(text="Image")
canvas.create_window(200,240,window=final_label)

root.mainloop()
