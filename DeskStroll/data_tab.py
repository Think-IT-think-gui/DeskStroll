from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import tkinter.scrolledtext
from time import *
import time
import threading
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import sqlite3
import shutil
import random

#======================================Button Funtion====================================
def text_area_color():
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])
def open_text():
    filepath = filedialog.askopenfilename()
    file = open(filepath, "r")
    file = file.read()
    text_area.delete("1.0",END)
    text_area.insert("end", file)
    file.close()
def save_text():
    text = text_area.get("1.0",END)
    filepath = filedialog.asksaveasfile(defaultextension='.txt',
            filetypes=[("Text Files",".txt"),("All Files",".*")])
    filepath.write(str(text))
    filepath.close()
def new_work():
    text = text_area.get("1.0",END)
    filepath = filedialog.asksaveasfile(defaultextension='.txt',
            filetypes=[("Text Files",".txt"),("All Files",".*")])
    filepath.write(str(text))
    filepath.close()
    text_area.delete("1.0",END)
#======================================Button Funtion====================================
#=====================================add product=======================================
def add_product():
    new_product = list_entry.get()
    new_product = new_product.capitalize()
    product_list.insert(END,new_product)
    list_entry.delete(0,END)
#=====================================add product=======================================

#=====================================profile image======================================
def add_image():
    global image_id
    image_id = filedialog.askopenfilename()
    image = Image.open(image_id)
    new_image = image.resize((190,190))
    out_image = ImageTk.PhotoImage(new_image)
    label = Label(tab2,image=out_image)
    label.place(x=63,y=60)
    mainloop()  
#=====================================profile image======================================

#======================================currency==========================================
def get_currency():
    def cl1():
     currency_entry.delete(0,"end")
     currency_entry.insert(0, "GH₵")  
     Sub_win1.destroy()
    def cl2():
     currency_entry.delete(0,"end")
     currency_entry.insert(0, "$")  
     Sub_win1.destroy()
    def cl3():
     currency_entry.delete(0,"end")
     currency_entry.insert(0, "€")  
     Sub_win1.destroy()

    Sub_win1 = Toplevel()
    Sub_win1.geometry("150x150")
    Sub_win1.config(bg="#172433")
    cedi_curreny = Button(Sub_win1,bg="#172433",image=save12,border=0,
                                activebackground="#172433",command=cl1)
    cedi_curreny.pack()
    doller_curreny = Button(Sub_win1,bg="#172433",image=save14,border=0,
                                 activebackground="#172433",command=cl2)
    doller_curreny.pack()
    euro_curreny = Button(Sub_win1,bg="#172433",image=save13,border=0,
                                activebackground="#172433",command=cl3)
    euro_curreny.pack()
    Sub_win1.resizable(False,False)
    mainloop()
#=======================================currency=========================================

#======================================database==========================================
def add_to_database(): 
   id_list = ["uri","ttp","xzi","3ew","dsew","dsa","wqw","uek","ptp","ewew"]
   mixed = random.choice(id_list)

   assign = first_name_entry.get()+mixed+str(age_scale.get())
   shutil.copy(image_id,"Data_files//Images//"+assign+".png")
   if gentder_scale.get() == 1:
       gender = "Male"
   elif gentder_scale.get() == 2:
       gender = "Female"
   cost_val = cost_entry.get()
   paid_val = paid_entry.get()
   ballance_val = int(cost_val) - int(paid_val) 
   conn = sqlite3.connect('main_database.db')
   c = conn.cursor() 
   c.execute("INSERT INTO customer_info VALUES (:first_name, :last_name, :gender, :age, :contact, :city, :address, :date, :cost, :paid, :ballance, :info_key)",
             {
                 'first_name': first_name_entry.get().capitalize(),
                 'last_name' : last_name_entry.get().capitalize(),
                 'gender': gender,
                 'age': str(age_scale.get()),
                 'contact' : Contact_entry.get(),
                 'address': Address_entry.get().capitalize(),
                 'city' : City_entry.get().capitalize(),
                 'date' : current_date,
                 'cost' : currency_entry.get()+cost_entry.get(),
                 'paid' : currency_entry.get()+paid_entry.get(),
                 'ballance' : currency_entry.get()+str(ballance_val),
                 'info_key' : assign
             })      
   conn.commit()
   conn.close() 
   items = []
   list_text = open("Data_files//Product_files//{}.txt".format(assign), "w")
   for i in product_list.curselection(): 
     items.insert(i,product_list.get(i)) 
   for i in items:
    list_text.write(i+'\n')
   list_text.close()   
   first_name_entry.delete(0,END)
   last_name_entry.delete(0,END)
   Contact_entry.delete(0,END)                  
   Address_entry.delete(0,END)
   City_entry.delete(0,END)
   cost_entry.delete(0,END)
   paid_entry.delete(0,END)
   tree.update()
   tree.update_idletasks()
