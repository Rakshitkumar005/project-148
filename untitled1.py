from tkinter import *
import random

root=Tk()
root.title("PICNIC BAG LIST")
root.geometry("500x400")
 
label_list=Label(root)
label_item=Label(root)

list_items=["Bottle","Tiffin","ID Card","Chocolates","Chips","Tickets","Hanky"]
label_list["text"]="Listed Items :"+str(list_items)

def bag_items():
    random_items=random.sample(range(1,7),1)
    label_item["text"]="Put Item No. "+str(random_items)+" In Bag"
    
btn=Button(root,text="Which Items To Put In Bag ?",command=bag_items,bg="orange",fg="white")
label_list.place(relx=0.5,rely=0.4,anchor=CENTER)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)  
label_item.place(relx=0.5,rely=0.6,anchor=CENTER) 

root.mainloop()