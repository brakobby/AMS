import customtkinter as c

class AgapeSystem:
    def __init__(self, ui):
        self.ui = ui
        self.ui.title("Agape School Management System")
        self.ui.geometry("1300x760+0+0")
        c.set_appearance_mode("light")

        # Make window resizable
        self.ui.rowconfigure(0, weight=1)
        self.ui.columnconfigure(0, weight=1)

        self.content()

    def content(self):
        self.parent_widget = c.CTkFrame(self.ui)
        self.parent_widget.grid(row=0, column=0, sticky="nsew")  # Expand to fill

        # Make frame content responsive (optional)
        self.parent_widget.rowconfigure(0, weight=0)
        self.parent_widget.rowconfigure(1,weight=20)
        self.parent_widget.columnconfigure(0, weight=1)
        self.parent_widget.columnconfigure(1,weight=30)

        self.top_navigation = c.CTkFrame(self.parent_widget,height = 60,corner_radius=0,fg_color="#011c40")
        self.top_navigation.grid(row =0, column = 0,sticky = "nwe",columnspan = 2)

        self.side_navigation = c.CTkFrame(self.parent_widget,corner_radius=0,fg_color="#023859")
        self.side_navigation.grid(row =1,column =0,sticky = "nsew")

        self.dash_container = c.CTkFrame(self.parent_widget)
        self.dash_container.grid(row = 1,column = 1,sticky = "nsew")
        self.dash_container.rowconfigure(0, weight=1)
        self.dash_container.rowconfigure((1, 2), weight=2)
        self.dash_container.columnconfigure((0,1,2), weight = 1)


        #Cards
        self.card1 = c.CTkFrame(self.dash_container,height = 120,fg_color="#26658C")
        self.card1.grid(row = 0, column = 0, sticky = "nwe",padx = 10,pady =15,ipadx = 70)

        self.card2 = c.CTkFrame(self.dash_container, height=120,fg_color = "#54ACBF")
        self.card2.grid(row=0, column=1, sticky="nwe", padx=10, pady=15, ipadx=70)

        self.card3 = c.CTkFrame(self.dash_container, height=120,fg_color = "#7691AD")
        self.card3.grid(row=0, column=2, sticky="nwe", padx=10, pady=15, ipadx=70)

        self.graph_card1 = c.CTkFrame(self.dash_container,fg_color="#EFEACD")
        self.graph_card1.grid(row = 1, column = 0,sticky = "nsew",padx = 10, pady = 15, ipadx = 70,columnspan =2 )

        self.graph_card2 = c.CTkFrame(self.dash_container,fg_color="#FFFFFF")
        self.graph_card2.grid(row=1, column=2, sticky="nsew", padx=10, pady=15, ipadx=70, columnspan=2)

        self.graph_card3 = c.CTkFrame(self.dash_container,fg_color="#FFFFFF")
        self.graph_card3.grid(row=2, column=0, sticky="nsew", padx=10, pady=15, ipadx=70, columnspan=3)

        #Content for top Navigation


        #Contents of the SideNavigation Bar
        self.dashboard_btn = c.CTkButton(self.side_navigation, text="Dashboard",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.dashboard_btn.pack(pady=20, padx=10, fill="x")
        self.dashboard_btn.configure(command = self.dashboard)

        self.student_btn = c.CTkButton(self.side_navigation, text="Students",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.student_btn.pack(pady=20, padx=10, fill="x")
        self.student_btn.configure(command = self.Student)

        self.teacher_btn = c.CTkButton(self.side_navigation, text="Teachers",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.teacher_btn.pack(pady=20, padx=10, fill="x")
        self.teacher_btn.configure(command=self.teacher)

        self.class_btn = c.CTkButton(self.side_navigation, text="Classes",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.class_btn.pack(pady=20, padx=10, fill="x")

        self.attendance_btn = c.CTkButton(self.side_navigation, text="Attendance",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.attendance_btn.pack(pady=20, padx=10, fill="x")
        self.attendance_btn.configure(command = self.attendance)

        self.payment_btn = c.CTkButton(self.side_navigation, text="Payments",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.payment_btn.pack(pady=20, padx=10, fill="x")

        self.report_btn = c.CTkButton(self.side_navigation, text="Reports",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.report_btn.pack(pady=20, padx=10, fill="x")

        self.setting_btn = c.CTkButton(self.side_navigation, text="Settings",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.setting_btn.pack(pady=20, padx=10, fill="x")

        self.logout_btn = c.CTkButton(self.side_navigation, text="Logout", fg_color="#3c507d",
                                        hover_color="#00766D", font=("Montserrat Alternates", 16, "bold"))
        self.logout_btn.pack(pady=20, padx=10, fill="x")
    def dashboard(self):
        try:
            self.ams_parent_container.destroy()
        except AttributeError:
            pass

    def Student(self):
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)

        self.ams_student_container = c.CTkFrame(self.ams_parent_container, fg_color="#F5F5F5")
        self.ams_student_container.grid(row=0, column=0, sticky="nsew",columnspan = 3,rowspan =3)
        self.ams_student_container.rowconfigure(0,weight=1)
        self.ams_student_container.rowconfigure(1, weight=1)
        self.ams_student_container.rowconfigure(2, weight=2)
        self.ams_student_container.rowconfigure(3, weight=1)
        self.ams_student_container.rowconfigure(3, weight=2)
        self.ams_student_container.columnconfigure((0,2),weight = 1)
        self.ams_student_container.columnconfigure(1, weight=1)

        self.searchframe = c.CTkFrame(self.ams_student_container,height = 60,corner_radius=0,fg_color="#F5F5F5")
        self.searchframe.grid(row = 0, column=0,sticky = "new",padx = 50,columnspan =3,pady = 10)
        self.searchframe.columnconfigure(0,weight=2)
        self.searchframe.columnconfigure(1, weight=1)
        self.searchframe.columnconfigure(2,weight =1)

        self.search_bar = c.CTkEntry(self.searchframe,placeholder_text="Search", font = ("Montserrat Alternates",16),fg_color="#F5F5F5")
        self.search_bar.grid(row =0, column = 0,padx=50,sticky = "sew",pady = 20,columnspan =1,ipadx =10)
        self.addbtn = c.CTkButton(self.searchframe, text="Search", font=("Montserrat Alternates", 16))
        self.addbtn.grid(row=0, column=1, sticky="w", padx=0)


        self.ams_table_frame = c.CTkFrame(self.ams_student_container,fg_color="white",border_color="black",border_width=1,height =500)
        self.ams_table_frame.grid(row = 1, column = 0,sticky="nsew",rowspan =2,columnspan=3,ipadx =100,padx = 50,pady =0)

        self.addbtn = c.CTkButton(self.ams_student_container,text = "ADD STUDENT",font = ("Montserrat Alternates",16))
        self.addbtn.grid(row = 3,column =0,sticky = "ew",padx = 50)
        self.addbtn = c.CTkButton(self.ams_student_container, text="UPDATE RECORD",font = ("Montserrat Alternates",16))
        self.addbtn.grid(row=3, column=1,sticky = "ew",padx = 50)
        self.removebtn = c.CTkButton(self.ams_student_container, text="REMOVE STUDENT",font = ("Montserrat Alternates",16))
        self.removebtn.grid(row=3, column=2,sticky = "ew",padx = 50)
        self.removebtn.configure(fg_color="red")


    def teacher(self):
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)

    def attendance(self):
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)


if __name__ == '__main__':
    systemWindow = c.CTk()
    classObject = AgapeSystem(systemWindow)
    systemWindow.mainloop()