def clear_form():
   first_name_entry.delete(0,END)
   last_name_entry.delete(0,END)
   Contact_entry.delete(0,END)                  
   Address_entry.delete(0,END)
   City_entry.delete(0,END)
   cost_entry.delete(0,END)
   paid_entry.delete(0,END)
#======================================database==========================================

#===================================Key info=============================================

def get_saved_data():
    key_val = key_entry.get()
    info = open("Data_files//Product_files//{}.txt".format(key_val), "r")
    info = info.read()
    product_out.delete("1.0",END)
    product_out.insert(END, info)
    image = Image.open("Data_files//Images//"+key_val+".png")
    new_image = image.resize((230,267))
    out_image = ImageTk.PhotoImage(new_image)
    profile_picture = Label(tab3,image=out_image,border=0)
    profile_picture.place(x=35,y=25)
    mainloop()






#===================================Key info=============================================


#=====================================Command functions==================================
def minimize():
    window.attributes("-fullscreen", False)
    window.geometry("1280x1100")
    window.resizable(False,True)
def maximize():
    window.attributes("-fullscreen", True)
def exit_window():
    window.destroy()    
def time_get():
    time_string = strftime("%I:%M:%S %p     %A - %b - %Y")
    time_label.config(text=time_string)
    time_label.after(1000,time_get)     
#=====================================Command functions==================================

#===================================Animation functions==================================
def slid_up(e):
    x = threading.Thread(target=up_motion, daemon=True)
    x.start()
def up_motion():
 time_factor = 0
 cord_map=150
 while time_factor <100:
  time_factor +=5
  cord_map -=5
  time.sleep(0.01)
  frame = main_canvas.create_window((5,cord_map), window=main_frame, anchor="nw")
  window.update()
 print(cord_map)
def slid_down(e):
    ys = threading.Thread(target=down_motion ,daemon=True)
    ys.start()
def down_motion():
 time_factor = 0
 cord_map=50
 while time_factor <100:
  time_factor +=5
  cord_map +=5
  time.sleep(0.01)
  frame = main_canvas.create_window((5,cord_map), window=main_frame, anchor="nw")   
#===================================Animation functions==================================

#=====================================Bindings===========================================
def on_button_in_5(e):
    button5["image"] = base16
def on_button_out_5(e):
    button5["image"] = base15  
def on_button_in_6(e):
    button6["image"] = base18
def on_button_out_6(e):
    button6["image"] = base17   
def on_button_in_7(e):
    button7["image"] = base20
def on_button_out_7(e):
    button7["image"] = base19  
def add_client_in(e):
    add_client["image"] = save23
def add_client_out(e):
    add_client["image"] = save22 
def clear_info_in(e):
    clear_info["image"] = save25
def clear_info_out(e):
    clear_info["image"] = save24 
#=====================================Bindings===========================================

