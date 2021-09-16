 from tkinter import *
 import random  

 root=Tk()
 root.title("List")
 root.geometry("400x400")
 
 random_number_list = Label(root)
 random_number_sorted_list  = Label(root)
 
 def randomList():
     randomList = random.sample(range(10,30),5)
     random_number_list["text"] = "Extrordinarly Random list " + str(randomList)
     randomList.sort()
     random_number_sorted_list["text"] = "Extrordinarly Sorted list :" + str(randomList)
 
    
 btn=Button(root,text="Generate Stuff",command=randomList)
 btn.place(relx=0.5,rely=0.4,anchor=CENTER)
 
 random_number_list.place(relx=0.5, rely=0.5, anchor=CENTER)
 random_number_sorted_list.place(relx=0.5, rely=0.6, anchor=CENTER)
 
 root.mainloop()