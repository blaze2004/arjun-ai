from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
import requests
# from smalltalkdownloader import *
from smalltalk import *

#____________________________________________________________________________________________________________________________________________________________________
# main app class
class rootApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.font = font.Font(family="Helvetica", size=25, weight="bold")

        self.geometry("400x700")
        self.resizable(width=False, height=False)
        self.title("Arjun")
        self.iconbitmap(default="logo.ico")
        #we will place mltiple frames in a container
        #and show the one we want

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for i in (HomePage, OPTIONSPAGE, Setting, Help_Support):
            page_name = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page_name] = frame

            #put all of the pages in the same location
            #the one on the top of the stacking order
            #will be the one that is visible

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

#____________________________________________________________________________________________________________________________________________________________________
# autoscroll class
class AutoScroll(Scrollbar):

    # defining set method with all
    # its parameter
    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:

            #using grid_remove
            self.tk.call("place", "forget", self)
        
        else:
            self.place(x=382, y=50, height=610)
        Scrollbar.set(self, low, high)
    
#____________________________________________________________________________________________________________________________________________________________________
# homepage class
user_input = ""
class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")

        Title = Label(self, font= controller.font, text="Arjun", bg="black", fg="white")
        Title.pack()
        b1 = Button(self, font=("Helvetica",15), fg="white", bg="black", activebackground="black",  borderwidth=0, text="ΞΞ", command=lambda: controller.show_frame("OPTIONSPAGE"))
        b1.place(x=2, y=2)

        def send():
            global user_input
            user_input = EntryBox.get("0.0", END).strip("\n")
            if user_input == " Ask Arjun...":
                user_input = ""
            mic_btn.place(x=367, y=665)
            cut.place_forget()
            userbubble(user_input)
            EntryBox.delete("0.0", END)
            EntryBox.config(bg="black", fg="white", width=50)
            EntryBox.config(insertbackground="white")
            Send_btn.place_forget()
            reply = TODO.arjun_response(self, user_input.lower())
            arjunbubble(reply)
            EntryBox.insert("0.0", " Ask Arjun...")
        
        def empty():
            mic_btn.place(x=367, y=665)
            cut.place_forget()
            EntryBox.delete("0.0", END)
            EntryBox.config(bg="black", fg="white", width=50)
            EntryBox.config(insertbackground="white")
            Send_btn.place_forget()
            cut.place_forget()

        def clear(event):
            help_msg = EntryBox.get("0.0", "1.22")
            if help_msg == " Ask Arjun...":
                EntryBox.delete("0.0", END)

        def add(event):
            EntryBox.config(bg="white", fg="black", width=43)
            EntryBox.config(insertbackground="black")
            cut.place(x=340, y=665)
            Send_btn.place(x=367, y=665)
            help_msg = EntryBox.get("0.0", "1.22")
            mic_btn.place_forget()
            if help_msg == " Ask Arjun...":
                EntryBox.delete("0.0", END)
        
        def enter(event):
            send()

        def hear():
            r = sr.Recognizer()
            audio = ""

            with sr.Microphone() as source:
                arjunbubble("Listening...")
                audio = r.listen(source, phrase_time_limit=5)
            
            try:
                text = r.recognize_google(audio, language="en")
                EntryBox.config(bg="white", fg="black", width=43)
                EntryBox.config(insertbackground="black")
                cut.place(x=340, y=665)
                mic_btn.place_forget()
                Send_btn.place(x=367, y=665)
                EntryBox.delete("0.0", END)
                EntryBox.insert("0.0", text)
                return

            except:
                ans = random.choice(EXCEPTION_VOICE)
                arjunbubble(ans.lower())
                return

        EntryBox = Text(self, bd=2, bg="black", fg="White", width=50, height=2)
        EntryBox.insert("0.0", " Ask Arjun...", END)
        EntryBox.config(insertbackground="white", selectbackground="black", wrap=WORD)
        EntryBox.bind("<Enter>", clear)
        EntryBox.bind("<Key>", add)
        EntryBox.bind("<Return>", enter)
        EntryBox.place(x=-3, y=665)

        Send_img = Image.open("send.png").resize((32,34))
        send_img = ImageTk.PhotoImage(Send_img)
        Send_btn = Button(self, bd=0, command=send, image=send_img, bg="white", activebackground="white", fg="black")
        Send_btn.image = send_img

        mic_img = Image.open("mic.png").resize((32,34))
        mic_img = ImageTk.PhotoImage(mic_img)
        mic_btn = Button(self, bd=0, command=hear, image=mic_img, bg="black", activebackground="black")
        mic_btn.image = mic_img
        mic_btn.place(x=367, y=665)

        cut = Button(self, bd=0, bg="white", activebackground="white", command=empty, fg="black", text="X", font=("Helvetica", 15, "bold"))
        google_img = Image.open("google.png").resize((50,50))
        google_img_Chatlog  = ImageTk.PhotoImage(google_img)

        user_img = Image.open("user.png").resize((32,34))
        user_img_Chatlog = ImageTk.PhotoImage(user_img)

        arjun_img = Image.open("arjun.png").resize((45,48))
        arjun_img_Chatlog = ImageTk.PhotoImage(arjun_img)

        # lets create the gui to show output
        self.Chatlog = Text(self, bd=0, bg="black", fg="white", width=47, height=38, wrap=WORD, cursor="arrow")
        self.Chatlog.place(x=1, y=50)
        scrollbar = AutoScroll(self, command=self.Chatlog.yview)
        self.Chatlog['yscrollcommand'] = scrollbar.set
        scrollbar.place(x=382, y=50, height=610)
        
        color = "green"
        color1 ="blue"
        def show():
            self.Chatlog.tag_configure('user_time', foreground="black")

        def show1():
            self.Chatlog.tag_configure('arjun_time', foreground="black")
        
        def hide():
            self.Chatlog.tag_configure('user_time', foreground="green")
        
        def hide1():
            self.Chatlog.tag_configure('arjun_time', foreground="blue")

        self.Chatlog.config(insertbackground="white", state=DISABLED)
        self.Chatlog.tag_configure('user_msg', justify=RIGHT, background="green", font=("arial", 12, "bold"))
        self.Chatlog.tag_configure('arjun_repl', justify=LEFT, background="blue", font=("arial", 12, "bold"))
        self.Chatlog.tag_configure('google')
        self.Chatlog.tag_configure('user_time', justify=RIGHT, foreground=color, background="green", font=("Helvetica", 12, "bold"))
        self.Chatlog.tag_configure('arjun_time', justify=LEFT, foreground=color1, background="blue", font=("Helvetica", 12, "bold"))
        self.Chatlog.tag_bind('user_time', "<Enter>", lambda event, color= color: show())
        self.Chatlog.tag_bind('arjun_time', "<Enter>", lambda event, color= color1: show1())
        self.Chatlog.tag_bind('user_time', "<Leave>", lambda event, color= color: hide())
        self.Chatlog.tag_bind('arjun_time', "<Leave>", lambda event, color= color1: hide1())

        def chatinitializer(message):
            time_repl = int(datetime.datetime.now().hour)
            if time_repl> 12:
                time_repl = str(time_repl-12) + datetime.datetime.now().strftime(":%M") + " PM"
            elif time_repl == 12:
                time_repl = datetime.datetime.now().strftime("%H:%M") + " PM"
            else:
                time_repl = datetime.datetime.now().strftime("%H:%M") + " AM"

            if message != None:
                self.Chatlog.config(state=NORMAL)
                self.Chatlog.image_create(END, image=arjun_img_Chatlog)
                self.Chatlog.insert(END, " "+message+" ", 'arjun_repl')
                self.Chatlog.insert(END, " "+time_repl+"\n", 'arjun_time')
                self.Chatlog.insert(END, "\n")
                self.Chatlog.config(state=DISABLED)
                self.Chatlog.yview(END)
                self.Chatlog.update_idletasks()
        chatinitializer(random.choice(chatinitializer_words))

        def userbubble(message):
            time_sent = int(datetime.datetime.now().hour)
            if time_sent > 12:
                time_sent = str(time_sent-12) + datetime.datetime.now().strftime(":%M") + " PM"
            elif time_sent == 12:
                time_sent = datetime.datetime.now().strftime("%H:%M") + " PM"
            else:
                time_sent = datetime.datetime.now().strftime("%H:%M") + " AM"

            if message != None:
                self.Chatlog.config(state=NORMAL)
                self.Chatlog.insert(END, time_sent+" ", 'user_time')
                self.Chatlog.insert(END, " "+message+" ", 'user_msg')
                self.Chatlog.image_create(END, image=user_img_Chatlog)
                self.Chatlog.insert(END, "\n\n")
                self.Chatlog.config(state=DISABLED)
                self.Chatlog.yview(END)
        
        def arjunbubble(message):
            global user_input
            time_repl = int(datetime.datetime.now().hour)
            if time_repl> 12:
                time_repl = str(time_repl-12) + datetime.datetime.now().strftime(":%M") + " PM"
            elif time_repl == 12:
                time_repl = datetime.datetime.now().strftime("%H:%M") + " PM"
            else:
                time_repl = datetime.datetime.now().strftime("%H:%M") + " AM"

            def google():
                webbrowser.open('https://www.google.com/search?q='+user_input)
            if message == "Google":
                self.Chatlog.config(state=NORMAL)
                self.Chatlog.image_create(END, image=arjun_img_Chatlog)
                self.Chatlog.insert(END, " "+random.choice(EXCEPTION_ELSE)+" ", 'arjun_repl')
                self.Chatlog.insert(END, " "+time_repl+"\n", 'arjun_time')
                self.Chatlog.insert(END, "\n")
                #self.Chatlog.image_create(END, image=google_img_Chatlog)
                self.Chatlog.window_create(END, align= CENTER, window=Button(self.Chatlog, bd=0, bg="black", activebackground="black", image=google_img_Chatlog, command=google))
                self.Chatlog.insert(END, "\n\n")
                self.Chatlog.config(state=DISABLED)
                self.Chatlog.yview(END)
                self.Chatlog.update_idletasks()
                message = random.choice(EXCEPTION_ELSE)

            elif message != None:
                self.Chatlog.config(state=NORMAL)
                self.Chatlog.image_create(END, image=arjun_img_Chatlog)
                self.Chatlog.insert(END, " "+message+" ", 'arjun_repl')
                self.Chatlog.insert(END, " "+time_repl+"\n", 'arjun_time')
                self.Chatlog.insert(END, "\n")
                self.Chatlog.config(state=DISABLED)
                self.Chatlog.yview(END)
                self.Chatlog.update_idletasks()
                
            engine = pyttsx3.init()
            """RATE"""
            rate = engine.getProperty('rate')# get the details of current speaking rate
            engine.setProperty('rate', 175)# set new speech rate
            """VOLUME"""
            volume = engine.getProperty('volume')# get details of current volume
            engine.setProperty('volume', 1.0)# set new volume
            """VOICES"""
            voices = engine.getProperty('voices')# get details of current voice
            engine.setProperty('voice', voices[1].id)# set new voices
            engine.say(message)
            engine.runAndWait() 
    