#====================================Front End===========================================
window = Tk() 
window.attributes("-fullscreen", True)
#==================================Tmages================================================
save1 = PhotoImage(file='img\\background\\data_background.png')
save2 = PhotoImage(file='img\\background\\not_back.png')
save3 = PhotoImage(file='img\\Labels_blocks\\popup_text_editor.png')
save4 = PhotoImage(file='img\\buttons\\pop_up.png')
save5 = PhotoImage(file='img\\buttons\\new_file.png')
save6 = PhotoImage(file='img\\buttons\\open_file.png')
save7 = PhotoImage(file='img\\buttons\\save_file.png')
save8 = PhotoImage(file='img\\buttons\\text_color.png')
save9 = PhotoImage(file='img\\background\\store_back.png')
save10 = PhotoImage(file='img\\buttons\\import_img.png')
save11 = PhotoImage(file='img\\buttons\\add_to_list.png')
save12 = PhotoImage(file='img\\buttons\\cedi_b.png')
save13= PhotoImage(file='img\\buttons\\euro_b.png')
save14 = PhotoImage(file='img\\buttons\\doller_b.png')
base15 = PhotoImage(file='img\\buttons\\minimize_main.png')
base16 = PhotoImage(file='img\\buttons\\minimize_hover.png')
base17 = PhotoImage(file='img\\buttons\\maximize_main.png')
base18 = PhotoImage(file='img\\buttons\\maximize_hover.png')
base19 = PhotoImage(file='img\\buttons\\exit_main.png')
base20 = PhotoImage(file='img\\buttons\\exit_hover.png')
save21 = PhotoImage(file='img\\buttons\\currency.png')
save22 = PhotoImage(file='img\\buttons\\add_client_main.png')
save23 = PhotoImage(file='img\\buttons\\add_client_hover.png')
save24 = PhotoImage(file='img\\buttons\\clear_info_main.png')
save25 = PhotoImage(file='img\\buttons\\clear_info_hover.png')
save26 = PhotoImage(file='img\\background\\retrive_back.png')
save27 = PhotoImage(file='img\\buttons\\find_key.png')

#==================================Tmages================================================

new_background = Label(image=save1)
new_background.pack()

time_label = Label(window,font=("arial",9,"bold"),fg="white",bg="#242425")
time_label.place(x=25,y=1)
q = threading.Thread(target=time_get())
q.start()
h = Label(window)
h.place(x=53,y=95)
Note_holder = Label(h,width=90,height=50,border=0,)
Note_holder.pack()
notebook = ttk.Notebook(Note_holder,)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
#==================================Tab 1=================================================
notebook.add(tab1,text="Desk Note")
back_label = Label(tab1,image=save2,bg="#f0f0f0")
back_label.pack()
text_area = tkinter.scrolledtext.ScrolledText(tab1,width=136,height=35,fg="white",
                bg="#242425",border=0,tabstyle="wordprocessor",font=("bell mt",12))
text_area.place(x=30,y=20)
#==================================Tab 1=================================================

#======================================Menu Build========================================
main_canvas = Canvas(tab1,width= 770,height=140,bg="#242425",border=0)
main_canvas.place(x=200,y=666)
pop_up = Label(main_canvas,image=save4,border=0,bg="#242425")
pop_up.place(x=360,y=30)
main_frame=Frame(main_canvas,width=735,height="100",border=0,bg="#242425")
frame = main_canvas.create_window((5,50), window=main_frame, anchor="nw")
menu_label = Label(main_frame,bg="#242425",border=0,image=save3)
menu_label.place(x=0,y=0)
slid_down(E)
#======================================Menu Build========================================

#====================================Cover Strips========================================
cover_horizontal = Label(tab1,width=130,height=2,border=2,bg="#242425")
cover_horizontal.place(x=100,y=650)
cover_vertical_1 = Label(tab1,width=5,height=11,border=2,bg="#242425")
cover_vertical_1.place(x=950,y=637)
cover_vertical_1 = Label(tab1,width=1,height=11,border=2,bg="#242425")
cover_vertical_1.place(x=190,y=637)
#====================================Cover Strips========================================

