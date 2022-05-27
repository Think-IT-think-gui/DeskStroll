
from pygame import mixer
from tkinter.ttk import *
from tkinter import *
import os
import threading
from time import *
import time
from mutagen.mp3 import MP3
import threading
#==================================================Back end==============================
h = 0
h3 = 0
def playsong():
  currentsong=playlist.get(ACTIVE)
  mixer.music.load(currentsong)
  songstatus.set("Playing")
  mixer.music.play()
  current_possition = mixer.music.get_pos()
  current_bar_level = audio_progress_bar['value']
  x = threading.Thread(target=Bar_loading, daemon=True)
  audio_progress_bar['value']-=current_bar_level
  Main_win.update_idletasks()
  x.start()
 
def autoplaysong():
  global h
  h +=1
  try:
   currentsong=playlist.curselection()
   currentsong = currentsong[0]+h
   currentsong=playlist.get(currentsong)
  except pygame.error:
   h=0 
  currentsong=playlist.curselection()
  currentsong = currentsong[0]+h
  currentsong=playlist.get(currentsong)
  mixer.music.load(currentsong)
  songstatus.set("Playing")
  mixer.music.play()
  current_possition = mixer.music.get_pos()
  current_bar_level = audio_progress_bar['value']
  y = threading.Thread(target=Bar1_loading, daemon=True)
  audio_progress_bar['value']-=current_bar_level
  Main_win.update_idletasks()
  y.start()

def next_song():
  global h3
  h3 +=1
  currentsong=playlist.curselection()
  currentsong = currentsong[0]+h3
  currentsong=playlist.get(currentsong)
  mixer.music.load(currentsong)
  songstatus.set("Playing")
  mixer.music.play()
  current_possition = mixer.music.get_pos()
  current_bar_level = audio_progress_bar['value']
  h = threading.Thread(target=Bar2_loading, daemon=True)
  audio_progress_bar['value']-=current_bar_level
  Main_win.update_idletasks()
  h.start()

def prev_song():
  global h3
  h3 -=1
  currentsong=playlist.curselection()
  currentsong = currentsong[0]+h3
  currentsong=playlist.get(currentsong)
  mixer.music.load(currentsong)
  songstatus.set("Playing")
  mixer.music.play()
  current_possition = mixer.music.get_pos()
  current_bar_level = audio_progress_bar['value']
  i = threading.Thread(target=Bar3_loading, daemon=True)
  audio_progress_bar['value']-=current_bar_level
  Main_win.update_idletasks()
  i.start()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()
    back_value = audio_progress_bar['value']
    info_store = open("text.txt", "w")
    info_store.write(str(back_value))
    info_store.close()  
    pausebtn.config(state=DISABLED)
    Resumebtn.config(state=NORMAL)
    pause_resume_lookup("offline") 

def pause_resume_lookup(factor): 
    factor = factor
    if factor == "offline":
        audio_progress_bar['value']-=5000000
        Main_win.update_idletasks()
    elif factor == "online":
        info = open("text.txt","r")
        info = info.read()
        current_time=audio_progress_bar['value']
        audio_progress_bar['value']+=-current_time+ float(info) 
        
        
def voldown():
    volume_sound = mixer.music.get_volume()
    volume_sound -=0.1
    mixer.music.set_volume(volume_sound )
def volup():
    volume_sound = mixer.music.get_volume()   
    volume_sound +=0.1
    mixer.music.set_volume(volume_sound )  
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
    current_time=audio_progress_bar['value']
    other = 100 - current_time
    audio_progress_bar['value']+= other 
   
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()
    pausebtn.config(state=NORMAL)
    Resumebtn.config(state=DISABLED)
    pause_resume_lookup("online")    
vol_level = 0