#____________________________________________________________________________________________________________________________________________________________________
# OPTIONSPAGE class
class OPTIONSPAGE(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")

        def change(event):
            back.config(bg="white", fg="black")
        
        def change_back(event):
            back.config(bg="black", fg="white")

        back = Button(self, bd=0, bg="black", fg="white", activebackground="white", text="X", font=("Helvetica", 20, "bold"), command=lambda:controller.show_frame("HomePage"))
        back.place(x=20, y=30)
        back.bind("<Enter>", change)
        back.bind("<Leave>", change_back)

        def change2(event):
            Settings.config(bg="white", fg="black")
        
        def change_back2(event):
            Settings.config(bg="black", fg="white")

        Settings = Button(self, bd=0, bg="black", fg="white", activebackground="white", text="Settings", font=("Helvetica", 20, "bold"), command=lambda:controller.show_frame("Setting"))
        Settings.place(x=60, y=130)
        Settings.bind("<Enter>", change2)
        Settings.bind("<Leave>", change_back2)

        def change3(event):
            Help.config(bg="white", fg="black")
        
        def change_back3(event):
            Help.config(bg="black", fg="white")

        Help = Button(self, bd=0, bg="black", fg="white", activebackground="white", text="Help & Support", font=("Helvetica", 20, "bold"), command=lambda:controller.show_frame("Help_Support"))
        Help.place(x=60, y=180)
        Help.bind("<Enter>", change3)
        Help.bind("<Leave>", change_back3)

#____________________________________________________________________________________________________________________________________________________________________
# settings page
class Setting(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")

        Label(self, font= controller.font, text="Setting", bg="black", fg="white").pack()

        def change(event):
            back.config(bg="white", fg="black")
        
        def change_back(event):
            back.config(bg="black", fg="white")

        back = Button(self, bd=0, bg="black", fg="white", activebackground="white", text="⬅", font=("Helvetica", 15, "bold"), command=lambda:controller.show_frame("OPTIONSPAGE"))
        back.place(x=-3, y= 1)
        back.bind("<Enter>", change)
        back.bind("<Leave>", change_back)

        settings_msg = "There is nothing to change for now. Wait for next update to control arjun's behaviour."
        setting = Text(self, bd=0, bg="black", fg="white", width=35, height=38, wrap=WORD, cursor="arrow", font=("Helvetica", 15, "bold"))
        setting.tag_configure("")
        setting.place(x=1, y=90)
        setting.insert("1.0", settings_msg)
        setting.config(state=DISABLED)

#____________________________________________________________________________________________________________________________________________________________________
# help and support page
class Help_Support(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")

        Label(self, font= controller.font, text="Help & Support", bg="black", fg="white").pack()

        def change(event):
            back.config(bg="white", fg="black")
        
        def change_back(event):
            back.config(bg="black", fg="white")

        back = Button(self, bd=0, bg="black", fg="white", activebackground="white", text="⬅", font=("Helvetica", 15, "bold"), command=lambda:controller.show_frame("OPTIONSPAGE"))
        back.place(x=-3, y= 1)
        back.bind("<Enter>", change)
        back.bind("<Leave>", change_back)  

        contact_details = "For any query mail at :- shubhamtiwari06112004@gmail.com"
        contact = Text(self, bd=0, bg="black", fg="white", width=47, height=38, wrap=WORD, cursor="arrow", font=("Helvetica", 15, "bold"))
        contact.place(x=1, y=90)
        contact.insert("1.0", contact_details)
        contact.config(state=DISABLED)

#____________________________________________________________________________________________________________________________________________________________________
# lets run the app
if __name__ == "__main__":
    app = rootApp()
    app.mainloop()      
