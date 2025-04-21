import customtkinter as a
from PIL import Image,ImageTk

win = a.CTk()
win.title("Agape Academy International(AAI)")
win.geometry("1290x760")
win.resizable(0,0)
img = Image.open("images.jpeg")
img = img.resize((60,60))
photo = ImageTk.PhotoImage(img)

dash_frame = a.CTkFrame(win, height = 55, width=1290, fg_color= "#820025", corner_radius=0)
dash_frame.place(relx = 0, rely = 0)

dash_frame2 = a.CTkFrame(win, width =1090, height= 55, corner_radius = 0, fg_color = "#014342")
dash_frame2.place(relx = 0.155, rely = 0.072)

dash2_1 = a.CTkFrame(dash_frame2, width = 255, height= 30, fg_color= "white", corner_radius = 4 )
dash2_1.place(relx = 0.05, rely = 0.2)

pic = a.CTkLabel(dash_frame2, image = photo, text = "")
pic.place(relx = 0.3, rely = 0.2)

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