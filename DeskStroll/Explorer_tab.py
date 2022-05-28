#imports <<<
from tkinter import  *
from tkinter import ttk
import os
from time import *
import random
import threading
#imports >>>

#====================================== Back end ========================================

# chirld file assigner and generator  <<<   
class Make:
    def __init__(self):
        print("active")
    def send(link):
        link = link
        os.startfile(link)    
    def Child_files(name,link,color,frame):
        name = name
        link = link
        file_ex = name.split(".")
        exten = (repr(file_ex[-1]))
        if len(name) >=25:
          name = name[0:21]     
        else:
            pass
        name = Button(frame,text=name,compound=TOP,fg=color,font=("arial",12,"bold"),
                                                                             border=0)
        name.pack(pady=5)
        name.config(command= lambda : Make.send(link))
        name.config(image=base1)
        range_list = random.randint(1, 100)
        my_canvas.config(width=range_list)
        list1 = [400,396,397,403,401,399,402]
        from_list1 = random.choice(list1)
        my_canvas.config(width=from_list1)
        #==========================================
        if exten == "'mp3'" :
            name.config(image=base10)
        elif exten == "'wav'":
            name.config(image=base10)
        elif exten == "'wma'":
            name.config(image=base10)
        elif exten == "'act'":
            name.config(image=base10)   
        #==========================================
        elif exten == "'docx'":
            name.config(image=base13)   
        elif exten == "'pdf'":
            name.config(image=base13)  
        elif exten == "'xlsx'":
            name.config(image=base13)  
        elif exten == "'txt'" :
            name.config(image=base13) 
        elif exten =="'xls'":
            name.config(image=base13)  
        elif exten == "'ppt'":
            name.config(image=base13)  
        elif exten == "'pptx'" :
            name.config(image=base13)         
        elif exten == "'html'" :
            name.config(image=base13)
        #==========================================
        elif exten == "'gif'":
            name.config(image=base12)
        elif exten == "'png'":
            name.config(image=base12)
        elif exten == "'bmp'":
            name.config(image=base12)        
        elif exten == "'jepg'":
            name.config(image=base12)
        elif exten == "'jpg'":
            name.config(image=base12)
        #==========================================
        elif exten == "'avi'":
            name.config(image=base11)
        elif exten == "'3gp'":
            name.config(image=base11)
        elif exten == "'svi'":
            name.config(image=base11)
        elif exten == "'mpeg'":
            name.config(image=base11)
        elif exten == "'wmv'":
            name.config(image=base11)            
        elif exten == "'mov'":
            name.config(image=base11)
        elif exten == "'flv'":
            name.config(image=base11)
        elif exten == "'mkv'":
            name.config(image=base11)   
        elif exten == "'webm'":
            name.config(image=base11)              
        elif exten == "'mp4'":
            name.config(image=base11)
        #==========================================
        elif exten == "'rar'":
            name.config(image=base14)
        elif exten == "'zip'": 
            name.config(image=base14)
        #==========================================
        elif exten == "'exe'":
            name.config(image=base1)
        #==========================================
        else:
            name.config(image=base7)
        #==========================================    
# chirld file assigner and generator  >>> 
# chirld folder assigner  <<<          
def create_folder_link(link):
    in_ent = link
    dirinfo = os.listdir(in_ent)
    frame = second_frame
    ent.delete(0,"end")
    ent.insert(0, link)
    for i in second_frame.winfo_children():
            i.destroy()
    Object_assign(in_ent,"green",frame)
# chirld folder assigner  >>>    
# chirld folder generator  <<<           
def Child_folders(link,name,color,frame):
        link = link
        name = name       
        if len(name) >=25:          
          name = name[0:21]     
        else:
            pass
# chirld folder generator  >>>                
        name = Button(frame,text=name,compound=TOP,image=base6,fg=color,
                                       font=("arial",12,"bold"),border=0)
        name.pack(pady=5)
        name.config(command= lambda : create_folder_link(link))         
        range_list = random.randint(1, 100)
        my_canvas.config(width=range_list)
        list1 = [400,396,397,403,401,399,402]
        from_list1 = random.choice(list1)
        my_canvas.config(width=from_list1)
# back adresses generator  <<<          
def back():
    entry_info = ent.get()
    file_ex = entry_info.split("\\")
    exten = (repr(file_ex[-1])) 
    
    name_lent = len(exten)
    name_lent = int(name_lent) - 1
    frame = second_frame
    back_address = entry_info[0:-int(name_lent)] 
    ent.delete(0,"end")
    ent.insert(0, back_address)  
    for i in second_frame.winfo_children():
            i.destroy()
    Object_assign(back_address,"red",frame)
