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

dash_entry = a.CTkEntry(dash_frame2, height=30, width = 270)
dash_entry.place(relx= 0.05, rely = 0.2)

dash_btn1 = a.CTkButton(dash_frame2, height=30, width =170, fg_color= "white",text = "SORT BY", font = ("Monserrat",15,"bold"), text_color="black" )
dash_btn1.place(relx = 0.5, rely = 0.2)

dash_btn2 = a.CTkButton(dash_frame2, height=30, width =135, fg_color= "white", text = "DELETE", font = ("Monserrat",15,"bold"), text_color="black")
dash_btn2.place(relx = 0.71, rely = 0.2)

dash_btn3 = a.CTkButton(dash_frame2, height=30, width =135, fg_color= "white", text = "CLOSE", font = ("Monserrat",15,"bold"), text_color="black")
dash_btn3.place(relx = 0.85, rely = 0.2)

center_frame = a.CTkFrame(win, width = 850, height=450, corner_radius=0, fg_color="white")
center_frame.place(relx= 0.247, rely = 0.19)

ctr_frame_fr = a.CTkFrame(center_frame, width=850, height = 40, fg_color= "#710C04", corner_radius=0 )
ctr_frame_fr.place(relx =0, rely = 0 )

ctr_frame_lbl1 = a.CTkLabel(ctr_frame_fr, text = "STUDENT ID", font = ("Monserrat", 12), text_color="white")
ctr_frame_lbl1.place(relx = 0.045, rely = 0.15)

ctr_frame_lbl2 = a.CTkLabel(ctr_frame_fr, text = "FULL NAME", font = ("Monserrat", 12), text_color="white")
ctr_frame_lbl2.place(relx = 0.215, rely = 0.15)

ctr_frame_lbl3 = a.CTkLabel(ctr_frame_fr, text = "DATE OF BIRTH", font = ("Monserrat", 12), text_color="white")
ctr_frame_lbl3.place(relx = 0.395, rely = 0.15)

ctr_frame_lbl4 = a.CTkLabel(ctr_frame_fr, text = "GRADE", font = ("Monserrat", 12), text_color="white")
ctr_frame_lbl4.place(relx = 0.595, rely = 0.15)

ctr_frame_lbl5 = a.CTkLabel(ctr_frame_fr, text = "PARENT", font = ("Monserrat", 12), text_color="white")
ctr_frame_lbl5.place(relx = 0.745, rely = 0.15)

ctr_frame_lbl6 = a.CTkLabel(ctr_frame_fr, text = "CONTACTS", font = ("Monserrat", 12), text_color="white")
ctr_frame_lbl6.place(relx = 0.885, rely = 0.15)


win.mainloop()