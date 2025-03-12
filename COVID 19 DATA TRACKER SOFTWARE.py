# do all imports

# pip install requests module
import requests

# pip install bs4 library for uses of information scrap
from bs4 import BeautifulSoup

# pip install tkinter package which prvides the modern themed widget set and API
from tkinter import*

# pip install tkinter as Tk for use interface
import tkinter as Tk

# pip install plyer module its use of desktop notifier
from plyer import notification

# pip install time module  to display the notification in screen till perticular time
import time


# function for notifying...    
def notifyMe(title,message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "E:\corona tracker 1\corona tracker 1\icon.ico",
    timeout = 10
    )
    time.sleep(5)

if __name__=="__main__":
    notifyMe("nikk","COVID 19 Reports")
    

url="https://www.worldometers.info/coronavirus/"
page=requests.get(url)
Soup=BeautifulSoup(page.content,"html.parser")
info=Soup.find_all(class_="maincounter-number")
a=[items.get_text() for items in info]

country=" "

# for creating gui...
root=Tk.Tk()

# use for give the name of title
root.title("coronavirus analysis")

# use for change the background color of banner(image)
root.configure(background="white")

# use for increasing and decreasing size of geometry
root.geometry("900x900")

# use for change the font, size,style of text
font=("poppins",8,"bold")

# use for create banner image 
banner=Tk.PhotoImage(file="E:\\corona tracker 1\\corona tracker 1\\banner.png")
bannerLabel=Tk.Label(root,image=banner)
bannerLabel.pack()

# defining function for scrap data from website
def find_info():
    country=c.get()
    url1="https://www.worldometers.info/coronavirus/country/" + country
    page1=requests.get(url1)
    Soup1=BeautifulSoup(page1.content,"html.parser")
    info1=Soup1.find_all(class_="maincounter-number")
    b=[items.get_text() for items in info1]
    
# Create label use for find the data of all countries 
    label1=Label(root,font=font,bg="white",text="Total cases of coronavirus in "+ country)
    label1.pack()
    
    label1=Label(root,font=font,bg="white",text=b[0])
    label1.pack()

    label1=Label(root,font=font,bg="white",text="Tatol deaths of coronavirus in "+ country)
    label1.pack()
    
    label1=Label(root,font=font,bg="white",text=b[1])
    label1.pack()

    label1=Label(root,font=font,bg="white",text="Total recovered people from coronavirus in "+ country)
    label1.pack()

    label1=Label(root,font=font,bg="white",text=b[2])
    label1.pack()

# create label use for find the data of whole world
label1=Label(root,font=font,bg="white",text="Total cases of coronavirus in world")
label1.pack()

label1=Label(root,font=font,bg="white",text=a[0])
label1.pack()

label1=Label(root,font=font,bg="white",text="Total deaths of coronavirus in world")
label1.pack()

label1=Label(root,font=font,bg="white",text=a[1])
label1.pack()

label1=Label(root,font=font,bg="white",text="Total recovered people from coronavirus in world")
label1.pack()

label1=Label(root,font=font,bg="white",text=a[2])
label1.pack()

label1=Label(root,font=font,bg="white",text="please enter country name")
label1.pack()

c=Entry(root,font=font,bg="white",relief="solid")
c.pack()

# create button for find the data...
button1=Button(root,font=font,text= "find info" ,bg="green", relief="solid",command= find_info)
button1.pack()

# function use to reload the data from website
def refresh():
    newdata=find_info()
    label1["text"]=newdata

# create refresh button...
reBtn=Tk.Button(root,text="REFRESH",font=font,bg="white",relief="solid",command=refresh)
reBtn.pack()


root.mainloop()