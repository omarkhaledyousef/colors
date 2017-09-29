from Tkinter import*

def clr():
    
    f = open("Selection.txt","w")
    f.write('0'+'\n'+"0"+'\n'+"0"+'\n'+"0")
 
    f.close()
    la4.destroy()
    showresult.destroy()
    la3.destroy()
    clearresult.destroy()
    

def show():
    if female==0:
         fratio="not yet"
         s="."
    else:     
        fratio=(float(rightfemale)/female)*100
        s="%"
        fratio=round(fratio,2)
    if male==0 :
        mratio="not yet"
        ss="."
    else:
     ss="%"
     mratio=(float(maleright)/male)*100
     mratio=round(mratio,2)
    tt="females answered correctly: "+str(fratio)+str(s)+"\n"+"males answered correctly: "+str(mratio)+str(ss)
    la4.config(text=tt,font=('Stylus BT','35',"bold"),fg="black",bg="white")
    clearresult.config(state=NORMAL)


     
def exit():
   page3.withdraw()


def result():

    global page3,la4,la3
    global mratio
    global fratio
    global female
    global male
    global maleright
    global rightfemale
    global showresult,clearresult
    
    
    page2.withdraw()
    page3=Toplevel()
    pagefr=Frame(page3)
    pagefr.pack(expand=1)
    page3.geometry("900x650")
    pagefr.config(bg="white")
    page3.config(bg="white")
    page3.deiconify()



    la3=Label(pagefr)
    la3.grid(row=0,columnspan=4,padx=15)
     

    showresult=Button(pagefr,text="Show results",width=15,height=2,bg="#169BFB",fg="white",font=("BOSKO","15"),command=show)
    showresult.grid(row=2,pady=15,padx=2,column=0)

    clearresult=Button(pagefr,text="Clear results",width=15,height=2,bg="#169BFB",fg="white",font=("BOSKO","15"),command=clr,state=DISABLED)
    clearresult.grid(row=2,pady=15,padx=2,column=1)



    Exit=Button(pagefr,text="Exit",width=15,height=2,bg="#169BFB",fg="white",font=("BOSKO","15"),command=exit)
    Exit.grid(row=2,pady=15,padx=2,column=3)

    la4=Label(pagefr,bg="white")
    la4.grid(row=3,columnspan=4)
   
        
    if c1.get()==c2.get():
        la3.config(text="EXCEllENT!",font=("Forte",'70'),fg="green",bg="white")
        
        
        
    else :
       la3.config(text="NOT PERFECT!",font=("Forte",'70'),fg="red",bg="white")

    #Read each value from file and assign it to int variables to edit it
    #if choice is men -> male +=1 
    #if choice is female -> female +=1
  
    f2 = open("Selection.txt")
    for i, line in enumerate(f2):
      if i==0:
        male=int(line)
      elif i==1:
        female=int(line)
      elif i==2:
        maleright=int(line)
      elif i==3:
        rightfemale=int(line)
    if v1.get()==1:
        male+=1
    elif v1.get()==2:
        female+=1
    if c1.get()==c2.get() and  v1.get()==1:
        maleright+=1
    elif c1.get()==c2.get() and  v1.get()==2:
        rightfemale+=1       
         
    f2.close()

    #cast variables from int to str
    m=(str(male))
    fm=str(female)
    mr=str(maleright)
    fmr=str(rightfemale)

    #open exist file in mode write and create an obj from it {to update data}
    f = open("Selection.txt","w")
    f.write(m+'\n')
    f.write(fm+'\n')
    f.write(mr+'\n')
    f.write(fmr)
    f.close()

    #load values from file 
    f1 = open("Selection.txt")
    for i, line in enumerate(f1):
      if i==0:
        male=int(line)
      elif i==1:
        female=int(line)
      elif i==2:
        maleright=int(line)
      elif i==3:
        rightfemale=int(line)
  
    f2.close()
   
    
    
 
   
def enable2():
  sub3.config(state=NORMAL)
  
def choice1():
     
    global c2
    global sub3
    global page2
    
    page1.withdraw()
    

    
    c2=IntVar()
    
    
    page2=Toplevel()
    pagefr=Frame(page2)
    pagefr.pack(expand=1)
    page2.geometry("900x650")
    pagefr.config(bg="white")
    page2.config(bg="white")
    page2.deiconify()

    pickla=Label(pagefr,text="Try to \n \n Pick \n \nthe same \n \n color!",font=("Forte",'25'),fg="#169BFB",bg="white")
    pickla.grid(pady=2,rowspan=4)

    

    color3=Radiobutton(pagefr,width=15,height=8,bg="#D33F3A",variable=c2,value=3,command=enable2)
    color3.grid(row=1,column=1)

    color6=Radiobutton(pagefr,width=15,height=8,bg="#CD3A2D",variable=c2,value=6,command=enable2)
    color6.grid(row=1,column=2)

    color8=Radiobutton(pagefr,width=15,height=8,bg="#C9403E",variable=c2,value=8,command=enable2)
    color8.grid(row=1,column=3)

    color2=Radiobutton(pagefr,width=15,height=8,bg="#D24336",variable=c2,value=2,command=enable2)
    color2.grid(row=2,column=1)

    color1=Radiobutton(pagefr,width=15,height=8,bg="#D64336",variable=c2,value=1,command=enable2)
    color1.grid(row=2,column=2)
    
    color4=Radiobutton(pagefr,width=15,height=8,bg="#CD392E",variable=c2,value=4,command=enable2)
    color4.grid(row=2,column=3)

    color9=Radiobutton(pagefr,width=15,height=8,bg="#C8403C",variable=c2,value=9,command=enable2)
    color9.grid(row=3,column=1)

    color7=Radiobutton(pagefr,width=15,height=8,bg="#CD4336",variable=c2,value=7,command=enable2)
    color7.grid(row=3,column=2)

    color5=Radiobutton(pagefr,width=15,height=8,bg="#D1403A",variable=c2,value=5,command=enable2)
    color5.grid(row=3,column=3)

    sub3=Button(pagefr,text="Select",command=result,width=15,height=2,bg="#169BFB",state=DISABLED,fg="white",font=("Forte","15"))
    sub3.grid(pady=15,padx=0)

   
    page2.mainloop()

def enable1():
  sub2.config(state=NORMAL)

  
def clc():

    

   
    root.withdraw()
    global page1
    global c1,sub2

    page1=Toplevel()
    pagefr=Frame(page1)
    pagefr.pack(expand=1)
    page1.config(bg="white")
    pagefr.config(bg="white")
    page1.geometry("900x650")
    page1.deiconify()
    
    pickla=Label(pagefr,text="Pick \n \n a color \n \n and keep it \n \n on your \n \n mind!",font=('Forte','25'),fg="#169BFB",bg="white")
    pickla.grid(pady=2,rowspan=4)

    c1=IntVar()
    

    color1=Radiobutton(pagefr,width=15,height=8,bg="#D64336",variable=c1,value=1,command=enable1)
    color1.grid(row=1,column=1,padx=0)

    color2=Radiobutton(pagefr,width=15,height=8,bg="#D24336",variable=c1,value=2,command=enable1)
    color2.grid(row=1,column=2,padx=0)

    color3=Radiobutton(pagefr,width=15,height=8,bg="#D33F3A",variable=c1,value=3,command=enable1)
    color3.grid(row=1,column=3,padx=0)

    color4=Radiobutton(pagefr,width=15,height=8,bg="#CD392E",variable=c1,value=4,command=enable1)
    color4.grid(row=2,column=1,padx=0)

    color5=Radiobutton(pagefr,width=15,height=8,bg="#D1403A",variable=c1,value=5,command=enable1)
    color5.grid(row=2,column=2,padx=0)

    color6=Radiobutton(pagefr,width=15,height=8,bg="#CD3A2D",variable=c1,value=6,command=enable1)
    color6.grid(row=2,column=3,padx=0)

    color7=Radiobutton(pagefr,width=15,height=8,bg="#CD4336",variable=c1,value=7,command=enable1)
    color7.grid(row=3,column=1,padx=0)

    color8=Radiobutton(pagefr,width=15,height=8,bg="#C9403E",variable=c1,value=8,command=enable1)
    color8.grid(row=3,column=2,padx=0)

    color9=Radiobutton(pagefr,width=15,height=8,bg="#C8403C",variable=c1,value=9,command=enable1)
    color9.grid(row=3,column=3,padx=0)

    sub2=Button(pagefr,text="Select",command=choice1,width=15,height=2,bg="#169BFB",state=DISABLED,fg="white",font=("Forte","15"))
    sub2.grid(pady=15,padx=0)

    
    
   
    page1.mainloop()
    
def enable():
  sub.config(state=NORMAL)
    
def main():
    global root
    root=Tk()
    root.title("colors")
    rootfr=Frame(root)
    rootfr.pack(expand=1)
    root.configure(bg="white")
    rootfr.config(bg="white")
    
    global v1,la2,sub

    la=Label(rootfr,text="Choose please",font=('Forte','70'),fg="#169BFB",bg="white")
    la.grid()
    
    v1=IntVar()
    
    male=Radiobutton(rootfr,text="Male",variable=v1,value=1,bg="white",fg="black",font=('Stylus BT','35'),command=enable)
    male.grid()


    
    female=Radiobutton(rootfr,text="Female",variable=v1,value=2,bg="white",fg="black",font=('Stylus BT','35'),command=enable)
    female.grid()


    sub=Button(rootfr,text="Submit",command=clc,width=15,height=2,bg="#3399ff",fg="white",font=('Forte','15'),state=DISABLED)
    sub.grid()

   
    
      


    root.geometry("900x600")
    root.mainloop()
if __name__=="__main__":
    
  main()
    
