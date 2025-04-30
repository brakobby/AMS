import customtkinter as ctk
win = ctk.CTk()
win.title("AMS")
win.geometry("1300x760")
win.resizable(0,0)
win._set_appearance_mode("light")



sidenav = ctk.CTkFrame(win, fg_color="#0e716b", height=760, width=220, corner_radius=0)
sidenav.place(relx=0, rely=0)

topnav = ctk.CTkFrame(win, fg_color="#A20025", height=50, width=1300, corner_radius=0)
topnav.place(relx=0, rely=0)

date = ctk.CTkLabel(topnav, text="DECEMBER 25, 2025")
date.place(relx=0.43, rely=0.15)

bottomnav = ctk.CTkFrame(win, fg_color="#A20025", height=50, width=1300, corner_radius=0)
bottomnav.place(relx=0, rely=0.934)

fstudents = ctk.CTkFrame(win, width=250, height=100, fg_color="#0F8A7B")
fstudents.place(relx=0.20, rely=0.12)

mstudents = ctk.CTkFrame(win, width=250, height=100, fg_color="#647687")
mstudents.place(relx=0.45, rely=0.12)

students3 = ctk.CTkFrame(win, width=250, height=100, fg_color="#A20025")
students3.place(relx=0.70, rely=0.12)

button1 = ctk.CTkButton(sidenav, height=30, width=180, fg_color="white", border_color="black", text="DASHBOARD", text_color="black", border_width=2)
button1.place(relx=0.1, rely=0.15)

button2 = ctk.CTkButton(sidenav, height=30, width=180, fg_color="white", border_color="black", text="REGISTRATION", text_color="black", border_width=2)
button2.place(relx=0.1, rely=0.25)

button3 = ctk.CTkButton(sidenav, height=30, width=180, fg_color="white", border_color="black", text="DATA HOUSE", text_color="black", border_width=2)
button3.place(relx=0.1, rely=0.35)

button4 = ctk.CTkButton(sidenav, height=30, width=180, fg_color="white", border_color="black", text="ACADEMICS", text_color="black", border_width=2)
button4.place(relx=0.1, rely=0.45)

button5 = ctk.CTkButton(sidenav, height=30, width=180, fg_color="white", border_color="black", text="PROPERTIES", text_color="black", border_width=2)
button5.place(relx=0.1, rely=0.55)

button6 = ctk.CTkButton(sidenav, height=30, width=180, fg_color="white", border_color="black", text="SETTINGS", text_color="black", border_width=2)
button6.place(relx=0.1, rely=0.65)

gr1 = ctk.CTkFrame(win, height=250, width=650, fg_color="grey")
gr1.place(relx=0.20, rely=0.3)

gr2 = ctk.CTkFrame(win, height=200, width=650, fg_color="grey")
gr2.place(relx=0.20, rely=0.65)

gr3 = ctk.CTkFrame(win, height=250, width=250, fg_color="grey")
gr3.place(relx=0.715, rely=0.3)

gr4 = ctk.CTkFrame(win, height=200, width=250, fg_color="grey")
gr4.place(relx=0.715, rely=0.65)


win.mainloop()