def Bar_loading():
    currentsong=playlist.get(ACTIVE)
    currentsong = currentsong
    file_info =MP3(currentsong)
    file_info = file_info.info.length
    print(file_info)
    Split_time = file_info/1000
    t = open("new.txt", "w")
    t.write(str(Split_time))
    t.close()
    task_Legnth = 1000
    x = 0   
    while((x<task_Legnth)):
      t = open("new.txt", "r")
      t = t.read()
      Split_time = float(t)
      audio_progress_bar['value']+=0.1
      x+=1
      Main_win.update_idletasks()
      time.sleep(Split_time)
    Split_time = 0
    audio_progress_bar['value']-=100
    Main_win.update_idletasks()
    autoplaysong()
 
def Bar1_loading():
    currentsong=playlist.curselection()
    currentsong = currentsong[0]+h
    currentsong=playlist.get(currentsong)
    currentsong = currentsong
    file_info =MP3(currentsong)
    file_info = file_info.info.length
    print(file_info)
    Split_time = file_info/1000
    task_Legnth = 1000
    x = 0   
    while(x<task_Legnth):
      audio_progress_bar['value']+=0.1
      x+=1
      Main_win.update_idletasks()
      time.sleep(Split_time)
    audio_progress_bar['value']-=100
    Main_win.update_idletasks()
    autoplaysong()

def minimize():
    Main_win.attributes("-fullscreen", False)
    Main_win.geometry("1280x1100")
    Main_win.resizable(False,True)

def maximize():
    Main_win.attributes("-fullscreen", True)

def exit_window():
    Main_win.destroy()    

def time_get():
    time_string = strftime("%I:%M:%S %p     %A - %b - %Y")
    time_label.config(text=time_string)
    time_label.after(1000,time_get)   

def Bar2_loading():
    currentsong=playlist.curselection()
    currentsong = currentsong[0]+1
    currentsong=playlist.get(currentsong)
    currentsong = currentsong
    file_info =MP3(currentsong)
    file_info = file_info.info.length
    print(file_info)
    Split_time = file_info/1000
    task_Legnth = 1000
    x = 0   
    while(x<task_Legnth):
      audio_progress_bar['value']+=0.1
      x+=1
      Main_win.update_idletasks()
      time.sleep(Split_time)
    audio_progress_bar['value']-=100
    Main_win.update_idletasks()
    autoplaysong()

def Bar3_loading():
    currentsong=playlist.curselection()
    currentsong = currentsong[0]-1
    currentsong=playlist.get(currentsong)
    currentsong = currentsong
    file_info =MP3(currentsong)
    file_info = file_info.info.length
    print(file_info)
    Split_time = file_info/1000
    task_Legnth = 1000
    x = 0   
    while(x<task_Legnth):
      audio_progress_bar['value']+=0.1
      x+=1
      Main_win.update_idletasks()
      time.sleep(Split_time)
    audio_progress_bar['value']-=100
    Main_win.update_idletasks()
    autoplaysong()

def get_list():
  path_info = song_list_input.get()      
  os.chdir(path_info)
  playlist.config()
  songs=os.listdir()
  for s in songs:
    file_ex = s.split(".")
    exten = (repr(file_ex[-1]))
    if exten == "'mp3'":
      playlist.insert(END,s)
    elif exten == "'wav'" : 
      playlist.insert(END,s)
    elif exten == "'wma'" : 
      playlist.insert(END,s)
    elif exten == "'act'" : 
      playlist.insert(END,s)
    elif exten == "'m4a'" : 
      playlist.insert(END,s)    
    pass

#binding functions
def playbtn_in(e):
    playbtn["image"] = save4
def playbtn_out(e):
    playbtn["image"] = save3
def pausebtn_in(e):
    pausebtn["image"] = save6
def pausebtn_out(e):
    pausebtn["image"] = save5
def Resumebtn_in(e):
    Resumebtn["image"] = save8
def Resumebtn_out(e):
    Resumebtn["image"] = save7
def next_audio_in(e):
    next_audio["image"] = save10
def next_audio_out(e):
    next_audio["image"] = save9
def prev_audio_in(e):
    prev_audio["image"] = save12
def prev_audio_out(e):
    prev_audio["image"] = save11  
def stopbtn_in(e):
    stopbtn["image"] = save14
def stopbtn_out(e):
    stopbtn["image"] = save13  
