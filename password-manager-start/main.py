from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import json 


##Constants 
windowbg_color = "#89CFF3"
canvasbg_color = "#89CFF3"
FONT_NAME ="Times New Roman"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
 
# ---------------------------- SAVE PASSWORD ------------------------------- #
##First save password into Dict  ##website ,password ,email
 
def get_info():
   
     
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data ={
             website :{
                  "email" :email,
                  "password":password
        }}
    
    try:
        with open("data.json","r") as file_name :
            ##Reading old data
            loaded_data = json.load(file_name)
    except FileNotFoundError as error:
        loaded_data.update(new_data)
        print(error)
    else:
        with open("data.json","w") as file_name:
            json.dump(loaded_data,file_name,indent=4)
    finally:
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        email_entry.delete(0,END)

        
def find_password():
        website = website_entry.get()
        with open("data.json","r") as file_name :
            ##Reading old data
            loaded_data = json.load(file_name)
        if website in loaded_data:
            email = loaded_data[website]["email"]
            password = loaded_data[website]["password"]
            email_entry.delete(0,END)
            password_entry.delete(0,END)
            email_entry.insert(0,email)
            password_entry.insert(0,password)
            


    


# ---------------------------- UI SETUP ------------------------------- #
window  = Tk()
window.title("UI Password")
window.config(padx=100, pady=50,bg=windowbg_color)
bg_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200,bg=canvasbg_color,highlightthickness=0)
canvas.create_image(100,100,image=bg_image)
#timer_text = canvas.create_text(103,112,text="00:00",fill="white",font=(FONT_NAME,28,"bold"))
canvas.grid(column=1, row=1)

#Labels
website_label = Label(text="Website :",bg=canvasbg_color,font=(FONT_NAME,12,"bold"))
website_label.grid(column=0,row=2)
email_label = Label(text="Email :",bg=canvasbg_color,font=(FONT_NAME,12,"bold"))
email_label.grid(column=0 , row=3)
password_label = Label(text="Password :",bg=canvasbg_color,font=(FONT_NAME,12,"bold"))
password_label.grid(column=0,row=4)

##Entries 
website_entry = Entry(width=35,bg=canvasbg_color,highlightthickness=0)
website_entry.focus()
email_entry = Entry(width=35,bg=canvasbg_color,highlightthickness=0)
email_entry.insert(0,"iamism@gmail.com")
password_entry = Entry(width=25,bg=canvasbg_color,highlightthickness=0)

website_entry.grid(column=1,row=2,columnspan=2)
email_entry.grid(column=1,row=3,columnspan=2)
password_entry.grid(column=1,row=4)

##Buttons
generate_password = Button(text="Generate Password",bg=canvasbg_color,highlightthickness=0,command=generate_password)
add_button = Button(text ="Add",width=25,command=get_info)
generate_password.grid(row=3,column=2)
add_button.grid(row=5 ,column=1,columnspan=2)
search_button = Button(text="search",width=25,command=find_password)
search_button.grid(row=4,column=2)

window.mainloop()