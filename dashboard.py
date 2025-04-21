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

mid_frame1 = a.CTkFrame(win, width = 250, height = 90, fg_color="#0e716b", corner_radius= 20 )
mid_frame1.place(relx = 0.2, rely = 0.10)

mid_frame2 = a.CTkFrame(win, width = 250, height = 90, fg_color="#647687", corner_radius= 20 )
mid_frame2.place(relx = 0.48, rely = 0.10)

mid_frame3 = a.CTkFrame(win, width = 250, height = 90, fg_color="#820025", corner_radius= 20 )
mid_frame3.place(relx = 0.76, rely = 0.10)

mid_frame4 = a.CTkFrame(win, width = 680, height = 230, corner_radius = 0, border_color= "black")
mid_frame4.place(relx = 0.2, rely = 0.26)

mid_frame5 = a.CTkFrame(win, width = 255, height = 230, corner_radius = 0, border_color= "black")
mid_frame5.place(relx = 0.76, rely = 0.26)

mid_frame6 = a.CTkFrame(win, width = 680, height = 180, corner_radius = 0, border_color= "black")
mid_frame6.place(relx = 0.2, rely = 0.58)

mid_frame7 = a.CTkFrame(win, width = 680, height = 180, corner_radius = 0, border_color= "black")
mid_frame7.place(relx = 0.2, rely = 0.58)

mid_frame7 = a.CTkFrame(win, width = 255, height = 180, corner_radius = 0, border_color= "black")
mid_frame7.place(relx = 0.76, rely = 0.58)

ms_frame1 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame1.place(relx = 0.136, rely = 0.1)

ms_frame2 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame2.place(relx = 0.136, rely = 0.2)

ms_frame3 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame3.place(relx = 0.136, rely = 0.3)

ms_frame4 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame4.place(relx = 0.136, rely = 0.4)

ms_frame5 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame5.place(relx = 0.136, rely = 0.5)

ms_frame6 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame6.place(relx = 0.136, rely = 0.6)




win.mainloop()