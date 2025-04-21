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

mid_frame = a.CTkFrame(win, width = 320, height= 500, fg_color= "#0e716b", corner_radius=50)
mid_frame.place(relx = 0.73, rely = 0.13)

bb_frame1 = a.CTkFrame(mid_frame, width = 235, height= 34, fg_color= "white", corner_radius=30)
bb_frame1.place(relx = 0.14, rely = 0.35)

bb_frame2 = a.CTkFrame(mid_frame, width = 235, height= 34, fg_color= "white", corner_radius=30)
bb_frame2.place(relx = 0.14, rely = 0.49)

bb_frame3 = a.CTkFrame(mid_frame, width = 235, height= 34, fg_color= "#36000C", corner_radius=30)
bb_frame3.place(relx = 0.14, rely = 0.62)

win.mainloop()