def Increase_volume_button_in(e):
    Increase_volume_button["image"] = save16
def Increase_volume_button_out(e):
    Increase_volume_button["image"] = save15  
def Decrease_volume_button_in(e):
    Decrease_volume_button["image"] = save18
def Decrease_volume_button_out(e):
    Decrease_volume_button["image"] = save17 
def generate_list_in(e):
    generate_list["image"] = save20
def generate_list_out(e):
    generate_list["image"] = save19    
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
#binding functions
#==================================================Back end==============================

#==================================================front end=============================
Main_win = Tk()
Main_win.attributes("-fullscreen", True)
mixer.init()
songstatus=StringVar()
#volume_sound = 0.9
count =1 
songstatus.set("choosing")
#=====================================================================================
#images imports <<<
save1 = PhotoImage(file='img//background//music_background.png')
save2 = PhotoImage(file='img//labels_blocks//cover_horizontal.png')
save3 = PhotoImage(file='img//buttons//play_main.png')
save4 = PhotoImage(file='img//buttons//play_hover.png')
save5 = PhotoImage(file='img//buttons//pause_main.png')
save6 = PhotoImage(file='img//buttons//pause_hover.png')
save7 = PhotoImage(file='img//buttons//resume_main.png')
save8 = PhotoImage(file='img//buttons//resume_hover.png')
save9 = PhotoImage(file='img//buttons//next_main.png')
save10 = PhotoImage(file='img//buttons//next_hover.png')
save11 = PhotoImage(file='img//buttons//previouse_main.png')
save12 = PhotoImage(file='img//buttons//previouse_hover.png')
save13 = PhotoImage(file='img//buttons//stop_main.png')
save14 = PhotoImage(file='img//buttons//stop_hover.png')
save15 = PhotoImage(file='img//buttons//high_sound_main.png')
save16 = PhotoImage(file='img//buttons//high_sound_hover.png')
save17 = PhotoImage(file='img//buttons//low_sound_main.png')
save18 = PhotoImage(file='img//buttons//low_sound_hover.png')
save19 = PhotoImage(file='img//buttons//audio_scan_main.png')
save20 = PhotoImage(file='img//buttons//audio_scan_hover.png')
base15 = PhotoImage(file='img\\buttons\\minimize_main.png')
base16 = PhotoImage(file='img\\buttons\\minimize_hover.png')
base17 = PhotoImage(file='img\\buttons\\maximize_main.png')
base18 = PhotoImage(file='img\\buttons\\maximize_hover.png')
base19 = PhotoImage(file='img\\buttons\\exit_main.png')
base20 = PhotoImage(file='img\\buttons\\exit_hover.png')
base21 = PhotoImage(file='img\\icons\\Deskstroll_logo.png')
#images imports >>>
#=====================================================================================
#wallpaper <<<
Main_win.iconphoto(True,base21)
Main_win.title("DeskStroll")
wallpaper_label = Label(Main_win,image=save1,border=0)
wallpaper_label.pack(fill=BOTH)
time_label = Label(Main_win,font=("arial",9,"bold"),fg="white",bg="#242425")
time_label.place(x=25,y=1)
q = threading.Thread(target=time_get())
q.start()
#wallpaper >>>
#Gui objects <<<
#=====================================================================================
playlist =Listbox(Main_win,selectborderwidth=0,justify="center"
,font=("bell mt",17),highlightbackground="#f0f0f0",
highlightthickness=0,selectmode=SINGLE,selectbackground="#cf59f2",
bg="#f0f0f0",fg="#8a22a8",border=0,width=98,height=6)
playlist.place(x=48,y=830)
#=====================================================================================
s = Style()
s.theme_use('alt')
s.configure("TProgressbar",background="#db6df9",troughcolor="white")