# back adresses generator  >>>  
        
# manually assigned adresses  <<<          
def Entery_path_assign(e):
    in_ent = ent.get()
    addtext1 = in_ent.split("\\")
    addtext = (repr(addtext1[-1]))
    frame = second_frame
    for i in second_frame.winfo_children():
            i.destroy()
    Object_assign(in_ent,"blue",frame)
# manually assigned adresses  >>>   
             
# file and dir diffrentiator  <<<  
def Object_assign(new_info,color,frame):
    
    in_ent = new_info  
    dirinfo = os.listdir(in_ent)
     
    for x in dirinfo:
        if os.path.isfile(in_ent+"\\"+x):
            Make.Child_files(x,in_ent+"\\"+x,color,frame)
        else:
            Child_folders(in_ent+"\\"+x, x,color,frame)
# file and dir diffrentiator >>>  

def minimize():
    main_win.attributes("-fullscreen", False)
    main_win.geometry("1280x900")
    main_win.resizable(False,True)

def maximize():
    main_win.attributes("-fullscreen", True)
def exit_window():
    main_win.destroy()    

# chirld file assigner and generator for window 2 <<<  
class Make_2:
    def __init__(self):
        print("active")
    def send(link):
        link = link
        os.startfile(link)    
    def Child_files_2(name,link,color):
        name = name
        link = link
        file_ex = name.split(".")
        exten = (repr(file_ex[-1])).lower()
        if len(name) >=25:
          name = name[0:21]     
        else:
            pass
        
        name = Button(second1_frame,text=name,compound=TOP,fg=color,
                                   font=("arial",12,"bold"),border=0)
        name.pack(pady=5)
        name.config(command= lambda : Make_2.send(link))
        #name.config(image=base1)
        range_list = random.randint(1, 100)
        my1_canvas.config(width=range_list)
        list1 = [400,396,397,403,401,399,402]
        from_list1 = random.choice(list1)
        my1_canvas.config(width=from_list1)
        
        #==========================================
        if exten == "'mp3'" :
            name.config(image=base10)
        elif exten == "'wav'":
            name.config(image=base10)
        elif exten == "'wma'":
            name.config(image=base10)
        elif exten == "'act'":
            name.config(image=base10)   
        #==========================================
        elif exten == "'docx'":
            name.config(image=base13)   
        elif exten == "'pdf'":
            name.config(image=base13)  
        elif exten == "'xlsx'":
            name.config(image=base13)  
        elif exten == "'txt'" :
            name.config(image=base13) 
        elif exten =="'xls'":
            name.config(image=base13)  
        elif exten == "'ppt'":
            name.config(image=base13)  
        elif exten == "'pptx'" :
            name.config(image=base13)         
        elif exten == "'html'" :
            name.config(image=base13)
        #==========================================
        elif exten == "'gif'":
            name.config(image=base12)
        elif exten == "'png'":
            name.config(image=base12)
        elif exten == "'bmp'":
            name.config(image=base12)        
        elif exten == "'jepg'":
            name.config(image=base12)
        elif exten == "'jpg'":
            name.config(image=base12)
        #==========================================
        elif exten == "'avi'":
            name.config(image=base11)
        elif exten == "'3gp'":
            name.config(image=base11)
        elif exten == "'svi'":
            name.config(image=base11)
        elif exten == "'mpeg'":
            name.config(image=base11)
        elif exten == "'wmv'":
            name.config(image=base11)            
        elif exten == "'mov'":
            name.config(image=base11)
        elif exten == "'flv'":
            name.config(image=base11)
        elif exten == "'mkv'":
            name.config(image=base11)   
        elif exten == "'webm'":
            name.config(image=base11)              
        elif exten == "'mp4'":
            name.config(image=base11)
        #==========================================
        elif exten == "'rar'":
            name.config(image=base14)
        elif exten == "'zip'": 
            name.config(image=base14)
        #==========================================
        elif exten == "'exe'":
            name.config(image=base1)
        #==========================================
        else:
            name.config(image=base7)
        #==========================================    
# chirld file assigner and generator for window 2 >>> 

# chirld folder assigner for window 2 <<<          
def create_folder_link_2(link):
    in_ent = link
    dirinfo = os.listdir(in_ent)
    ent2.delete(0,"end")
    ent2.insert(0, link)
    for i in second1_frame.winfo_children():
            i.destroy()
    Object_assign_2(in_ent,"green")
