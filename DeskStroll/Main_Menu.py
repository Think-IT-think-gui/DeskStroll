from tkinter import *
import os
import pywintypes
import win32api
import win32con
import threading
from time import *
import time
from tkinter import messagebox
#screen resolution <<<
def revert():
   if messagebox.askyesno(title="Prompt" , message="Do You Want To Exit DeskStoll!"):
     info_wid = open("info_wid","r")
     info_wid = info_wid.read()
     info_hig = open("info_hig","r")
     info_hig = info_hig.read()
     devmode = pywintypes.DEVMODEType()
     devmode.PelsWidth = int(info_wid)
     devmode.PelsHeight = int(info_hig)
     devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
     win32api.ChangeDisplaySettings(devmode,0)  
     main_win.destroy()  
   else:
     messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!') 
#screen resoloution >>>
def media():
  os.startfile("Media_Tab.exe")
def file_ex():
    os.startfile("File_explorer.exe")
def web_tab():
    os.startfile("web_tab.exe")
def data():
    os.startfile("Data_tab.exe") 
def art():
    os.startfile("Art_tab.exe")
def shutdown():
    if messagebox.askyesno(title="Prompt" , message="Do You Want To Shutdown This Computer!"):
     os.system('cmd /c" shutdown /s /t 5"')
     messagebox.showinfo(title='Prompt',message='The Operation Was Successful!') 
    else:
       messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!') 
   
def restart():
    if messagebox.askyesno(title="Prompt" , message="Do You Want To Restart This Computer!"):
     os.system('cmd /c" shutdown /r /t 5"')  
     messagebox.showinfo(title='Prompt',message='The Operation Was Successful!') 
    else:
       messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!') 
      
def time_get():
    time_string_main= strftime("%I:%M")
    time_string_sec = strftime("%S")
    time_string_note = strftime("%p")
    time_string_date = strftime("%A - %b - %Y")
    time_label_main.config(text=time_string_main)
    time_label_sec.config(text=time_string_sec)
    time_label_note.config(text=time_string_note)
    time_label_date.config(text=time_string_date)
    time_label_date.after(1000,time_get)            
#hover methods <<<
def on_enter_media(e):
    media_button["image"] = save3
def on_leave_media(e):
    media_button["image"] = save2   
#==========================================================================
def on_enter_web(e):
    web_button["image"] = save4
def on_leave_web(e):
    web_button["image"] = save5           
def on_enter_data(e):
    data_button["image"] = save6
def on_leave_data(e):
    data_button["image"] = save7     
#==========================================================================
def on_enter_work(e):
    work_button["image"] = save9
def on_leave_work(e):
    work_button["image"] = save8   
#==========================================================================
def on_enter_art(e):
    art_button["image"] = save17
def on_leave_art(e):
    art_button["image"] = save16 
def on_enter_button1(e):
    button1["image"] = save11
def on_leave_button1(e):
    button1["image"] = save10   
def on_enter_button2(e):
    button2["image"] = save13
def on_leave_button2(e):
    button2["image"] = save12   
def on_enter_button3(e):
    button3["image"] = save15
def on_leave_button3(e):
    button3["image"] = save14   

#hover method <<<
main_win = Tk()
main_win.title("DeskSroll")
screen_info = Open("info_hig","r")
screen_info = screen_info.read()
if int(screen_info) == 1024:
   main_win.geometry("1280x1024")
else:   
  main_win.attributes("-fullscreen", True)

#==========================================================================
#images imports <<<
save1 = PhotoImage(file='img//background//background.png')
save2 = PhotoImage(file='img//buttons//media_main.png')
save3 = PhotoImage(file='img//buttons//media_hover.png')
save4 = PhotoImage(file='img//buttons//web_hover.png')
save5 = PhotoImage(file='img//buttons//web_main.png')
save6 = PhotoImage(file='img//buttons//data_hover.png')
save7 = PhotoImage(file='img//buttons//data_main.png')
save8 = PhotoImage(file='img//buttons//work_main.png')
save9 = PhotoImage(file='img//buttons//work_hover.png')
save10 = PhotoImage(file='img//buttons//power_off_main.png')
save11 = PhotoImage(file='img//buttons//power_off_hover.png')
save12 = PhotoImage(file='img//buttons//restart_main.png')
save13 = PhotoImage(file='img//buttons//restart_hover.png')
save14 = PhotoImage(file='img//buttons//exit_main.png')
save15 = PhotoImage(file='img//buttons//exit_hover.png')
save16 = PhotoImage(file='img//buttons//art_main.png')
save17 = PhotoImage(file='img//buttons//art_hover.png')

