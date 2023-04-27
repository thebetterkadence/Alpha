from tkinter import *
import tkinter.messagebox


textBox = Entry(str(input("Search Bill")),Tk(), width=50,)
textBox.pack()
varWord = input()

def create_window():
    #Tk() = new independent window
    new_window= Tk() 
window = Tk()

Button(window,text="create new window",command=create_window).pack
window.mainloop()
#print("Hello, world!")
#def helloWorld():
#    print("Hello, world!")
#helloWorld()
#web scraping
def firstLink():
    varWord = input()
    print(input("Enter keywords to access liable search results pertaining to any Congressional Bills."))
    link = "https://www.congress.gov/search?q=%7B%22congress%22%3A%5B%22118%22%5D%2C%22source%22%3A%22all%22%2C%22search%22%3A%22" + varWord +"%20%22%7D"
    print(link)

