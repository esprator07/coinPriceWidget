import requests
import json
from tkinter import *

payload = {} # To fetch data from the Binance website 
headers = {} # To fetch data from the Binance website

colour1='#EEEEEE' #The background color of our application
fon1=('Arial 12 bold') #The font of our application.

coinLabel=["0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0",
             "0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0"] #We will link the tkinter labels to this.

coins=[] #The coins entered by the user will be saved here.


coinName = ["BTCUSDT", "ETHUSDT", "SXPUSDT", "SPELLUSDT", "XRPUSDT", "ZILUSDT", "GMTUSDT", "COTIUSDT", "RLCUSDT",
            "RVNUSDT", "OPUSDT", "DYDXUSDT", "APEUSDT", "MTLUSDT", "USDTTRY"] #The coins entered by the user will be saved here.
#If the user does not enter any coin, the 15 coins here will be displayed automatically.
url = "https://api.binance.com/api/v3/ticker/price?&symbols=[" #The URL that allows us to fetch data from Binance.
#We will add coin names to this URL.
i = 0
coinoldprice=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #When there is a price change on the screen, it will be green and red.

while len(coinName) - i:
    url = url + "%22" + coinName[i] + "%22"
    i = i + 1
    if i != len(coinName):
        url = url + ","
    elif i == len(coinName):
        url = url + "]"
#At the start of the program, we create the URLs for the 15 coins we have selected.

def data():
    global coinName, result
    global coinLabel

    coinValue = requests.get(url, headers=headers, data=payload)
    result = json.loads(coinValue.content) #I saved the information coming from the URL to the result.
    coin_show()
    window.after(5000, data) #The data function will be executed every 5 seconds.

def coin_show () :
    global coinName,coinLabel ,result
    i=0

    while len(coinName)-i:
        ind=next((index for (index, d) in enumerate(result) if d["symbol"] == coinName[i]), None)
        #Since the coins do not come in the order we entered from the URL, we determine the index at which the coin is located.
        coinLabel[i]['text']=(float(result[ind]["price"])) #We are printing the coin's price on the screen.
        if (float(result[ind]["price"])) > coinoldprice[i]:
            coinLabel[i]['fg']='green'
        elif (float(result[ind]["price"])) < coinoldprice[i]:
            coinLabel[i]['fg'] = 'red'
        else:
            coinLabel[i]['fg']='#000000'
        coinoldprice[i]=(float(result[ind]["price"]))
        #We are changing the color of the coin's price.
        i=i+1
        window.update() #We are updating the application.

window=Tk () 
window.title('COIN PRICES') 
window.attributes('-topmost', 'true')
window.configure(bg=colour1) 

def remove_widgets():
    for widget in window.winfo_children():
        widget.destroy()	

def page2():
    global coinName,url,i,coins
    if coins.get():
        coinss = coins.get()
        coinName = coinss.split(",")

    url = "https://api.binance.com/api/v3/ticker/price?&symbols=["
    i = 0
    while len(coinName) - i:
        url = url + "%22" + coinName[i] + "%22"
        i = i + 1
        if i != len(coinName):
            url = url + ","
        elif i == len(coinName):
            url = url + "]"

    # We separated the coins entered by the user with commas and then created a new URL with these coins.
    remove_widgets()
    frame1 = Frame(window, bg=colour1)
    frame1.grid(row=0, column=0)
    frame2 = Frame(window, bg=colour1)
    frame2.grid(row=0, column=1)
    frame3 = Frame(window, bg=colour1)
    frame3.grid(row=0, column=2)
    # We used 3 frames for tkinter.
    c = 0


    counter = len(coinName)
    while counter:
        Label(frame1, text=coinName[c], font=fon1, bg=colour1, padx=8, pady=8).pack()
        Label(frame2, text=':', font=fon1, bg=colour1, padx=8, pady=8).pack()
        coinLabel[c] = Label(frame3, font=fon1, bg=colour1)
        coinLabel[c].pack(padx=8, pady=6.5)
        c = c + 1
        counter = counter - 1
    data()
    # We displayed the names of the coins on the screen.

def page1():

    global coins
    remove_widgets()
    frame1 = Frame(window, bg=colour1)
    frame1.grid(row=0, column=0)
    frame2 = Frame(window, bg=colour1)
    frame2.grid(row=2, column=0)
    frame3 = Frame(window, bg=colour1)
    frame3.grid(row=3, column=0)
    # We used 3 frames for tkinter.
    Label(frame1, text='Enter coins name (ex: BTCUSDT,ETHUSDT,XRPUSDT,USDTTRY) :', font=fon1, bg=colour1, padx=8, pady=8, justify='center').pack()
    coins = Entry(frame2, width=60, font=fon1, bg=colour1, justify='center')
    coins.pack(padx=60, pady=5)
    butonnn=Button(frame3,text="START PROGRAM",command=page2)
    butonnn.pack()

page1()
#We ran the opening screen function named page1.
window.mainloop()
# We entered the function to keep the window open continuously.
