# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:31:14 2020
"""
#利用tkinter radiobutton、Label、button、entry、showmessage製作簡易點餐系統

import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title("點餐系統")
window.geometry("500x500")

#step1 定義變數
total=0 #折扣後金額
ototal=0#原始金額
hambugernum=0 #漢堡數量
friesnum=0 #薯條數量
chickennum=0 #雞塊數量
colanum=0 #可樂數量
meal='' #餐點清單
mealnum=0#餐點數量
#step2 定義函式
def cash(product,val):
    global total
    global ototal
    global hambugernum
    global friesnum
    global chickennum
    global colanum
    global mealnum
    total+=val
    ototal+=val
    if product == 'hambuger':
        hambugernum+=1
    if product == 'fries':
        friesnum+=1
    if product == 'chicken':
        chickennum+=1
    if product == 'cola':
        colanum+=1
    mealnum+=1    
    price.set(total)

def discount(val):
    global total
    total=ototal*val
    price.set(total)

#重新點餐函式
def reset():
   global total
   global ototal
   global hambugernum
   global friesnum
   global chickennum
   global colanum
   global meal
   global mealnum
   total=0
   ototal=0
   hambugernum=0
   friesnum=0
   chickennum=0
   colanum=0
   meal=''
   mealnum=0
   price.set(total)
   disc.set(1)

#確認點餐並顯示點餐清單
def accept():
    global total
    global ototal
    global hambugernum
    global friesnum
    global chickennum
    global colanum
    global meal
    global mealnum
    #total=total*float(disc.get())#折扣後金額
    if hambugernum > 0:
      meal= "漢堡"+" * "+str(hambugernum)+"\n"
    if friesnum>0:
      meal+= "薯條"+" * "+str(friesnum)+"\n"
      
    if chickennum>0:
      meal+= "雞塊"+" * "+str(chickennum)+"\n"
      
    if colanum>0:
      meal+= "可樂"+" * "+str(colanum)+"\n"
    
    if meal=='':
        tkinter.messagebox.showinfo(title='餐點',message="沒有任何餐點") 
    else:
        meal+=str(mealnum)+"份餐點"+"，"+"共"+str(total)+"元"
        tkinter.messagebox.showinfo(title='餐點',message=meal) 
    total=0
    ototal=0
    hambugernum=0
    friesnum=0
    chickennum=0
    colanum=0
    meal=''
    mealnum=0
    price.set(total)
    disc.set(1)#預設為沒有折扣
    
price=tk.StringVar()
tk.Label(window,text="金額：").place(x=0,y=0)
tk.Entry(window,width=200,textvariable=price,state="readonly").place(x=50,y=0)

tk.Label(window,text="選擇餐點：").place(x=0,y=30)

#lambda表示點擊按鈕時再傳參數給函式
tk.Button(window,text="漢堡\n$20",width=10,height=5,command=lambda:cash('hambuger',20)).place(x=0,y=50)
tk.Button(window,text="薯條\n$15",width=10,height=5,command=lambda:cash('fries',15)).place(x=80,y=50)
tk.Button(window,text="雞塊\n$25",width=10,height=5,command=lambda:cash('chicken',25)).place(x=160,y=50)
tk.Button(window,text="可樂\n$5",width=10,height=5,command=lambda:cash('cola',5)).place(x=240,y=50)

disc=tk.StringVar()
disc.set(1)#預設為沒有折扣
tk.Label(window,text="選擇折扣：").place(x=0,y=160)
tk.Radiobutton(window,text="沒有折扣",value="1",variable=disc,command=lambda:discount(1)).place(x=100,y=160)
tk.Radiobutton(window,text="85折",value="0.85",variable=disc,command=lambda:discount(0.85)).place(x=200,y=160)
tk.Radiobutton(window,text="75折",value="0.75",variable=disc,command=lambda:discount(0.75)).place(x=300,y=160)
tk.Radiobutton(window,text="5折",value="0.5",variable=disc,command=lambda:discount(0.5)).place(x=400,y=160)

tk.Button(window,text="結帳",width=10,height=1,command=accept).place(x=0,y=190)
tk.Button(window,text="重新點餐",width=10,height=1,command=reset).place(x=80,y=190)


window.mainloop()
