import customtkinter as a

win = a.CTk()
win.title("Agape Academy International(AAI)")
win.geometry("1290x760")
win.resizable(0,0)

dash_frame = a.CTkFrame(win, height = 55, width=1290, fg_color= "#820025", corner_radius=0)
dash_frame.place(relx = 0, rely = 0)

dash_pic = a.CTkFrame(dash_frame, width=40, height= 40, fg_color="white", corner_radius= 600)
dash_pic.place(relx = 0.96, rely = 0.15)

btm_frame = a.CTkFrame(win, height = 55, width=1290, fg_color= "#820025",corner_radius=0)
btm_frame.place(relx = 0, rely = 0.836)

dash_title = a.CTkLabel(win, text = "Agape Management System", text_color = "white", font = ("Monserrat", 20), fg_color= "#820025", corner_radius=0)
dash_title.place(relx = .05, rely = 0.020)

dash_title2 = a.CTkLabel(win, text = "December 25, 2025", text_color = "white", font = ("Monserrat", 15), fg_color= "#820025", corner_radius=0)
dash_title2.place(relx = .5, rely = 0.020)

side_frame = a.CTkFrame(win, height = 581, width = 200, fg_color= "#0e716b", corner_radius = 0)
side_frame.place(relx = 0, rely = 0.0716)

ms_frame1 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame1.place(relx = 0.136, rely = 0.1)

msf1_label = a.CTkLabel(ms_frame1, text = "DASHBOARD", font = ("Monserrat", 12, "bold"))
msf1_label.place(relx= 0.21, rely = 0.01)

ms_frame2 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame2.place(relx = 0.136, rely = 0.2)

msf2_label = a.CTkLabel(ms_frame2, text = "REGISTRATION", font = ("Monserrat", 12, "bold"))
msf2_label.place(relx= 0.16, rely = 0.01)

ms_frame3 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame3.place(relx = 0.136, rely = 0.3)

msf3_label = a.CTkLabel(ms_frame3, text = "DATA HOUSE", font = ("Monserrat", 12, "bold"))
msf3_label.place(relx= 0.2, rely = 0.01)

ms_frame4 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame4.place(relx = 0.136, rely = 0.4)

msf4_label = a.CTkLabel(ms_frame4, text = "ACADEMICS", font = ("Monserrat", 12, "bold"))
msf4_label.place(relx= 0.23, rely = 0.01)

ms_frame5 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame5.place(relx = 0.136, rely = 0.5)

msf5_label = a.CTkLabel(ms_frame5, text = "PROPERTIES", font = ("Monserrat", 12, "bold"))
msf5_label.place(relx= 0.22, rely = 0.01)

ms_frame6 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame6.place(relx = 0.136, rely = 0.6)

msf6_label = a.CTkLabel(ms_frame6, text = "SETTING", font = ("Monserrat", 12, "bold"))
msf6_label.place(relx= 0.28, rely = 0.01)

dash_frame2 = a.CTkFrame(win, width =1090, height= 55, corner_radius = 0, fg_color = "#014342")
dash_frame2.place(relx = 0.155, rely = 0.072)

btm_frame2 = a.CTkFrame(win, width = 930, height = 55, fg_color = "#014342", corner_radius = 0  )
btm_frame2.place(relx = 0.2, rely = 0.74)

pic_frame = a.CTkFrame(win,corner_radius=20, width = 130, height= 150, fg_color= "white" )
pic_frame.place(relx = 0.515, rely= 0.17)

f_entry1 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white", placeholder_text = "Grade", font = ("Monserrat", 12, "bold"))
f_entry1.place(relx = 0.2, rely = 0.65)

f_entry2 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white",placeholder_text = "Date Of Birth", font = ("Monserrat", 12, "bold"))
f_entry2.place(relx = 0.2, rely = 0.57)

f_entry3 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white",placeholder_text = "Full Name", font = ("Monserrat", 12, "bold") )
f_entry3.place(relx = 0.2, rely = 0.49)

f_entry4 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white", placeholder_text = "Student ID", font = ("Monserrat", 12, "bold"))
f_entry4.place(relx = 0.2, rely = 0.41)

f_entry5 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white", placeholder_text = "Allergy", font = ("Monserrat", 12, "bold"))
f_entry5.place(relx = 0.58, rely = 0.65)

f_entry6 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white", placeholder_text = "Emergency Contact", font = ("Monserrat", 12, "bold"))
f_entry6.place(relx = 0.58, rely = 0.57)

f_entry7 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white", placeholder_text = "Contact", font = ("Monserrat", 12, "bold"))
f_entry7.place(relx = 0.58, rely = 0.49)

f_entry8 = a.CTkEntry(win, corner_radius=4, width = 440, height= 30, fg_color="white", placeholder_text = "Parent", font = ("Monserrat", 12, "bold"))
f_entry8.place(relx = 0.58, rely = 0.41)

mb_btn1 = a.CTkButton(btm_frame2, corner_radius=6, width = 170, height= 40, fg_color= "#647687", text = "SUBMIT", font = ("Monserrat", 12, "bold"), text_color="white")
mb_btn1.place(relx = 0.1, rely = 0.15)

mb_btn2 = a.CTkButton(btm_frame2, corner_radius=6, width = 170, height= 40, fg_color= "#820025",text = "RESET", font = ("Monserrat", 12, "bold"), text_color="white")
mb_btn2.place(relx = 0.4, rely = 0.15)

mb_btn3 = a.CTkButton(btm_frame2, corner_radius=6, width = 170, height= 40, fg_color= "#0e716b", text = "UPLOAD PHOTO", font = ("Monserrat", 12, "bold"), text_color="white" )
mb_btn3.place(relx = 0.7, rely = 0.15)


win.mainloop()