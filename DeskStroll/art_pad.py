from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import threading
from time import *
import os       
                                            
#====================================back end============================================
def minimize():
    win.attributes("-fullscreen", False)
    win.geometry("1280x1100")
    win.resizable(False,True)

def maximize():
    win.attributes("-fullscreen", True)

def exit_window():
    win.destroy()    

def get_cords(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def foreground_color():
    global f_color
    color = colorchooser.askcolor()
    f_color=color[1]
def background_color():
    global b_color
    color = colorchooser.askcolor()
    b_color=color[1]


def drag(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x   
    y = widget.winfo_y() - widget.startY + event.y   
    widget.place(x=x,y=y)
    win.update()
def clear_page():
    if messagebox.askyesno(title="Prompt" , message="Do You Want To Clear All Objects!"):
     for i in Plane_frame.winfo_children():
            i.destroy()
     messagebox.showinfo(title='Prompt',message='The Operation Was Successful!') 
    else:
       messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!') 

def clear_line_func():
     if messagebox.askyesno(title="Prompt" , message="Do You Want To Clear All Brush Arts!"):
      Plane_frame.delete(ALL)
      messagebox.showinfo(title='Prompt',message='The Operation Was Successful!') 
     else:
       messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!') 

def create_labels():
    h_value = height_Label.get()
    w_value = width_Label.get()
    tex = Name_Label.get()
    font = Font_Size_Label.get()
    size = Font_Size_Label.get()
    font = Font_style_Label.get(ACTIVE)
    print(font)
    label = Label(Plane_frame,bg=b_color,width=w_value,height=h_value,
                            fg=f_color,text=tex,font=(font,size))
    label.place(x=0,y=0)
    label.bind("<Button-1>",get_cords)
    label.bind("<B1-Motion>",drag)
def browse():
    global filepath
    filepath = filedialog.askdirectory()
    images_availible.delete(0,END)
    dirinfo = os.listdir(filepath)
    for i in dirinfo:
        file_ex = i.split(".")
        exten = (repr(file_ex[-1])).lower() 
        if  exten == "'jpg'":
         images_availible.insert(END,i)
        elif exten == "'png'":
         images_availible.insert(END,i) 
        else :
            pass
def line_color_change():
    global color_val
    color = colorchooser.askcolor()
    color_val=color[1]
def Line_width_change(value):
    global width_val
    width_val = value

def square_line():
    global type_var
    type_var = PROJECTING

def circle_line():
    global type_var
    type_var = ROUND

def bar_line():
    global type_var
    type_var = BUTT


def free_draw(event):
    global width_val
    x1,y1=(event.x-1), (event.y-1)
    x2,y2=(event.x+1), (event.y+1)
    Plane_frame.create_line(x1,y1,x2,y2,width=width_val,fill=color_val,capstyle=type_var,smooth=True)

    
  

def create_vertical():
    height2= Line_Height.get()
    label = Label(Plane_frame,height=height2,width=1,bg="black")
    label.place(x=50,y=50)
    label.bind("<Button-1>",get_cords)
    label.bind("<B1-Motion>",drag)
    
def create_horizontal():
    width2= Line_width.get()
    label = Label(Plane_frame,height=1,width=width2,bg="black")
    label.place(x=50,y=50)
    label.bind("<Button-1>",get_cords)
    label.bind("<B1-Motion>",drag)
def create_image():
    image_id = images_availible.get(ACTIVE)
    print(filepath)
    os.chdir(filepath)
    image_h = image_height.get()
    image_w = image_width.get()
    image = Image.open(image_id)
    new_image = image.resize((image_w,image_h))
    print(image_id)
    out_image = ImageTk.PhotoImage(new_image)
    label = Label(Plane_frame,image=out_image,bg=img_color)
    label.place(x=70,y=70)
    win.update()
    label.bind("<Button-1>",get_cords)
    label.bind("<B1-Motion>",drag)
    mainloop()

def image_color_fill():
    global img_color
    color = colorchooser.askcolor()
    img_color=color[1]
def time_get():
    time_string = strftime("%I:%M:%S %p     %A - %b - %Y")
    time_label.config(text=time_string)
    time_label.after(1000,time_get)     
#==============================binding funtions =========================================
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
#==============================binding funtions =========================================


width_val = 1
color_val ="black"   
type_var = ROUND  
#====================================back end============================================

#====================================front end===========================================
win = Tk()
win.attributes("-fullscreen", True)
  
#================================image files=============================================
base1 = PhotoImage(file='img\\background\\panner_background.png') 
base2 = PhotoImage(file='img\\buttons\\fill_color.png') 
base3 = PhotoImage(file='img\\buttons\\info_color.png') 
base4 = PhotoImage(file='img\\buttons\\create_shape.png') 
base5 = PhotoImage(file='img\\buttons\\clear_objects.png') 
base6 = PhotoImage(file='img\\buttons\\vertical_line.png') 
base7 = PhotoImage(file='img\\buttons\\horizontal_line.png') 
base8 = PhotoImage(file='img\\buttons\\browse_button.png')
base9 = PhotoImage(file='img\\buttons\\image_fill.png')
base10 = PhotoImage(file='img\\buttons\\create_image.png')
base11 = PhotoImage(file='img\\buttons\\line_color.png')
base12 = PhotoImage(file='img\\buttons\\clear_line.png')

base13 = PhotoImage(file='img\\buttons\\square_type.png')
base14 = PhotoImage(file='img\\buttons\\circle_type.png')
base21 = PhotoImage(file='img\\buttons\\bar_type.png')


base15 = PhotoImage(file='img\\buttons\\minimize_main.png')
base16 = PhotoImage(file='img\\buttons\\minimize_hover.png')
base17 = PhotoImage(file='img\\buttons\\maximize_main.png')
base18 = PhotoImage(file='img\\buttons\\maximize_hover.png')
base19 = PhotoImage(file='img\\buttons\\exit_main.png')
base20 = PhotoImage(file='img\\buttons\\exit_hover.png')

#================================image files=============================================

#==================================window frames=========================================
back_label = Label(win,image=base1)
back_label.place(x=-2,y=-1)

time_label = Label(win,font=("arial",9,"bold"),fg="white",bg="#242425")
time_label.place(x=25,y=2)
q = threading.Thread(target=time_get())
q.start()

Plane_frame= Canvas(win,width=895,height=797)
Plane_frame.pack(pady=42)
win.config(bg="blue")

Name_Label = Entry(win,bg="#343435",fg="#f0f0f0",font=("bell mt",10),border=0)
Name_Label.place(x=15,y=98)

Font_style_Label = Listbox(win,width=25,border=0,highlightthickness=0,bg="#343435",
highlightbackground="#343435",selectbackground="#cf59f2",selectborderwidth=0,
fg="#f0f0f0",font=("Times New Roman",10))
Font_style_Label.place(x=14,y=180)
#==================================window frames=========================================



#==================================font list=============================================
Font_style_Label.insert(0, "Algerian")
Font_style_Label.insert(2, "Arial")
Font_style_Label.insert(3, "Arial Black")
Font_style_Label.insert(4, "Bauhaus 93")
Font_style_Label.insert(5, "Bell mt")
Font_style_Label.insert(6, "Bernard MT Condensed")
Font_style_Label.insert(7, "Calibri")
Font_style_Label.insert(8, "Castellar")
Font_style_Label.insert(9, "Forte")
Font_style_Label.insert(10, "Georgia")
Font_style_Label.insert(11, "Goudy Stout")
Font_style_Label.insert(12, "Harlow Solid Italic")
Font_style_Label.insert(13, "Impact")
Font_style_Label.insert(14, "Kristen ITC")
Font_style_Label.insert(15, "Matura MT Script Capitals")
Font_style_Label.insert(16, "Old English Text MT")
Font_style_Label.insert(17, "Palace Script MT")
Font_style_Label.insert(18, "Ravie")
Font_style_Label.insert(19, "Segoe UI")
Font_style_Label.insert(20, "Times New Roman")
#==================================font list=============================================

#===============================left toolbar=============================================
Font_Size_Label = Scale(win,from_=1,to=500,highlightthickness=0,border=0,width=10,
length=100,fg="#f0f0f0",orient=HORIZONTAL,bg="#343435")
Font_Size_Label.place(x=36,y=400)

height_Label = Scale(win,from_=500,to=1,width=10,length=100,fg="#f0f0f0",
highlightthickness=0,border=0,orient=VERTICAL,bg="#343435")
height_Label.place(x=20,y=490)

width_Label = Scale(win,from_=1,to=500,width=10,length=100,fg="#f0f0f0",
highlightthickness=0,border=0,orient=HORIZONTAL,bg="#343435")
width_Label.place(x=55,y=590)

Font_background_Label = Button(win,image=base2,border=0,bg="#343435",
activebackground="#343435",command=background_color)
Font_background_Label.place(x=30,y=700)

font_color_Label = Button(win,image=base3,border=0,bg="#343435",
             activebackground="#343435",command=foreground_color)
font_color_Label.place(x=30,y=650)

create_button_1 = Button(win,image=base4,border=0,bg="#343435",
               activebackground="#343435",command=create_labels)
create_button_1.place(x=30,y=750)
#===============================left toolbar=============================================

#==================================buttom toolbar========================================
clear_button = Button(win,image=base5,border=0,command=clear_page)
clear_button.place(x=120,y=890)

Line_width = Scale(win,from_=1,to=200,width=10,length=300,fg="#f0f0f0",
highlightthickness=0,border=0,orient=HORIZONTAL,bg="#343435")
Line_width.place(x=650,y=945)

Line_Height = Scale(win,from_=1,to=100,width=10,length=300,fg="#f0f0f0",
highlightthickness=0,border=0,orient=HORIZONTAL,bg="#343435")
Line_Height.place(x=650,y=900)

create_vertical_line = Button(win,image=base6,border=0,bg="#343435",
               activebackground="#343435",command=create_vertical)
create_vertical_line.place(x=960,y=900)

create_horizontal_line = Button(win,image=base7,border=0,bg="#343435",
               activebackground="#343435",command=create_horizontal)
create_horizontal_line.place(x=960,y=945)

brush_width = Scale(win,from_=1,to=300,width=10,length=250,fg="#f0f0f0",
highlightthickness=0,border=0,orient=HORIZONTAL,bg="#343435",command=Line_width_change)
brush_width.place(x=360,y=900)

line_color = Button(win,image=base11,border=0,bg="#343435",
               activebackground="#343435",command=line_color_change)
line_color.place(x=260,y=906)

clear_line = Button(win,image=base12,border=0,bg="#343435",
               activebackground="#343435",command=clear_line_func)
clear_line.place(x=270,y=939)

square_type = Button(win,image=base13,border=0,bg="#343435",
               activebackground="#343435",command=square_line)
square_type.place(x=365,y=939)

circle_type = Button(win,image=base14,border=0,bg="#343435",
               activebackground="#343435",command=circle_line)
circle_type.place(x=450,y=939)

bar_type = Button(win,image=base21,border=0,bg="#343435",
               activebackground="#343435",command=bar_line)
bar_type.place(x=535,y=939)

#==================================buttom toolbar========================================

#==================================right toolbar=========================================
image_height = Scale(win,from_=1000,to=1,width=10,length=100,fg="#f0f0f0",
highlightthickness=0,border=0,orient=VERTICAL,bg="#343435")
image_height.place(x=1120,y=400)

image_width = Scale(win,from_=1,to=1000,width=10,length=100,fg="#f0f0f0",
highlightthickness=0,border=0,orient=HORIZONTAL,bg="#343435")
image_width.place(x=1150,y=500)

browse = Button(win,image=base8,border=0,bg="#343435",
               activebackground="#343435",command=browse)
browse.place(x=1140,y=220)

images_availible = Listbox(win,width=23,height=5,border=0,highlightthickness=0,
bg="#343435",highlightbackground="#343435",selectbackground="#cf59f2",
selectborderwidth=0,fg="#f0f0f0",font=("Times New Roman",9))
images_availible.place(x=1123,y=260)

image_fill = Button(win,image=base9,border=0,bg="#343435",
       activebackground="#343435",command=image_color_fill)
image_fill.place(x=1138,y=570)

create_img = Button(win,image=base10,border=0,bg="#343435",
               activebackground="#343435",command=create_image)
create_img.place(x=1138,y=615)
#==================================right toolbar=========================================

#==================================controll toolbar======================================
button5 = Button(win,activebackground="#242425",bg="#242425",
                                           border=0,image=base15,command=minimize)
button5.place(x=1100,y=2)
button6 = Button(win,activebackground="#242425",bg="#242425",border=0,
                                              image=base17,command=maximize)
button6.place(x=1150,y=2)
button7 = Button(win,activebackground="#242425",bg="#242425",border=0,
                                           image=base19,command=exit_window)
button7.place(x=1200,y=2)
#==================================controll toolbar======================================

#=======================================binders==========================================
button5.bind("<Enter>", on_button_in_5)
button5.bind("<Leave>", on_button_out_5)

button6.bind("<Enter>", on_button_in_6)
button6.bind("<Leave>", on_button_out_6)

button7.bind("<Enter>", on_button_in_7)
button7.bind("<Leave>", on_button_out_7)

Plane_frame.bind("<B1-Motion>",free_draw)


#=======================================binders========================================

#====================================front end===========================================
win.mainloop()