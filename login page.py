import customtkinter as a
from PIL import Image,ImageTk

win = a.CTk()
win.title("Agape Academy International(AAI)")
win.geometry("1290x760")
win.resizable(0,0)
img = Image.open("5aab5af2-90e2-4fb9-9114-d0402646f4e0.png")
img = img.resize((1500,1000))
photo = ImageTk.PhotoImage(img)

dash_frame = a.CTkFrame(win, height = 55, width=1290, fg_color= "#820025", corner_radius=0)
dash_frame.place(relx = 0, rely = 0)

dash_picframe = a.CTkFrame(dash_frame, width=40, height= 40, fg_color="white", corner_radius= 600)
dash_picframe.place(relx = 0.96, rely = 0.15)

main_pic = a.CTkLabel(win, image = photo, text = "")
main_pic.place(relx = 0,rely =0.07)

main_frame = a.CTkFrame(win, width = 350, height = 740, fg_color= "#016c60", corner_radius=0)
main_frame.place(relx = 0.75, rely = 0.07)

btm_frame = a.CTkFrame(win, height = 55, width=1290, fg_color= "#820025",corner_radius=0)
btm_frame.place(relx = 0, rely = 0.836)

dash_title = a.CTkLabel(win, text = "Agape Management System", text_color = "white", font = ("Monserrat", 20), fg_color= "#820025", corner_radius=0)
dash_title.place(relx = .05, rely = 0.020)

dash_title2 = a.CTkLabel(win, text = "December 25, 2025", text_color = "white", font = ("Monserrat", 15), fg_color= "#820025", corner_radius=0)
dash_title2.place(relx = .5, rely = 0.020)

mid_frame = a.CTkFrame(win, width = 320, height= 500, fg_color= "#0e716b", bg_color= "#016c60", corner_radius=50 )
mid_frame.place(relx = 0.73, rely = 0.13)

bb_entry1 = a.CTkEntry(mid_frame, width = 235, height= 34, corner_radius=30, border_color="#710C04", placeholder_text="School ID",font = ("Monserrat", 15))
bb_entry1.place(relx = 0.14, rely = 0.35)

bb_entry2 = a.CTkEntry(mid_frame, width = 235, height= 34, corner_radius=30, border_color="#710C04", placeholder_text= "Password",font = ("Monserrat", 15))
bb_entry2.place(relx = 0.14, rely = 0.49)

bb_button3 = a.CTkButton(mid_frame, width = 235, height= 34, fg_color= "#710C04", corner_radius=30,text = "LOGIN", font = ("Monserrat", 15, "bold"))
bb_button3.place(relx = 0.14, rely = 0.62)


win.mainloop()