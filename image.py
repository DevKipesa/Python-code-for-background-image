from tkinter import*
root=Tk()
root.title("Kipesa trial")
root.resizable(False, False)
root.geometry("500x400")
#background image
imagee= PhotoImage(file= "image/share.png")
bg_image=Label(root, image= imagee).place(x=0, y=0, relwidth=1, relheight=1)
text=Label(root, text= "Welcome to the background image code",font= "bold 15".upper()).place(x=0,y=0)

root.mainloop()