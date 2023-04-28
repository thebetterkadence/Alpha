from tkinter import *
import tkinter.messagebox
window = Tk()

textBox = Entry(window, width=50)
textBox.pack()
varWord = input()
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=0, y=0)
        clearButton = Button(self, text="Clear", command=self.clickClearButton)
        clearButton.place(x=0, y=20)
        helloButton= Button(self, text= "Search for Legislative Bills." command=self.clickHelloButton)
        helloButton.place(x=42, y=57)
def clickExitButton(self):
    exit()
def clickHelloButton(self):
    search_query = textBox.get()
    
def create_window():
    #Tk() = new independent window
    new_window= Tk() 

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










window.wm_title("ALPHA")
window.geometry("320x200")
window.mainloop()