# chirld folder assigner for window 2 >>>    
    
# chirld folder generatorfor window 2  <<<           
def Child_folders_2(link,name,color):
        link = link
        name = name
        
        if len(name) >=25:
          
          name = name[0:21]     
        else:
            pass
 
              
        name = Button(second1_frame,text=name,compound=TOP,image=base6,fg=color,
                                               font=("arial",12,"bold"),border=0)
        name.pack(pady=5)
        name.config(command= lambda : create_folder_link_2(link))         
        range_list = random.randint(1, 100)
        my_canvas.config(width=range_list)
        list1 = [400,396,397,403,401,399,402]
        from_list1 = random.choice(list1)
        my_canvas.config(width=from_list1)
# chirld folder generator  for window 2>>>  

def time_get():
    time_string = strftime("%I:%M:%S %p     %A - %b - %Y")
    time_label.config(text=time_string)
    time_label.after(1000,time_get)

# back adresses generator for window 2 <<<          
def back_2():
    entry_info = ent2.get()
    file_ex = entry_info.split("\\")
    exten = (repr(file_ex[-1])) 
    name_lent = len(exten)
    name_lent = int(name_lent) - 1
    back_address = entry_info[0:-int(name_lent)] 
    ent2.delete(0,"end")
    ent2.insert(0, back_address)  
    for i in second1_frame.winfo_children():
            i.destroy()
    Object_assign_2(back_address,"red")
# back adresses generator for window 2 >>>  
        
# manually assigned adresses for window 2 <<<          
def Entery_path_assign_2(e):
    in_ent = ent2.get()
    addtext1 = in_ent.split("\\")
    addtext = (repr(addtext1[-1]))  
    for i in second1_frame.winfo_children():
            i.destroy()
    Object_assign_2(in_ent,"blue")
# manually assigned adresses for window 2 >>>   
             
# file and dir diffrentiator for window 2  <<<  
def Object_assign_2(new_info,color):
    
    in_ent = new_info  
    dirinfo = os.listdir(in_ent)
     
    for x in dirinfo:
        if os.path.isfile(in_ent+"\\"+x):
            Make_2.Child_files_2(x,in_ent+"\\"+x,color)
            
        else:
            Child_folders_2(in_ent+"\\"+x, x,color)
# file and dir diffrentiator for window 2  >>>  


# effect binding function <<<
def on_button_in(e):
    button1["image"] = base3
def on_button_out(e):
    button1["image"] = base4
def on_button_in_2(e):
    button2["image"] = base3
def on_button_out_2(e):
    button2["image"] = base4
def on_button_in_3(e):
    button3["image"] = base9
def on_button_out_3(e):
    button3["image"] = base8
def on_button_in_4(e):
    button4["image"] = base9
def on_button_out_4(e):
    button4["image"] = base8    
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

# effect binding function <<<
    
#^^^====================================== Back end =====================================

#====================================== Front end =======================================
main_win = Tk()
main_win.attributes("-fullscreen", True)

#image files imports<<<
base1 = PhotoImage(file='img\\buttons\\file_img.png')
base2 = PhotoImage(file='img\\background\\explorer_background.png') 
base3 = PhotoImage(file='img\\buttons\\b_normal.png')
base4 = PhotoImage(file='img\\buttons\\b_hover.png')
base5 = PhotoImage(file='img\\labels_blocks\\bar.png')  
base6 = PhotoImage(file='img\\buttons\\rar_file_img.png')
base7 = PhotoImage(file='img\\buttons\\other_file_img.png')
base8 = PhotoImage(file='img\\buttons\\back_main.png')
base9 = PhotoImage(file='img\\buttons\\back_hover.png')
base10 = PhotoImage(file='img\\buttons\\music_file_img.png')
base11 = PhotoImage(file='img\\buttons\\vid_img.png')
base12 = PhotoImage(file='img\\buttons\\Image_file_img.png')
base13 = PhotoImage(file='img\\buttons\\Doc_Files_img.png')
base14 = PhotoImage(file='img\\buttons\\rar_img.png')
base15 = PhotoImage(file='img\\buttons\\minimize_main.png')
base16 = PhotoImage(file='img\\buttons\\minimize_hover.png')
base17 = PhotoImage(file='img\\buttons\\maximize_main.png')
base18 = PhotoImage(file='img\\buttons\\maximize_hover.png')
base19 = PhotoImage(file='img\\buttons\\exit_main.png')
base20 = PhotoImage(file='img\\buttons\\exit_hover.png')
base21 = PhotoImage(file='img\\icons\\Deskstroll_logo.png')
#image files imports>>>

