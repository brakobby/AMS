import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import customtkinter as c
from tkinter import filedialog
from PIL import Image
import os
import shutil
from databaseCode import create_students_table, insert_student


class AgapeSystem:
    def __init__(self, ui):
        self.ui = ui
        self.ui.title("Agape School Management System")
        self.ui.geometry("1300x760+0+0")
        c.set_appearance_mode("light")

        # Make window resizable
        self.ui.rowconfigure(0, weight=1)
        self.ui.columnconfigure(0, weight=1)
        create_students_table()

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

        # self.teacher_btn = c.CTkButton(self.side_navigation, text="Teachers",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        # self.teacher_btn.pack(pady=20, padx=10, fill="x")
        # self.teacher_btn.configure("command=self.teacher")

        # self.class_btn = c.CTkButton(self.side_navigation, text="Classes",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        # self.class_btn.pack(pady=20, padx=10, fill="x")

        # self.attendance_btn = c.CTkButton(self.side_navigation, text="Attendance",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        # self.attendance_btn.pack(pady=20, padx=10, fill="x")
        # self.attendance_btn.configure(command = self.attendance)

        self.payment_btn = c.CTkButton(self.side_navigation, text="Payments",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.payment_btn.pack(pady=20, padx=10, fill="x")

        self.report_btn = c.CTkButton(self.side_navigation, text="Reports",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.report_btn.pack(pady=20, padx=10, fill="x")
        self.report_btn.configure(command =self.report_popup)

        self.setting_btn = c.CTkButton(self.side_navigation, text="Settings",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.setting_btn.pack(pady=20, padx=10, fill="x")

        self.logout_btn = c.CTkButton(self.side_navigation, text="Logout", fg_color="#3c507d",
                                        hover_color="#00766D", font=("Montserrat Alternates", 16, "bold"))
        self.logout_btn.pack(pady=20, padx=10, fill="x")

    def dashboard(self):
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

        self.search_bar = c.CTkEntry(self.searchframe,placeholder_text="Search", font = ("Montserrat Alternates",16),fg_color="#F5F5F5")
        self.search_bar.grid(row = 0, column = 0, padx = 0, pady =2,sticky = "nsew")
        self.search_bar.configure(width=400)
        self.addbtn = c.CTkButton(self.searchframe, text="Search", font=("Montserrat Alternates", 16),fg_color="#3c507d")
        self.addbtn.grid(row = 0, column =1,padx =20, sticky = "ew")
        # sort by widget
        self.sortoption = c.CTkOptionMenu(self.searchframe,values=["Grade","Age","Sex"])
        self.sortoption.grid(row = 0, column =3, padx = 20,sticky="ew")
        self.sortoption.configure(font=("Montserrat Alternates", 16),fg_color = "#3c507d")

        self.ams_table_frame = c.CTkFrame(self.ams_student_container,fg_color="white",border_color="black",border_width=1,height =400)
        self.ams_table_frame.grid(row = 1, column = 0,sticky="nsew",rowspan =2,columnspan=3,ipadx =100,padx = 50,pady =0)
        self.columns = ("ID", "Name", "Sex", "Parent", "Occupation", "Phone", "Grade")
        self.tree = ttk.Treeview(self.ams_table_frame, columns=self.columns, show="headings", height=17)
        
        # Style the Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#f0f0f0",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#FFFFFF",
                        font=("Montserrat Alternates", 12))
        style.configure("Treeview.Heading", font=("Montserrat Alternates", 14, "bold"))

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.pack(padx = 0,pady=0,fill="x")

        self.addbtn = c.CTkButton(self.ams_student_container,text = "ADD STUDENT",font = ("Montserrat Alternates",16),fg_color="#3c507d")
        self.addbtn.grid(row = 3,column =0,sticky = "ew",padx = 50)
        self.addbtn.configure(command = self.addStudent)
        self.updatebtn = c.CTkButton(self.ams_student_container, text="UPDATE RECORD",font = ("Montserrat Alternates",16),fg_color = "#3c507d")
        self.updatebtn.grid(row=3, column=1,sticky = "ew",padx = 30)
        self.updatebtn.configure(command = self.updateStudent)
        self.removebtn = c.CTkButton(self.ams_student_container, text="REMOVE STUDENT",font = ("Montserrat Alternates",16))
        self.removebtn.grid(row=3, column=2,sticky = "ew",padx = 60)
        self.removebtn.configure(fg_color="red")


    def addStudent(self):
        self.ams_add_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_add_container.grid(row=1, column=1, sticky="nsew")
        self.ams_add_container.rowconfigure(0, weight=1)
        self.ams_add_container.rowconfigure((1, 2), weight=2)
        self.ams_add_container.columnconfigure((0, 1, 2), weight=1)
        self.photoFrame = c.CTkFrame(self.ams_add_container,width=200,height=200,border_color="#3c507d")
        self.photoFrame.pack(padx = 20, pady = 10)
        self.uploadphoto = c.CTkButton(self.ams_add_container, text = "Upload",font = ("Montserrat Alternates",16),width=200,fg_color = "#3c507d")
        self.uploadphoto.pack(padx = 20, pady = 10)
        self.uploadphoto.configure(command = self.upload_passport)
        self.image_label = c.CTkLabel(self.photoFrame, text="",width=180,height=180)
        self.image_label.pack(padx=10, pady=10)
        
        # Entry Widgets
        self.idEntry =  c.CTkEntry(self.ams_add_container,placeholder_text="Student ID",font = ("Montserrat Alternates",16),width=600)
        self.idEntry.pack(padx = 0, pady=10)
        self.nameEntry =  c.CTkEntry(self.ams_add_container,placeholder_text="Full Name",font = ("Montserrat Alternates",16),width=600)
        self.nameEntry.pack(padx = 0, pady=10)
        self.sexEntry =  c.CTkOptionMenu(self.ams_add_container,values=["Sex","Male","Female"],font = ("Montserrat Alternates",16),width=600)
        self.sexEntry.pack(padx = 0, pady=10)
        self.parentEntry =  c.CTkEntry(self.ams_add_container,placeholder_text="Parent/Guardian",font = ("Montserrat Alternates",16),width=600)
        self.parentEntry.pack(padx = 0, pady=10)
        self.occupationEntry =  c.CTkEntry(self.ams_add_container,placeholder_text="Occupation",font = ("Montserrat Alternates",16),width=600)
        self.occupationEntry.pack(padx = 0, pady=10)
        self.phoneEntry =  c.CTkEntry(self.ams_add_container,placeholder_text="Phone Number",font = ("Montserrat Alternates",16),width=600)
        self.phoneEntry.pack(padx = 0, pady=10)
        self.gradeEntry =  c.CTkEntry(self.ams_add_container,placeholder_text="Grade",font = ("Montserrat Alternates",16),width=600)
        self.gradeEntry.pack(padx = 0, pady=10)
        self.submit = c.CTkButton(self.ams_add_container, text = "SAVE",font = ("Montserrat Alternates",16),width = 600)
        self.submit.pack(padx =0, pady =10)
        self.submit.configure(command = self.save_student_data)
        self.cancel = c.CTkButton(self.ams_add_container, text = "CLOSE",font = ("Montserrat Alternates",16),width = 600)
        self.cancel.pack(padx =0, pady =5)
        self.cancel.configure(command = lambda : self.ams_add_container.destroy())
    


    def upload_passport(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if file_path:
            # Create a local "images" folder if it doesn't exist
            if not os.path.exists("images"):
                os.makedirs("images")

            # Get filename and destination
            filename = os.path.basename(file_path)
            destination_path = os.path.join("images", filename)

            # Copy the file to local images folder
            shutil.copy(file_path, destination_path)

            # Store this path to be saved into the database later
            self.saved_photo_path = destination_path

            # Display the image
            image = Image.open(destination_path)
            image = image.resize((180, 180))
            self.photo = c.CTkImage(light_image=image, dark_image=image, size=(180, 180))
            self.image_label.configure(image=self.photo, text="")


    def save_student_data(self):
    # adjust to your import

        student_id = self.idEntry.get()
        full_name = self.nameEntry.get()
        sex = self.sexEntry.get()
        parent_name = self.parentEntry.get()
        occupation = self.occupationEntry.get()
        phone = self.phoneEntry.get()
        grade = self.gradeEntry.get()
        photo_path = getattr(self, "saved_photo_path", None)  # default to None

        try:
            insert_student(
                student_id, full_name, sex, parent_name,
                occupation, phone, grade, photo_path
            )
            c.CTkMessagebox(title="Success", message="Student record saved!", icon="check")
            self.ams_add_container.destroy()
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e), icon="error")



    def updateStudent(self):
        self.ams_update_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_update_container.grid(row=1, column=1, sticky="nsew")
        self.ams_update_container.rowconfigure(0, weight=1)
        self.ams_update_container.rowconfigure((1, 2), weight=2)
        self.ams_update_container.columnconfigure((0, 1, 2), weight=1)
        self.photoFrame = c.CTkFrame(self.ams_update_container,width=200,height=200,border_color="#3c507d")
        self.photoFrame.pack(padx = 20, pady = 10)
        self.uploadphoto = c.CTkButton(self.ams_update_container, text = "Upload",font = ("Montserrat Alternates",16),width=200,fg_color = "#3c507d")
        self.uploadphoto.pack(padx = 20, pady = 10)
        # Entry Widgets
        self.idEntry =  c.CTkEntry(self.ams_update_container,placeholder_text="Student ID",font = ("Montserrat Alternates",16),width=600)
        self.idEntry.pack(padx = 0, pady=10)
        self.nameEntry =  c.CTkEntry(self.ams_update_container,placeholder_text="Full Name",font = ("Montserrat Alternates",16),width=600)
        self.nameEntry.pack(padx = 0, pady=10)
        self.sexEntry =  c.CTkOptionMenu(self.ams_update_container,values=["Sex","Male","Female"],font = ("Montserrat Alternates",16),width=600)
        self.sexEntry.pack(padx = 0, pady=10)
        self.parentEntry =  c.CTkEntry(self.ams_update_container,placeholder_text="Parent/Guardian",font = ("Montserrat Alternates",16),width=600)
        self.parentEntry.pack(padx = 0, pady=10)
        self.occupationEntry =  c.CTkEntry(self.ams_update_container,placeholder_text="Occupation",font = ("Montserrat Alternates",16),width=600)
        self.occupationEntry.pack(padx = 0, pady=10)
        self.phoneEntry =  c.CTkEntry(self.ams_update_container,placeholder_text="Phone Number",font = ("Montserrat Alternates",16),width=600)
        self.phoneEntry.pack(padx = 0, pady=10)
        self.gradeEntry =  c.CTkEntry(self.ams_update_container,placeholder_text="Grade",font = ("Montserrat Alternates",16),width=600)
        self.gradeEntry.pack(padx = 0, pady=10)
        self.submit = c.CTkButton(self.ams_update_container, text = "UPDATE",font = ("Montserrat Alternates",16),width = 600)
        self.submit.pack(padx =0, pady =10)
        self.cancel = c.CTkButton(self.ams_update_container, text = "CLOSE",font = ("Montserrat Alternates",16),width = 600)
        self.cancel.pack(padx =0, pady =5)
        self.cancel.configure(command = lambda : self.ams_update_container.destroy())


    def attendance(self):
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)

    def report_popup(self):
        self.pop_window = c.CTkToplevel(self.ui)
        self.pop_window.geometry("500x200")
        self.pop_window.transient(self.ui)
        self.pop_window.update_idletasks()
        self.pop_window.grab_set()
        self.pop_window.title("Report")

    # Get main window position and size
        main_x = self.ui.winfo_x()
        main_y = self.ui.winfo_y()
        main_width = self.ui.winfo_width()
        main_height = self.ui.winfo_height()

        # Get popup size
        popup_width = self.pop_window.winfo_width()
        popup_height = self.pop_window.winfo_height()

        # Calculate position to center
        x = main_x + (main_width // 2) - (popup_width // 2)
        y = main_y + (main_height // 2) - (popup_height // 2)

        self.pop_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        self.pop_window.focus()
        
        # contents
        grades = ["Grade"] + [f"Grade {i}" for i in range(1, 13)]
        self.gradeAccess = c.CTkOptionMenu(self.pop_window, values=grades,width=300,font = ("Montserrat Alternates",16),fg_color="#7691AD")
        self.gradeAccess.pack(padx = 10, pady = 10)
        self.subject = c.CTkOptionMenu(self.pop_window, values=["Mathematics", "Science","Pre Algebra", "Bible"],width=300,font = ("Montserrat Alternates",16),fg_color="#7691AD")
        self.subject.pack(padx =10,pady =20)
        self.subbtn = c.CTkButton(self.pop_window, text="Submit",width=300,font = ("Montserrat Alternates",16),fg_color="#3c507d")
        self.subbtn.pack(padx =10,pady =5)
        self.subbtn.configure(command =self.Report)

    def Report(self):
        self.pop_window.destroy()
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)


        



if __name__ == '__main__':
    systemWindow = c.CTk()
    classObject = AgapeSystem(systemWindow)
    systemWindow.mainloop()
