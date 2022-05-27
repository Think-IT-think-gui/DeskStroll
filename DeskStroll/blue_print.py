from tkinter import *
import turtle
import threading
from tkinter import colorchooser

#=================================back_end==============================================

#===================================drag_drop==================================
def get_cords(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    print(event.y)
def drag(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x   
    y = widget.winfo_y() - widget.startY + event.y   
    widget.place(x=x,y=y)
#===================================drag_drop==================================

#================================animation=====================================
def info_update():    
  speed_info = Label(statuse_tab,font=("arial",11),fg="#c60f0f",bg="#343435",
                                           text="Speed  {} Pxm".format(speed))
  speed_info.place(x=2,y=70)
  angle_info = Label(statuse_tab,font=("arial",13,"bold"),fg="#31c60f",
                            bg="#343435",text="Angle  {}°".format(angle))
  angle_info.place(x=13,y=165)
  if  speed == 10:
      speed_meter = Label(statuse_tab,bg="#343435",image=base1,border=0)
      speed_meter.place(x=20,y=3) 
  elif speed == 30:
      speed_meter = Label(statuse_tab,bg="#343435",image=base2,border=0)
      speed_meter.place(x=20,y=3)   
  elif speed  == 50:
      speed_meter = Label(statuse_tab,bg="#343435",image=base3,border=0)
      speed_meter.place(x=20,y=3)   
  elif speed == 80:
      speed_meter = Label(statuse_tab,bg="#343435",image=base4,border=0)
      speed_meter.place(x=20,y=3) 
  elif speed == 100:
      speed_meter = Label(statuse_tab,bg="#343435",image=base5,border=0)
      speed_meter.place(x=20,y=3)     
  
  if  angle == 5:
      angle_meter = Label(statuse_tab,bg="#343435",image=base1,border=0)
      angle_meter.place(x=20,y=100) 
  elif angle == 30:
      angle_meter = Label(statuse_tab,bg="#343435",image=base2,border=0)
      angle_meter.place(x=20,y=100)   
  elif angle  == 50:
      angle_meter = Label(statuse_tab,bg="#343435",image=base3,border=0)
      angle_meter.place(x=20,y=100)   
  elif angle == 70:
      angle_meter = Label(statuse_tab,bg="#343435",image=base4,border=0)
      angle_meter.place(x=20,y=100) 
  elif angle == 90:
      angle_meter = Label(statuse_tab,bg="#343435",image=base5,border=0)
      angle_meter.place(x=20,y=100)     

  speed_info.after(500,info_update)
#================================animation====================================


#================================tab==========================================
def statuse_menu():
    statuse_tab.config(width=460)
    pannel_back = Label(statuse_tab,image=base8,border=0,bg="#343435")
    pannel_back.place(x=150,y=5)

    Line_Height = Scale(pannel_back,from_=1,to=100,width=10,length=200,fg="#f0f0f0",
    highlightthickness=0,border=0,orient=HORIZONTAL,bg="#343435",command=pencil_width)
    Line_Height.place(x=80,y=30)
    pencil_color_button = Button(pannel_back,image=base9,activebackground="#343435",
                                           bg="#343435",border=0,command=pencil_color)
    pencil_color_button.place(x=12,y=70)
    
    sheet_color_button = Button(pannel_back,image=base10,activebackground="#343435",
                                            bg="#343435",border=0,command=sheet_color)
    sheet_color_button.place(x=155,y=70)

    pannel_back.bind("<Leave>",exit_menu)
def exit_menu(e):
    statuse_tab.config(width=120)    

def statuse_show(e):
    statuse_tab.place(x=0,y=0)

def statuse_hide(e):
    statuse_tab.place(x=-600,y=0)
#================================tab==========================================

#===============================draw==========================================
def make_circle(e):
    pencil.circle(50)

def create_circle(e):
    min_win = Toplevel()
    min_win.geometry("300x50")
    min_win.title("create circle")
    min_win.resizable(False,False)
    min_win.bind("<c>",make_circle)


    mainloop()
#    pencil.circle(40)
def sheet_color():
    global color_info1
    color_info2 = colorchooser.askcolor()[1]
    print(color_info2)
    main_canvas.config(bg=color_info2)
def pencil_width(e):
    pencil.pensize(e)
def pencil_color():
    global color_info1
    color_info1 = colorchooser.askcolor()[1]
    pencil.pencolor(color_info1)
def increase_speed(e):
    global speed
    speed +=5
    if speed > 100:
        speed = 100      
def decrease_speed(e): 
    global speed                
    speed -=5
    if speed < 5:
        speed = 5
def increase_angle(e):
    global angle
    angle +=5
    if angle > 90:
        angle = 90
def decrease_angle(e):
    global angle
    angle -=5
    if angle < 5:
        angle = 5
def find_pencil(e):
    pencil.penup()
    pencil.goto(x=56,y=55)
def forward(e):                                                                                                                                                                     
    pencil.forward(speed)  
def backward(e):
    pencil.back(speed)
def right(e):
    pencil.right(angle)
def left(e):
    pencil.left(angle)
def p_up(e):
    pencil.penup()
def p_down(e):
    pencil.pendown()     
#===============================draw===========================================

#===============================hover==========================================
def on_menu_button_in(e):
    menu_button["image"] = base7
def on_menu_button_out(e):
    menu_button["image"] = base6  
#===============================hover==========================================
   
speed = 10
angle = 5
color_info1 = "white"
#=================================back end==============================================



#==================================front end============================================

window = Tk()
window.attributes("-fullscreen", True)
main_canvas = Canvas(window,)
main_canvas.pack(fill=BOTH,expand=1)

#========================================image imports==========================
base1 = PhotoImage(file='img\\animation\\meter1.png') 
base2 = PhotoImage(file='img\\animation\\meter2.png') 
base3 = PhotoImage(file='img\\animation\\meter3.png') 
base4 = PhotoImage(file='img\\animation\\meter4.png') 
base5 = PhotoImage(file='img\\animation\\meter5.png') 
base6 = PhotoImage(file='img\\buttons\\menu_main.png') 
base7 = PhotoImage(file='img\\buttons\\menu_hover.png') 
base8 = PhotoImage(file='img\\background\\statuse_background.png') 
base9 = PhotoImage(file='img\\buttons\\pencil_color.png')
base10 = PhotoImage(file='img\\buttons\\sheet_color.png')
#========================================image imports=========================

pencil = turtle.RawTurtle(main_canvas)
pencil.pencolor(color_info1)
main_canvas.config(bg="#1a7ae5")
statuse_tab = Frame(main_canvas,height=250,width=120,bg="#343435",
                                            border=1,relief=SUNKEN)
statuse_tab.place(x=0,y=0)
statuse_tab.bind("<Button-1>",get_cords)
statuse_tab.bind("<B1-Motion>",drag)
menu_button = Button(statuse_tab,image=base6,border=0,bg="#343435",
                    activebackground="#343435",command=statuse_menu)
menu_button.place(x=5,y=200)
x = threading.Thread(target=info_update,daemon=True)
x.start()
menu_button.bind("<Enter>", on_menu_button_in)
menu_button.bind("<Leave>", on_menu_button_out)

#==================================bindings====================================
window.bind('<Up>',forward)
window.bind('<Left>',left)
window.bind('<Right>',right)
window.bind('<Down>',backward)
window.bind('<a>',p_up)
window.bind('<d>',p_down)
window.bind('<w>',increase_speed)
window.bind('<s>',decrease_speed)
window.bind('<q>',increase_angle)
window.bind('<e>',decrease_angle)
window.bind('<m>',statuse_show)
window.bind('<n>',statuse_hide)
window.bind('<p>',find_pencil)
window.bind('<c>',create_circle)

#==================================bindings=====================================

#===================================end view============================================

window.mainloop()