#========================================Menu Buttons====================================
New_file = Button(menu_label,image=save5,border=0,command=new_work)
New_file.place(x=110,y=8)
open_file = Button(menu_label,image=save6,border=0,command=open_text)
open_file.place(x=250,y=8)
save_file = Button(menu_label,image=save7,border=0,command=save_text)
save_file.place(x=410,y=12)
text_color = Button(menu_label,image=save8,border=0,command=text_area_color)
text_color.place(x=550,y=12)
#======================================Menu Buttons======================================

#======================================Command Button====================================
button5 = Button(window,activebackground="#242425",state=DISABLED,bg="#242425",border=0,
                                                         image=base15,command=minimize)
button5.place(x=1100,y=0)
button6 = Button(window,activebackground="#242425",bg="#242425",border=0,image=base17,
                                                                      command=maximize)
button6.place(x=1150,y=0)
button7 = Button(window,activebackground="#242425",bg="#242425",border=0,image=base19,
                                                                   command=exit_window)
button7.place(x=1200,y=0)
#======================================Command Buttons===================================

#==================================Tab 2=================================================

#====================================database=====================================
current_date = strftime("%d/%b/%Y")
try:
 conn = sqlite3.connect('main_database.db')
 c = conn.cursor()
 c.execute("""CREATE TABLE customer_info (
    first_name text,
    last_name text,
    gender text,
    age text,
    contact text,
    city text,
    address text,
    date text,
    cost text,
    paid text,
    ballance text,
    info_key text
 )""")
 conn.commit()
 conn.close()
except sqlite3.OperationalError:
    pass 
#====================================database=====================================
notebook.add(tab2,text="Store Client Data")
back_label1 = Label(tab2,image=save9,bg="#f0f0f0")
back_label1.pack()
import_image_button = Button(tab2,image=save10,bg="#f0f0f0",border=0,command=add_image)
import_image_button.place(x=100,y=260)
first_name_entry = Entry(tab2,width=19,font=("arial",23),border=0,bg="#f0f0f0")
first_name_entry.place(x=340,y=233)
last_name_entry = Entry(tab2,width=19,font=("arial",23),border=0,bg="#f0f0f0")
last_name_entry.place(x=760,y=233)
gentder_scale = Scale(tab2,highlightthickness=0,troughcolor="#212ea8",border=0,
       length=180, orient=HORIZONTAL,font=("arial",1),from_=1,to=2,bg="#242425")
gentder_scale.place(x=175,y=360)
age_scale = Scale(tab2,highlightthickness=0,troughcolor="#212ea8",border=0,length=430,
         orient=HORIZONTAL,font=("arial",10),fg="#f0f0f0",from_=10,to=100,bg="#242425")
age_scale.place(x=610,y=350)
Contact_entry = Entry(tab2,width=20,font=("arial",18),border=0,bg="#f0f0f0")
Contact_entry.place(x=84,y=516)
City_entry = Entry(tab2,width=20,font=("arial",18),border=0,bg="#f0f0f0")
City_entry.place(x=454,y=516)
Address_entry = Entry(tab2,width=20,font=("arial",18),border=0,bg="#f0f0f0")
Address_entry.place(x=825,y=516)
list_entry = Entry(tab2,width=21,font=("arial",18),border=0,bg="#242425")
list_entry.place(x=85,y=723)
product_list = Listbox(tab2,height=5,fg="#f0f0f0",width=45,font=("arial",12),
                selectmode=MULTIPLE,border=0,bg="#242425",highlightthickness=0)
product_list.place(x=70,y=610)
Add_button = Button(tab2,image=save11,bg="#242425",activebackground="#242425",
                                                  border=0,command=add_product)
Add_button.place(x=364,y=720)
currency_entry = Entry(tab2,width=8,font=("arial",25),border=0,bg="#f0f0f0")
currency_entry.place(x=755,y=581)
currency_button = Button(tab2,image=save21,bg="#f0f0f0",activebackground="#f0f0f0",
                                                     border=0,command=get_currency)