# Gui structure <<<
#==========================================================================
main_win.iconphoto(True,base21)
main_win.title("DeskStroll")
background_image = Label(main_win,image=base2)
background_image.place(x=0,y=0)
time_label = Label(main_win,font=("arial",9,"bold"),fg="white",bg="#242425")
time_label.place(x=25,y=5)
x = threading.Thread(target=time_get())
back_manu_label = Label(main_win,width=160,height=5)
back_manu_label.pack(pady=80)
#==========================================================================
write_label = Label(back_manu_label,border=0,image=base5)
write_label.place(x=2,y=0)
write_label2 = Label(back_manu_label,border=0,image=base5)
write_label2.place(x=650,y=0)
#==========================================================================
ent = Entry(back_manu_label,font=("helvetica",20),fg="#1ce5aa",width=24,
                                                   border=0,bg="#f0f0f0")
ent.place(x=27,y=18)
ent2 = Entry(back_manu_label,width=27,font=("helvetica",20),fg="#1ce5aa",
                                                    border=0,bg="#f0f0f0")
ent2.place(x=683,y=18)                                                                                                                                              
#==========================================================================
button1 = Button(back_manu_label,image=base4,border=0,command= 
                                lambda : Entery_path_assign(E))
button1.place(x=398,y=15)
button2 = Button(back_manu_label,image=base4,border=0,command= 
                              lambda : Entery_path_assign_2(E))
button2.place(x=1047,y=15)
#==========================================================================
main_frame = Frame(main_win,width=100,)
main_frame.pack(padx=130,side=LEFT,fill=Y)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = ttk.Scrollbar(main_frame,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure
                    (scrollregion = my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")
#==========================================================================
main1_frame = Frame(main_win,width=100,height="500")
main1_frame.pack(side=LEFT,fill=Y,expand=1)
my1_canvas = Canvas(main1_frame)
my1_canvas.pack(side=LEFT, fill=BOTH, expand=3)
my1_scrollbar = ttk.Scrollbar(main1_frame,command=my1_canvas.yview)
my1_scrollbar.pack(side=RIGHT,fill=Y)
my1_canvas.configure(yscrollcommand=my1_scrollbar.set)
my1_canvas.bind('<Configure>', lambda e: my1_canvas.configure
                      (scrollregion = my1_canvas.bbox("all")))
second1_frame = Frame(my1_canvas)
second1_frame.config()
my1_canvas.create_window((0,0), window=second1_frame, anchor="nw")
#==========================================================================
button3 = Button(main_win,activebackground="#49e7a2",bg="#49e7a2",image=base8,
                                                        border=0,command=back)
button3.place(x=124 ,y=203)
button4 = Button(main_win,activebackground="#49e7a2",bg="#49e7a2",image=base8,
                                                      border=0,command=back_2)
button4.place(x=766 ,y=205)
button5 = Button(main_win,activebackground="#242425",bg="#242425",border=0,
                                              image=base15,command=minimize)
button5.place(x=1100,y=3)
button6 = Button(main_win,activebackground="#242425",bg="#242425",border=0,
                                              image=base17,command=maximize)
button6.place(x=1150,y=3)
button7 = Button(main_win,activebackground="#242425",bg="#242425",border=0,
                                           image=base19,command=exit_window)
button7.place(x=1200,y=3)
#==========================================================================
# Gui structure >>>

#hover bindings >>>
button1.bind("<Enter>", on_button_in)
button1.bind("<Leave>", on_button_out)

button2.bind("<Enter>", on_button_in_2)
button2.bind("<Leave>", on_button_out_2)

button3.bind("<Enter>", on_button_in_3)
button3.bind("<Leave>", on_button_out_3)

button4.bind("<Enter>", on_button_in_4)
button4.bind("<Leave>", on_button_out_4)

button5.bind("<Enter>", on_button_in_5)
button5.bind("<Leave>", on_button_out_5)

button6.bind("<Enter>", on_button_in_6)
button6.bind("<Leave>", on_button_out_6)

button7.bind("<Enter>", on_button_in_7)
button7.bind("<Leave>", on_button_out_7)

ent.bind("<Return>",Entery_path_assign)
ent2.bind("<Return>",Entery_path_assign_2)

#hover bindings >>>
#^^^====================================== Front end ====================================
main_win.mainloop()
