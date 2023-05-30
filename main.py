import tkinter
#this is libarory for GUI 
root_window=tkinter.Tk()
root_window.title("To do list ")
bg_color='#007acc'
root_window.geometry('1280x720')
button_width=3
lable_border=tkinter.GROOVE
lable_fg_color='white'
lable_bg='#007acc'
#Title of interface
title = tkinter.Label(root_window, pady=2, text="Time Shedular ", bd=12,width=1280,
bg=bg_color, fg='gold',font=('times new roman', 25,'bold'),relief=tkinter.GROOVE,justify=tkinter.CENTER)
title.pack()



if __name__=="__main__" :
    #FRAME 0  :
    F_outer_left = tkinter.LabelFrame(root_window, bd=10,text='  Add task : ', relief=tkinter.GROOVE, font=('times new romon', 15, 'bold'),
    fg = 'gold', bg = bg_color)
    F_outer_left.place(x=10, y=80, width=620,height=610)

    lab1 = tkinter.Label(F_outer_left, text=' Time : ', font=('times new romon', 18, 'bold'),bg=bg_color
    ,fg=lable_fg_color).grid(row=0, column=0, padx=0, pady=20)

    j=1




    lab2 = tkinter.Label(F_outer_left, text=' From : ', font=('times new romon', 18, 'bold'), bg=bg_color
                         , fg=lable_fg_color).grid(row=1, column=0, padx=0, pady=0)

    F_out_right = tkinter.LabelFrame(root_window, bd=10, relief=tkinter.GROOVE, font=('times new romon', 15, 'bold'),
                            fg='gold', bg=bg_color)
    F_out_right.place(x=640, y=80, width=625, height=40)
    root_window.mainloop()
"""
    #Frame 1
    F1=tkinter.Frame(root_window)
    F1_1 = tkinter.Frame(F1,width=4)        #label 1 : from
    F1_2 = tkinter.Frame(F1)        #time box
    F1_3 = tkinter.Frame(F1)        #label 2 : to
    F1_4 = tkinter.Frame(F1)        #time box
    F1_1.pack()
    F1_2.pack(side='right')
    F1_3.pack()
    F1_4.pack(side='right')
    F1.pack()
    #label : "from"
    lab1_f1 = tkinter.Label(F1_1, text='From :', relief=lable_border, font=('times new romon', 15, 'bold'),
                            fg='gold', bg=bg_color)
    lab1_f1.pack()
    #time box 1
    F1_2_1 = tkinter.Frame(F1_2)
    F1_2_2 = tkinter.Frame(F1_2)
    F1_2_3 = tkinter.Frame(F1_2)
    j = 1
    for i in range(1, 5):
        b1 = tkinter.Button(F1_2_1, text=str(j), padx=2, pady=2, width=button_width)
        j += 1
        b1.pack(side='left')
    for j in range(5, 9):
        b1 = tkinter.Button(F1_2_2, text=str(j), padx=2, pady=2, width=button_width)
        j += 1
        b1.pack(side='left')
    for j in range(9, 13):
        b1 = tkinter.Button(F1_2_3, text=str(j), padx=2, pady=2, width=button_width)
        j += 1
        b1.pack(side='left')
    F1_2_1.pack(side='top')
    F1_2_2.pack(side='top')
    F1_2_3.pack(side='top')
    F1.pack()
    #lable "to" :
    lab1_f3 = tkinter.Label(F1_1, text='To :', relief=lable_border, font=('times new romon', 15, 'bold'),
                            fg='gold', bg=bg_color)
    lab1_f3.pack()

    #table box 2 :
    F1_4_1 = tkinter.Frame(F1_4)
    F1_4_2 = tkinter.Frame(F1_4)
    F1_4_3 = tkinter.Frame(F1_4)
    j = 1
    for i in range(1, 5):
        b1 = tkinter.Button(F1_2_1, text=str(j), padx=2, pady=2, width=button_width)
        j += 1
        b1.pack(side='left')
    for j in range(5, 9):
        b1 = tkinter.Button(F1_2_2, text=str(j), padx=2, pady=2, width=button_width)
        j += 1
        b1.pack(side='left')
    for j in range(9, 13):
        b1 = tkinter.Button(F1_2_3, text=str(j), padx=2, pady=2, width=button_width)
        j += 1
        b1.pack(side='left')
    F1_4_1.pack(side='top')
    F1_4_2.pack(side='top')
    F1_4_3.pack(side='top;)
"""