currency_button.place(x=716,y=581)
cost_entry = Entry(tab2,width=10,font=("arial",25),fg="#f0f0f0",border=0,bg="#242425")
cost_entry.place(x=720,y=643)
paid_entry = Entry(tab2,width=10,fg="#f0f0f0",font=("arial",25),border=0,bg="#242425")
paid_entry.place(x=720,y=709)
add_client = Button(tab2,image=save22,bg="#242425",activebackground="#242425",
                                              border=0,command=add_to_database)
add_client.place(x=975,y=570)
clear_info = Button(tab2,image=save24,bg="#242425",activebackground="#242425",
                                                     border=0,command=clear_form)
clear_info.place(x=975,y=670)
notebook.pack(expand=True,fill="both")


#==================================Tab 2=================================================

#==================================Tab 3=================================================
notebook.add(tab3,text="Retrive Client Data")
back_label2 = Label(tab3,image=save26,bg="#f0f0f0")
back_label2.pack()

tree = ttk.Treeview(tab3)
tree['columns'] = ("Name",
                   "Gender", 
                   "age", 
                   "contact",
                   "location", 
                   "cost",
                   "paid", 
                   "ballance",
                   "date",
                   "info_key"
                  )

tree.column("#0",width=0,stretch=NO)
tree.column("Name",width=150,anchor=CENTER)
tree.column("Gender",width=100,anchor=CENTER)
tree.column("age",width=80,anchor=CENTER)
tree.column("contact",width=120,anchor=CENTER)
tree.column("location",width=150,anchor=CENTER)
tree.column("cost",width=80,anchor=CENTER)
tree.column("paid",width=90,anchor=CENTER)
tree.column("ballance",width=70,anchor=CENTER)
tree.column("date",width=130,anchor=CENTER)
tree.column("info_key",width=150,anchor=CENTER)

tree.heading("#0", text="")
tree.heading("Name", text="Client Name")
tree.heading("Gender", text="Gender")
tree.heading("age", text="Age")
tree.heading("contact", text="Contact")
tree.heading("location", text="Location")
tree.heading("cost", text="Total Cost")
tree.heading("paid", text="Amount Paid")
tree.heading("ballance", text="Ballance")
tree.heading("date", text="Date")
tree.heading("info_key", text="Client Key")

tree.place(x=20,y=345, height=420)
#fscrollbary = Scrollbar(tree, orient=VERTICAL)

conn = sqlite3.connect('main_database.db')
c = conn.cursor() 
c.execute("SELECT * , oid FROM customer_info")
rec = c.fetchall()
val_count=0
for i in rec:
 tree.insert(
     parent='',
     index=END ,
     iid=val_count,
     text="",
     values=(i[0]+" "+i[1],
     i[2],i[3],i[4],
     i[5]+"-"+i[6],i[8],
     i[9],i[10],i[7],i[11]
             ))

 val_count +=1
 print(i)

conn.commit()

conn.close() 

product_out = tkinter.scrolledtext.ScrolledText(tab3,width=25,fg="#f0f0f0",border=0,height=12,bg="#242425",font=("arial",13))
product_out.place(x=310,y=40)

key_entry = Entry(tab3,width=22,fg="black",bg="#f0f0f0",border=0,font=("impact",19))
key_entry.place(x=666,y=263)

submit = Button(tab3,image=save27,border=0,bg="#242425",activebackground="#242425",command=get_saved_data)
submit.place(x=980,y=258)
#==================================Tab 3=================================================

notebook.pack(expand=True,fill="both")
#================================Bindings================================================
pop_up.bind("<Enter>",slid_up)
menu_label.bind("<Leave>",slid_down)
button5.bind("<Enter>", on_button_in_5)
button5.bind("<Leave>", on_button_out_5)
button6.bind("<Enter>", on_button_in_6)
button6.bind("<Leave>", on_button_out_6)
button7.bind("<Enter>", on_button_in_7)
button7.bind("<Leave>", on_button_out_7)
add_client.bind("<Enter>", add_client_in)
add_client.bind("<Leave>", add_client_out)
clear_info.bind("<Enter>", clear_info_in)
clear_info.bind("<Leave>", clear_info_out)
#===============================Bindings=================================================
mainloop()
#====================================Front End===========================================   