audio_progress_bar = Progressbar(Main_win,orient=HORIZONTAL,style="TProgressbar",length=1190)
audio_progress_bar.place(x=44,y=740)
#=====================================================================================
#cover labels
cover_label = Label(Main_win,border=0,image=save2)
cover_label.place(x=43,y= 728)
cover_label2 = Label(Main_win,border=0,image=save2)
cover_label2.place(x=43,y= 754)
#cover labels
#=====================================================================================
playbtn = Button(Main_win,border=0,image=save3,command=playsong)
playbtn.place(x=604,y=760)
#=====================================================================================
pausebtn = Button(Main_win,border=0,image=save5,command=pausesong)
pausebtn.place(x=560,y=773)
#=====================================================================================
Resumebtn=Button(Main_win,border=0,image=save7,command=resumesong)
Resumebtn.place(x=670,y=773)
#=====================================================================================
next_audio = Button(Main_win,border=0,image=save9,command=next_song)
next_audio.place(x=715,y=773)
#=====================================================================================
prev_audio = Button(Main_win,border=0,image=save11,command=prev_song)
prev_audio.place(x=515,y=773)
#=====================================================================================
stopbtn=Button(Main_win,border=0,image=save13,command=stopsong)
stopbtn.place(x=760,y=773)

#=====================================================================================
Increase_volume_button =  Button(Main_win,border=0,image=save15,command=volup)
Increase_volume_button.place(x=1190,y=773)
#=====================================================================================
Decrease_volume_button = Button(Main_win,border=0,image=save17,command=voldown)
Decrease_volume_button.place(x=1150,y=773)
#=====================================================================================
song_list_input = Entry(Main_win,width=70,bg="#f0f0f0",border=0,fg="#db6df9",
                                                        font=("helvetica",20))
song_list_input.place(x=60,y=43) 
#=====================================================================================
generate_list = Button(Main_win,border=0,image=save19,command=get_list)
generate_list.place(x=1090,y=40)
#==========================================================================
button5 = Button(Main_win,activebackground="#242425",state=DISABLED,bg="#242425",
                                           border=0,image=base15,command=minimize)
button5.place(x=1100,y=0)
button6 = Button(Main_win,activebackground="#242425",bg="#242425",border=0,
                                              image=base17,command=maximize)
button6.place(x=1150,y=0)
button7 = Button(Main_win,activebackground="#242425",bg="#242425",border=0,
                                           image=base19,command=exit_window)
button7.place(x=1200,y=0)
#==========================================================================
#Gui objects >>>
#binders
#=====================================================================================
playbtn.bind("<Enter>", playbtn_in)
playbtn.bind("<Leave>", playbtn_out)

#=====================================================================================
pausebtn.bind("<Enter>", pausebtn_in)
pausebtn.bind("<Leave>", pausebtn_out)
#=====================================================================================

Resumebtn.bind("<Enter>", Resumebtn_in)
Resumebtn.bind("<Leave>", Resumebtn_out)
#=====================================================================================

next_audio.bind("<Enter>", next_audio_in)
next_audio.bind("<Leave>", next_audio_out)
#=====================================================================================

prev_audio.bind("<Enter>", prev_audio_in)
prev_audio.bind("<Leave>", prev_audio_out)
#=====================================================================================

stopbtn.bind("<Enter>", stopbtn_in)
stopbtn.bind("<Leave>", stopbtn_out)
#=====================================================================================

Increase_volume_button.bind("<Enter>", Increase_volume_button_in)
Increase_volume_button.bind("<Leave>", Increase_volume_button_out)
#=====================================================================================

Decrease_volume_button.bind("<Enter>", Decrease_volume_button_in)
Decrease_volume_button.bind("<Leave>", Decrease_volume_button_out)
#=====================================================================================

generate_list.bind("<Enter>", generate_list_in)
generate_list.bind("<Leave>", generate_list_out)
#=====================================================================================

song_list_input.bind("<Return>", get_list)
#=====================================================================================

#=======================================binders========================================
button5.bind("<Enter>", on_button_in_5)
button5.bind("<Leave>", on_button_out_5)

button6.bind("<Enter>", on_button_in_6)
button6.bind("<Leave>", on_button_out_6)

button7.bind("<Enter>", on_button_in_7)
button7.bind("<Leave>", on_button_out_7)
#=======================================binders========================================
#
#==================================================front end============================
mainloop()