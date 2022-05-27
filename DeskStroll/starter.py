from tkinter import  *
import pywintypes
import win32api
import win32con
import os  
#========================================================================================  
def change():
   devmode = pywintypes.DEVMODEType()
   devmode.PelsWidth = 1280
   devmode.PelsHeight = 1024
   devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
   win32api.ChangeDisplaySettings(devmode,0) 
   st()
def st():
   os.startfile("main_menu.exe")
   main_win.quit()
def on_enter_button1(e):
    b1["image"] = save3
def on_leave_button1(e):
    b1["image"] = save2      
#========================================================================================  

#========================================================================================  

main_win =Tk()
main_win.title("DeskStroll")
save1 = PhotoImage(file='img//background//mini_back.png')
save2 = PhotoImage(file='img//buttons//first_click.png')
save3 = PhotoImage(file='img//buttons//hover_click.png')
background = Label(main_win,image=save1,border=0)
background.pack()
wid = main_win.winfo_screenwidth()
hig = main_win.winfo_screenheight()
info_wid = open("info_wid","w")
info_wid.write(str(wid))
info_wid.close()
info_hig = open("info_hig","w")
info_hig.write(str(hig))
info_hig.close()
#========================================================================================

#========================================================================================  
b1 = Button(main_win,image=save2,bg="#3fe68b",activebackground="#3fe68b",border=0,
                                                                     command=change)
b1.place(x=160,y=330)
b1.bind("<Enter>", on_enter_button1)
b1.bind("<Leave>", on_leave_button1)
#========================================================================================

main_win.mainloop()
