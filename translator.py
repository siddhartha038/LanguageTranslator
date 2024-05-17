
from tkinter import* 
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="sa"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sr.get()
    d = comb_dest.get()
    
    msg = Sr_txt.get(1.0,END)
    textget = change(text=msg, src=s , dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)
    


root = Tk()
root.title("Translator")
root.geometry("500x1000")

root.config(bg='Red')

lab_txt = Label(root,text="Translator",font=("Time Now Roman",20,"bold"),bg="Red")
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Time Now Roman",20,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=100,height=20,width=300)

Sr_txt = Text(frame,font=("Time Now Roman",20,"bold"),wrap=WORD)
Sr_txt.place(x=10,y=130,height=100,width=480)

list_text = list(LANGUAGES.values())

comb_sr = ttk.Combobox(frame,value=list_text)
comb_sr.place(x=10,y=300,height=40,width=150)
comb_sr.set("english")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt = Label(root,text="Destination Text",font=("Time Now Roman",20,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time Now Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()
