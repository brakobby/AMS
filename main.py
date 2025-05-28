import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import customtkinter as c
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import sqlite3
import shutil
from databaseCode import create_students_table, insert_student,student_exists,get_all_students
from collections import defaultdict

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

        self.payment_btn = c.CTkButton(self.side_navigation, text="Payments",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.payment_btn.pack(pady=20, padx=10, fill="x")

        self.report_btn = c.CTkButton(self.side_navigation, text="Reports",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.report_btn.pack(pady=20, padx=10, fill="x")
        self.report_btn.configure(command =self.report_popup)

        self.setting_btn = c.CTkButton(self.side_navigation, text="Settings",fg_color="#3c507d",hover_color="#00766D",font = ("Montserrat Alternates",16,"bold"))
        self.setting_btn.pack(pady=20, padx=10, fill="x")
        self.setting_btn.configure(command = self.show_report_card)

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
        self.search_bar.grid(row = 0, column = 0, padx = 0, pady=2,sticky = "nsew")
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
        self.load_students()

        self.addbtn = c.CTkButton(self.ams_student_container,text = "ADD STUDENT",font = ("Montserrat Alternates",16),fg_color="#3c507d")
        self.addbtn.grid(row = 3,column =0,sticky = "ew",padx = 50)
        self.addbtn.configure(command = self.addStudent)
        self.updatebtn = c.CTkButton(self.ams_student_container, text="UPDATE RECORD",font = ("Montserrat Alternates",16),fg_color = "#3c507d")
        self.updatebtn.grid(row=3, column=1,sticky = "ew",padx = 30)
        self.updatebtn.configure(command = self.updateStudent)
        self.removebtn = c.CTkButton(self.ams_student_container, text="REMOVE STUDENT",font = ("Montserrat Alternates",16))
        self.removebtn.grid(row=3, column=2,sticky = "ew",padx = 60)
        self.removebtn.configure(fg_color="red")

    def load_students(self):
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        students = get_all_students()

        # Insert rows into Treeview
        for student in students:
            self.tree.insert("", "end", values=student[:7])

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
        student_id = self.idEntry.get()
        full_name = self.nameEntry.get()
        sex = self.sexEntry.get()
        parent_name = self.parentEntry.get()
        occupation = self.occupationEntry.get()
        phone = self.phoneEntry.get()
        grade = self.gradeEntry.get()
        photo_path = getattr(self, "saved_photo_path", None)  # default to None

        if student_exists(student_id):
            messagebox.showwarning(title="Warning", message="Student ID already exists. Please use a unique ID.")
            return

        try:
            insert_student(
                student_id, full_name, sex, parent_name,
                occupation, phone, grade, photo_path
            )
            messagebox.showinfo(title="Success", message="Student record saved!")
            self.ams_add_container.destroy()
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e), icon="error")

    def updateStudent(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a student record to update.")
            return

        student_data = self.tree.item(selected_item)['values']
        if not student_data:
            messagebox.showerror("Error", "Failed to get student data from selection.")
            return

        student_id = student_data[0]

        # Query the database for full student data, including photo path
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, sex, parent_name, occupation, phone, grade, photo_path FROM students WHERE student_id = ?", (student_id,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            messagebox.showerror("Not Found", f"No data found for student ID: {student_id}")
            return

        full_name, sex, parent, occupation, phone, grade, photo_path = result

        # Create the update form UI
        self.ams_update_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_update_container.grid(row=1, column=1, sticky="nsew")
        self.ams_update_container.rowconfigure(0, weight=1)
        self.ams_update_container.rowconfigure((1, 2), weight=2)
        self.ams_update_container.columnconfigure((0, 1, 2), weight=1)

        # Image Frame
        self.photoFrame = c.CTkFrame(self.ams_update_container, width=200, height=200, border_color="#3c507d")
        self.photoFrame.pack(padx=20, pady=10)

        # Load and display the image
        try:
            if photo_path and os.path.exists(photo_path):
                image = Image.open(photo_path)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            image = Image.new("RGB", (200, 200), color="gray")  # fallback placeholder

        image = image.resize((200, 200))
        photo_image = ImageTk.PhotoImage(image)
        self.image_label = c.CTkLabel(self.photoFrame, image=photo_image, text="")
        self.image_label.image = photo_image  # Prevent garbage collection
        self.image_label.pack()

        self.uploadphoto = c.CTkButton(self.ams_update_container, text="Upload", font=("Montserrat Alternates", 16), width=200)
        self.uploadphoto.pack(padx=20, pady=10)

        # Populate Entry Widgets
        self.idEntry = c.CTkEntry(self.ams_update_container, placeholder_text="Student ID", font=("Montserrat Alternates", 16), width=600)
        self.idEntry.insert(0, student_id)
        self.idEntry.pack(padx=0, pady=10)

        self.nameEntry = c.CTkEntry(self.ams_update_container, placeholder_text="Full Name", font=("Montserrat Alternates", 16), width=600)
        self.nameEntry.insert(0, full_name)
        self.nameEntry.pack(padx=0, pady=10)

        self.sexEntry = c.CTkOptionMenu(self.ams_update_container, values=["Male", "Female"], font=("Montserrat Alternates", 16), width=600)
        self.sexEntry.set(sex)
        self.sexEntry.pack(padx=0, pady=10)

        self.parentEntry = c.CTkEntry(self.ams_update_container, placeholder_text="Parent/Guardian", font=("Montserrat Alternates", 16), width=600)
        self.parentEntry.insert(0, parent)
        self.parentEntry.pack(padx=0, pady=10)

        self.occupationEntry = c.CTkEntry(self.ams_update_container, placeholder_text="Occupation", font=("Montserrat Alternates", 16), width=600)
        self.occupationEntry.insert(0, occupation)
        self.occupationEntry.pack(padx=0, pady=10)

        self.phoneEntry = c.CTkEntry(self.ams_update_container, placeholder_text="Phone Number", font=("Montserrat Alternates", 16), width=600)
        self.phoneEntry.insert(0, phone)
        self.phoneEntry.pack(padx=0, pady=10)

        self.gradeEntry = c.CTkEntry(self.ams_update_container, placeholder_text="Grade", font=("Montserrat Alternates", 16), width=600)
        self.gradeEntry.insert(0, grade)
        self.gradeEntry.pack(padx=0, pady=10)

        self.submit = c.CTkButton(self.ams_update_container, text="UPDATE", font=("Montserrat Alternates", 16), width=600)
        self.submit.pack(padx=0, pady=10)

        self.cancel = c.CTkButton(self.ams_update_container, text="CLOSE", font=("Montserrat Alternates", 16), width=600)
        self.cancel.configure(command=lambda: self.ams_update_container.destroy())
        self.cancel.pack(padx=0, pady=5)

    def attendance(self):
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)

    def report_popup(self):
        self.pop_window = c.CTkToplevel(self.ui)
        self.pop_window.geometry("500x350")
        self.pop_window.transient(self.ui)
        self.pop_window.update_idletasks()
        self.pop_window.grab_set()
        self.pop_window.title("Generate Report")

        # Center popup
        main_x = self.ui.winfo_x()
        main_y = self.ui.winfo_y()
        main_width = self.ui.winfo_width()
        main_height = self.ui.winfo_height()
        popup_width = self.pop_window.winfo_width()
        popup_height = self.pop_window.winfo_height()
        x = main_x + (main_width // 2) - (popup_width // 2)
        y = main_y + (main_height // 2) - (popup_height // 2)
        self.pop_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        self.pop_window.focus()

        # Grade selection
        grades = ["Grade"] + [f"Grade {i}" for i in range(1, 13)]
        self.gradeAccess = c.CTkOptionMenu(self.pop_window, values=grades, width=300, font=("Montserrat Alternates", 16), fg_color="#7691AD")
        self.gradeAccess.pack(padx=10, pady=10)

        # Subject selection (dynamic if you want to assign subjects per grade)
        self.subjects_by_grade = {
            f"Grade {i}": ["Mathematics", "Science", "English", "Social Studies", "ICT"] for i in range(1, 7)
        }
        self.subjects_by_grade.update({
            f"Grade {i}": ["Mathematics", "Science", "Pre Algebra", "Bible", "English", "Social Studies", "ICT"] for i in range(7, 13)
        })
        self.subject_var = tk.StringVar(value="Subject")
        self.subject_menu = c.CTkOptionMenu(self.pop_window, variable=self.subject_var, values=["Subject"], width=300, font=("Montserrat Alternates", 16), fg_color="#7691AD")
        self.subject_menu.pack(padx=10, pady=10)

        def update_subjects(*args):
            grade = self.gradeAccess.get()
            subjects = self.subjects_by_grade.get(grade, ["Subject"])
            self.subject_menu.configure(values=subjects)
            if subjects:
                self.subject_var.set(subjects[0])
            else:
                self.subject_var.set("Subject")
        self.gradeAccess.configure(command=lambda _: update_subjects())

        # Test type selection
        self.test_types = ["Quiz", "Project", "Test", "Exam"]
        self.test_type_var = tk.StringVar(value="Type of Test")
        self.test_type_menu = c.CTkOptionMenu(self.pop_window, variable=self.test_type_var, values=self.test_types, width=300, font=("Montserrat Alternates", 16), fg_color="#7691AD")
        self.test_type_menu.pack(padx=10, pady=10)

        # Submit button
        self.subbtn = c.CTkButton(self.pop_window, text="Submit", width=300, font=("Montserrat Alternates", 16), fg_color="#3c507d")
        self.subbtn.pack(padx=10, pady=10)
        self.subbtn.configure(command=self.Report)

    def Report(self):
        # Get selected grade, subject, and test type
        grade = self.gradeAccess.get()
        subject = self.subject_var.get()
        test_type = self.test_type_var.get()
        self.pop_window.destroy()

        # Main container for the report sheet
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)

        # Student ID Entry
        self.report_id_frame = c.CTkFrame(self.ams_parent_container, fg_color="#F5F5F5")
        self.report_id_frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky="ew")
        self.report_id_label = c.CTkLabel(self.report_id_frame, text="Enter Student ID:", font=("Montserrat Alternates", 16))
        self.report_id_label.pack(side="left", padx=10)
        self.report_id_entry = c.CTkEntry(self.report_id_frame, placeholder_text="Student ID", font=("Montserrat Alternates", 16), width=200)
        self.report_id_entry.pack(side="left", padx=10)
        self.report_id_btn = c.CTkButton(self.report_id_frame, text="Load Student", font=("Montserrat Alternates", 16), fg_color="#3c507d")
        self.report_id_btn.pack(side="left", padx=10)
        self.report_id_btn.configure(command=lambda: self.load_student_for_report(grade, subject))

    def load_student_for_report(self, grade, subject):
        student_id = self.report_id_entry.get().strip()
        if not student_id:
            messagebox.showwarning("Input Error", "Please enter a Student ID.")
            return

        # Fetch student info
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, grade FROM students WHERE student_id = ?", (student_id,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            messagebox.showerror("Not Found", f"No student found with ID: {student_id}")
            return

        full_name, student_grade = result

        # Remove previous report frame if exists
        if hasattr(self, "report_sheet_frame"):
            self.report_sheet_frame.destroy()

        # Report Sheet UI
        self.report_sheet_frame = c.CTkFrame(self.ams_parent_container, fg_color="#FFFFFF", border_color="#3c507d", border_width=2)
        self.report_sheet_frame.grid(row=1, column=0, columnspan=3, padx=30, pady=10, sticky="nsew")

        # Student Info
        info_text = f"Student: {full_name} (ID: {student_id})   Grade: {student_grade}   Subject: {subject}"
        self.student_info_label = c.CTkLabel(self.report_sheet_frame, text=info_text, font=("Montserrat Alternates", 16, "bold"))
        self.student_info_label.pack(pady=10)

        # Multiple test types for the subject
        self.result_entries = {}
        entry_frame = c.CTkFrame(self.report_sheet_frame, fg_color="#FFFFFF")
        entry_frame.pack(pady=10)

        test_types = ["Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam"]
        for ttype in test_types:
            entry = c.CTkEntry(entry_frame, placeholder_text=f"{ttype}", font=("Montserrat Alternates", 14), width=300)
            entry.pack(side="top", padx=10, pady=2)
            self.result_entries[ttype] = entry

        # Comments
        self.comment_label = c.CTkLabel(self.report_sheet_frame, text="Teacher's Comment:", font=("Montserrat Alternates", 14))
        self.comment_label.pack(pady=(20, 5))
        self.comment_entry = c.CTkEntry(self.report_sheet_frame, placeholder_text="Enter comments...", font=("Montserrat Alternates", 14), width=400)
        self.comment_entry.pack(pady=5)

        # Save Button
        self.save_report_btn = c.CTkButton(self.report_sheet_frame, text="Save Results", font=("Montserrat Alternates", 16), fg_color="#3c507d")
        self.save_report_btn.pack(pady=20)
        self.save_report_btn.configure(command=lambda: self.save_student_results(student_id, subject))

        # Print Report Card to Terminal Button
        self.print_report_btn = c.CTkButton(
            self.report_sheet_frame,
            text="Show Report Card",
            font=("Montserrat Alternates", 16),
            fg_color="#7691AD",
            command=lambda: self.show_report_card_ctk(student_id)
        )
        self.print_report_btn.pack(pady=10)

    def save_student_results(self, student_id, subject):
        # Save all test types for this subject
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                subject TEXT,
                test_type TEXT,
                score REAL,
                comment TEXT
            )
        """)
        comment = self.comment_entry.get().strip()
        for ttype, entry in self.result_entries.items():
            value = entry.get().strip()
            if not value:
                continue  # skip empty
            try:
                score = float(value)
            except ValueError:
                messagebox.showwarning("Input Error", f"Score for {subject} {ttype} must be a number.")
                return
            # Remove previous result for this student/subject/test_type (optional)
            cursor.execute("DELETE FROM results WHERE student_id = ? AND subject = ? AND test_type = ?", (student_id, subject, ttype))
            cursor.execute(
                "INSERT INTO results (student_id, subject, test_type, score, comment) VALUES (?, ?, ?, ?, ?)",
                (student_id, subject, ttype, score, comment)
            )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Results saved successfully!")
        self.report_sheet_frame.destroy()

    def print_report_card_terminal(self, student_id):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, grade FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        if not student:
            print("No student found with that ID.")
            conn.close()
            return
        full_name, grade = student

        cursor.execute("""
            SELECT subject, test_type, score
            FROM results
            WHERE student_id = ?
            ORDER BY subject, test_type
        """, (student_id,))
        results = cursor.fetchall()
        conn.close()

        # Organize results
        subjects = defaultdict(dict)
        for subject, test_type, score in results:
            subjects[subject][test_type] = score

        print("\n" + "="*60)
        print(f"Report Card for {full_name} (ID: {student_id})")
        print(f"Grade: {grade}")
        print("="*60)
        for subject, tests in subjects.items():
            print(f"\nSubject: {subject}")
            total = 0
            for ttype in ["Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam"]:
                score = tests.get(ttype, "-")
                print(f"  {ttype}: {score}")
                if isinstance(score, (int, float)):
                    total += score
            print(f"  Total: {total}")
            print(f"  Position: (not calculated)")  # You can implement position logic here
            print("-"*40)
        print("="*60)

    def show_report_card_ctk(self, student_id):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, grade FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        if not student:
            messagebox.showerror("Not Found", "No student found with that ID.")
            conn.close()
            return
        full_name, grade = student

        cursor.execute("""
            SELECT subject, test_type, score
            FROM results
            WHERE student_id = ?
            ORDER BY subject, test_type
        """, (student_id,))
        results = cursor.fetchall()
        conn.close()

        from collections import defaultdict

        subjects = defaultdict(dict)
        for subject, test_type, score in results:
            subjects[subject][test_type] = score

        # Create popup window
        popup = c.CTkToplevel(self.ui)
        popup.title("Report Card")
        popup.geometry("800x500")
        popup.grab_set()

        # Header
        header = c.CTkLabel(popup, text=f"Report Card for {full_name} (ID: {student_id})", font=("Montserrat Alternates", 18, "bold"))
        header.pack(pady=10)
        grade_label = c.CTkLabel(popup, text=f"Grade: {grade}", font=("Montserrat Alternates", 16))
        grade_label.pack(pady=5)

        # Table headers
        table_frame = c.CTkFrame(popup)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)

        headers = ["Subject", "Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam", "Total"]
        for col, h in enumerate(headers):
            lbl = c.CTkLabel(table_frame, text=h, font=("Montserrat Alternates", 14, "bold"), width=90)
            lbl.grid(row=0, column=col, padx=2, pady=2)

        # Table rows
        for row, (subject, tests) in enumerate(subjects.items(), start=1):
            c.CTkLabel(table_frame, text=subject, font=("Montserrat Alternates", 13), width=90).grid(row=row, column=0, padx=2, pady=2)
            total = 0
            for col, ttype in enumerate(["Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam"], start=1):
                score = tests.get(ttype, "-")
                c.CTkLabel(table_frame, text=str(score), font=("Montserrat Alternates", 13), width=90).grid(row=row, column=col, padx=2, pady=2)
                if isinstance(score, (int, float)):
                    total += score
            c.CTkLabel(table_frame, text=str(total), font=("Montserrat Alternates", 13, "bold"), width=90).grid(row=row, column=7, padx=2, pady=2)

        # Optionally, add a close button
        close_btn = c.CTkButton(popup, text="Close", command=popup.destroy, fg_color="#3c507d")
        close_btn.pack(pady=10)

    def show_report_card(self):
        # Create parent container
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.rowconfigure((1, 2), weight=2)
        self.ams_parent_container.columnconfigure((0, 1, 2), weight=1)

        # Table Frame
        table_frame = c.CTkFrame(self.ams_parent_container, fg_color="#FFFFFF", border_color="#3c507d", border_width=2)
        table_frame.grid(row=0, column=0, columnspan=3, padx=30, pady=20, sticky="nsew")

        # Treeview columns
        columns = ["Student ID", "Name", "Subject", "Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam", "Total"]

        tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=18)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        # Style the Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#f0f0f0",
                        foreground="black",
                        rowheight=28,
                        fieldbackground="#FFFFFF",
                        font=("Montserrat Alternates", 12))
        style.configure("Treeview.Heading", font=("Montserrat Alternates", 13, "bold"))

        tree.pack(fill="both", expand=True, padx=5, pady=5)

        # Fetch all results and organize by student and subject
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.student_id, s.full_name, r.subject, r.test_type, r.score
            FROM students s
            JOIN results r ON s.student_id = r.student_id
            ORDER BY s.student_id, r.subject, r.test_type
        """)
        rows = cursor.fetchall()
        conn.close()

        data = defaultdict(lambda: defaultdict(dict))
        for student_id, name, subject, test_type, score in rows:
            data[(student_id, name, subject)][test_type] = score

        test_types = ["Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam"]
        for (student_id, name, subject), scores in data.items():
            row_data = [student_id, name, subject]
            total = 0
            for ttype in test_types:
                score = scores.get(ttype, "-")
                row_data.append(score)
                if isinstance(score, (int, float)):
                    total += score
            row_data.append(total)
            tree.insert("", "end", values=row_data)

        # Optionally, add a close button
        close_btn = c.CTkButton(self.ams_parent_container, text="Close", command=self.ams_parent_container.destroy, fg_color="#3c507d")
        close_btn.grid(row=2, column=1, pady=10)
       

if __name__ == '__main__':
    systemWindow = c.CTk()
    classObject = AgapeSystem(systemWindow)
    systemWindow.mainloop()