#images import >>>
#==========================================================================
#wallpaper <<<
wallpaper_label = Label(main_win,image=save1)
wallpaper_label.pack(fill=BOTH)
#wallpaper >>>
#time <<<<
#==========================================================================
time_label_main = Label(main_win,bg="#3bf4be",fg="#242425",
                                        font=("impact",130))
time_label_main.place(x=370,y=80)
#==========================================================================
time_label_sec = Label(main_win,bg="#3bf4be",fg="#242425",
                                      font=("Algerian",60))
time_label_sec.place(x=790,y=175)
#==========================================================================
time_label_note = Label(main_win,bg="#3bf4be",fg="#242425",
                                      font=("Bauhaus 93",40))
time_label_note.place(x=790,y=120)
#==========================================================================
time_label_date = Label(main_win,bg="#3bf4be",fg="#242425",
                               font=("Brush Script MT",30))
time_label_date.place(x=460,y=265)
#==========================================================================
y = threading.Thread(target=time_get, daemon=True)
y.start()
#==========================================================================
#time >>>>
#buttons <<<
#==========================================================================
media_button = Button(main_win,text="click me",image=save2
,border=0,bg="#3ef1a8",activebackground="#3ef1a8",command=media)
media_button.place(x=95,y=400)
#==========================================================================
web_button = Button(main_win,text="click me",image=save5
,border=0,bg="#3ef1a8",activebackground="#3ef1a8",command=web_tab)
web_button.place(x=320,y=400)
#==========================================================================
data_button = Button(main_win,text="click me",image=save7
,border=0,bg="#3ef1a8",activebackground="#3ef1a8",command=data)
data_button.place(x=545,y=400)
#==========================================================================
work_button = Button(main_win,text="click me",image=save8
,border=0,bg="#3ef1a8",activebackground="#3ef1a8",command=file_ex)
work_button.place(x=770,y=400)
#==========================================================================
art_button = Button(main_win,text="click me",image=save16
,border=0,bg="#3ef1a8",activebackground="#3ef1a8",command=art)
art_button.place(x=990,y=400)
#==========================================================================
button1 = Button(main_win,activebackground="#242425",bg="#242425",border=0,
                                             image=save10,command=shutdown)
button1.place(x=1220,y=1)

button2 = Button(main_win,activebackground="#242425",bg="#242425",border=0,
                                              image=save12,command=restart)
button2.place(x=1185,y=1)

button3 = Button(main_win,activebackground="#242425",bg="#242425",border=0,
                                               image=save14,command=revert)
button3.place(x=1150,y=2)
#==========================================================================
#buttons >>>
#==========================================================================
#Binders <<<
media_button.bind("<Enter>", on_enter_media)
media_button.bind("<Leave>", on_leave_media)

web_button.bind("<Enter>", on_enter_web)
web_button.bind("<Leave>", on_leave_web)

data_button.bind("<Enter>", on_enter_data)
data_button.bind("<Leave>", on_leave_data)

work_button.bind("<Enter>", on_enter_work)
work_button.bind("<Leave>", on_leave_work)

art_button.bind("<Enter>", on_enter_art)
art_button.bind("<Leave>", on_leave_art)

button1.bind("<Enter>", on_enter_button1)
button1.bind("<Leave>", on_leave_button1)
button2.bind("<Enter>", on_enter_button2)
button2.bind("<Leave>", on_leave_button2)
button3.bind("<Enter>", on_enter_button3)
button3.bind("<Leave>", on_leave_button3)
#Binders >>>
#==========================================================================
main_win.mainloop()
