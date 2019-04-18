from tkinter import *
import requests
from flask import Flask
app = Flask(__name__)


#master = Tk()

#def callbackForUpdate():
#    print(requests.get('http://127.0.0.1:5000/updatecoordiantes/id/888').content)

#def callbackForProcess():
#    print(requests.get('http://127.0.0.1:5000/processunicorn').content)

#update = Button(master, text="Update", command=callbackForUpdate)
#update.pack()

#get = Button(master, text="Get", command=callbackForProcess)
#get.pack()

#mainloop()


from tkinter import *



master = Tk()




def show():
    T.insert(END, requests.get('http://127.0.0.1:5000/processunicorn').content)

def update():
   #print("Lattitude: %s\nLongitude: %s" % (e1.get(), e2.get()))
   requests.get('http://127.0.0.1:5000/updatecoordiantes/%s/%s' %(e1.get(), e2.get()))
   e1.delete(0,END)
   e2.delete(0,END)

Label(master, text="id").grid(row=0)
Label(master, text="Coordiantes").grid(row=1)

T = Text(master, height=2, width=30)


e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,"string")
e2.insert(10,"x,y")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
T.grid(row=2, column=1)

Button(master, text='Update', command=update).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )