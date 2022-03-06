from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("750x450")
bgImage=PhotoImage(file=r"votebg1.png")
Label(root,image=bgImage).place(relwidth=1,relheight=1)
root.title("Simple voitng system")
lst=["ruchita","vignesh","swati","parth","pawan","sakshi"]
number_of_voters=len(lst)
voted=[]
def start():
    root=Tk()
    root.geometry("400x500")
    name1=entry1.get()
    name2=entry2.get()
    def login():
        entry_value=entry.get()
        if entry_value in lst:
           tmsg.showinfo("voter",f"{entry_value} wants to login in")
           lbl["text"]=f"{entry_value} is a voter"
           vote_a["stat"]="normal"
           vote_b["stat"]="normal"

           if entry_value in voted:
              lbl["text"]=f"{entry_value} is logged in"
              tmsg.showinfo("Error",f"{entry_value} already voted")
              vote_a["stat"]="disabled"
              vote_b["stat"]="disabled"
           else:
              voted.append(entry_value)
    def votea():
        global scorea
        scorea+=1
        #score_lbl_a["text"]=f"Vote A is: {scorea}"
        vote_a["stat"]="disabled"
        vote_b["stat"]="disabled"
    def voteb():
        global scoreb
        scoreb+=1
        #score_lbl_b["text"]=f"Vote b is: {scoreb}"
        vote_a["stat"]="disabled"
        vote_b["stat"]="disabled"
    def result():
        if scorea>scoreb:
           percentage=(scorea/number_of_voters)*100
           label3=Label(root,text=f"{name1} won with {percentage} %",bg="green",font=("Helvetica",15,"bold"))
           label3.pack()
        elif scoreb>scorea:
           percentage=(scoreb/number_of_voters)*100
           label4=Label(root,text=f"{name2} won with {percentage} %",bg="green",font=("Helvetica",15,"bold"))
           label4.pack()
        else:
           label5=Label(root,text="Both have same votes",bg="red",font=("Helvetica",15,"bold"))
           label5.pack()
    f1=Frame(root,borderwidth=10,bg="purple")
    f1.pack(fill=X)
    label6=Label(f1,text="Enter Username:",bg="pink",font=("Georgia",15,"bold"))
    label6.pack(pady=15)
    entry =Entry(f1,font=("Helvetica",20,"bold"))
    entry.pack()
    login_btn=Button(f1,text="Submit",bg="yellow",font=("Helvetica",15,"bold"),command=login)
    login_btn.pack(pady=10)        
    lbl=Label(root,text="",fg="green",font=("Helvetica",15,"bold"))
    lbl.pack()
    vote_a=Button(root,text=f"Vote-{name1}",stat="disabled",command=votea,font=("Georgia",15,"bold"),bg="grey",fg="black")
    vote_a.pack(fill=X,padx=20,pady=15)
    vote_b=Button(root,text=f"Vote-{name2}",stat="disabled",command=voteb,font=("Georgia",15,"bold"),bg="grey",fg="black")
    vote_b.pack(fill=X,padx=20,pady=15)
    resu=Button(root,text="Result",bg="lightblue",font=("Helvetica",15,"bold"),command=result)
    resu.pack()
    score_lbl_a=Label(root,text="")
    score_lbl_a.pack()
    score_lbl_b=Label(root,text="")
    score_lbl_b.pack()
scorea=0
scoreb=0
label3=Label(root,text="!Welcome to voting system!",fg="pink",bg="black",font=("Times New Roman",20,"italic","bold"))
label3.pack(pady=15)
label1=Label(root,text="1st Nominee Name:",fg="pink",bg="black",font=("Georgia",15,"bold"))
label1.pack(pady=15)
entry1=Entry(root,textvariable=label1,font=("Helvetica",15,"bold"))
entry1.pack(pady=15)
label2=Label(root,text="2st Nominee Name:",fg="pink",bg="black",font=("Georgia",15,"bold"))
label2.pack(pady=15)
entry2=Entry(root,textvariable=label2,font=("Helvetica",15,"bold"))
entry2.pack(pady=15)
btn1=Button(root,text="start",command=start,bg="black",fg="white",font=("Georgia",15,"bold"))
btn1.pack()

root.mainloop()
