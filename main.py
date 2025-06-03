import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import customtkinter as c
from PIL import Image, ImageTk
import os
import sqlite3
import shutil
from databaseCode import create_students_table, insert_student, student_exists, get_all_students
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import string
import statistics
import requests

class AgapeSystem:
    def __init__(self, ui):
        self.ui = ui
        self.ui.title("Agape School Management System")
        self.ui.geometry("1300x760+0+0")
        c.set_appearance_mode("light")
        self.ui.rowconfigure(0, weight=1)
        self.ui.columnconfigure(0, weight=1)
        create_students_table()
        self.content()
        self.dashboard()

    def content(self):
        self.parent_widget = c.CTkFrame(self.ui,fg_color="#f8fafc", corner_radius=0)
        self.parent_widget.grid(row=0, column=0, sticky="nsew")
        self.parent_widget.rowconfigure(0, weight=0)
        self.parent_widget.rowconfigure(1, weight=20)
        self.parent_widget.columnconfigure(0, weight=1)
        self.parent_widget.columnconfigure(1, weight=30)

        self.top_navigation = c.CTkFrame(self.parent_widget, height=60, corner_radius=0, fg_color="#011c40")
        self.top_navigation.grid(row=0, column=0, sticky="nwe", columnspan=2)
        # Add title label
        self.title_label = c.CTkLabel(
            self.top_navigation,
            text="Agape School Management System",
            font=("Montserrat Alternates", 20, "bold"),
            text_color="#fff",
            fg_color="#011c40"
        )
        self.title_label.pack(side="left", padx=30, pady=10)

        self.side_navigation = c.CTkFrame(self.parent_widget, corner_radius=0, fg_color="#023859")
        self.side_navigation.grid(row=1, column=0, sticky="nsew")

        

        # --- NAVIGATION BUTTONS ---
        nav_btn_style = dict(fg_color="#3c507d", font=("Montserrat Alternates", 16, "bold"), corner_radius=10, height=48)
        self.dashboard_btn = c.CTkButton(self.side_navigation, text="Dashboard", **nav_btn_style, command=self.dashboard)
        self.dashboard_btn.pack(pady=(30, 18), padx=16, fill="x")
        self.dashboard_btn.bind("<Return>", lambda e: self.dashboard()) 
        self.student_btn = c.CTkButton(self.side_navigation, text="Students", **nav_btn_style, command=self.Student)
        self.student_btn.pack(pady=18, padx=16, fill="x")
        self.report_btn = c.CTkButton(self.side_navigation, text="Reports", **nav_btn_style, command=self.report_popup)
        self.report_btn.pack(pady=18, padx=16, fill="x")
        self.com_btn = c.CTkButton(self.side_navigation, text="Communication", **nav_btn_style, command=self.communication)
        self.com_btn.pack(pady=18, padx=16, fill="x")
        self.logout_btn = c.CTkButton(self.side_navigation, text="Logout", **nav_btn_style)
        self.logout_btn.pack(pady=(18, 30), padx=16, fill="x")
        self.logout_btn.bind("<Button-1>", lambda e: self.ui.destroy())
    def communication(self):
        # Destroy previous content in the right panel if any
        for widget in self.parent_widget.grid_slaves(row=1, column=1):
            widget.destroy()

        self.com_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.com_container.grid(row=1, column=1, sticky="nsew")
        self.com_container.rowconfigure(0, weight=1)
        self.com_container.columnconfigure(0, weight=1)

        # Title
        c.CTkLabel(
            self.com_container,
            text="Communication Center",
            font=("Montserrat Alternates", 26, "bold"),
            text_color="#26658C"
        ).pack(pady=(28, 8))

        # Decorative separator
        c.CTkFrame(self.com_container, height=2, fg_color="#54ACBF").pack(fill="x", padx=40, pady=(0, 18))

        # Entry fields for Message ID and Phone Number
        entry_frame = c.CTkFrame(self.com_container, fg_color="#eaf6f6", corner_radius=12)
        entry_frame.pack(pady=(10, 5), padx=30, fill="x")

        c.CTkLabel(
            entry_frame,
            text="Sender ID:",
            font=("Montserrat Alternates", 15, "bold"),
            text_color="#26658C"
        ).grid(row=0, column=0, padx=(18, 6), pady=12, sticky="e")
        self.msg_id_entry = c.CTkEntry(entry_frame, placeholder_text="e.g. AGAPE", font=("Montserrat Alternates", 15), width=220)
        self.msg_id_entry.grid(row=0, column=1, padx=(0, 18), pady=12)

        c.CTkLabel(
            entry_frame,
            text="Recipient Phone:",
            font=("Montserrat Alternates", 15, "bold"),
            text_color="#26658C"
        ).grid(row=0, column=2, padx=(8, 6), pady=12, sticky="e")
        self.phone_entry = c.CTkEntry(entry_frame, placeholder_text="e.g. 233XXXXXXXXX", font=("Montserrat Alternates", 15), width=220)
        self.phone_entry.grid(row=0, column=3, padx=(0, 18), pady=12)

        # TextBox for message body
        msg_frame = c.CTkFrame(self.com_container, fg_color="#f8fafc", corner_radius=12)
        msg_frame.pack(pady=(18, 5), padx=30, fill="x")
        c.CTkLabel(
            msg_frame,
            text="Message Body:",
            font=("Montserrat Alternates", 15, "bold"),
            text_color="#26658C"
        ).pack(anchor="w", padx=18, pady=(10, 2))
        self.message_body = c.CTkTextbox(msg_frame, font=("Montserrat Alternates", 15), width=540, height=140, fg_color="#fff", border_color="#54ACBF", border_width=2, corner_radius=8)
        self.message_body.pack(padx=18, pady=(0, 12), fill="x")
        self.message_body.insert("1.0", "Enter your message here...")

        # Info note
        c.CTkLabel(
            self.com_container,
            text="Tip: Use a valid sender ID and international phone format (e.g. 233XXXXXXXXX).",
            font=("Montserrat Alternates", 12),
            text_color="#7691AD"
        ).pack(pady=(0, 8))

        # Buttons
        btn_frame = c.CTkFrame(self.com_container, fg_color="#F5F5F5")
        btn_frame.pack(pady=15)

        self.send_btn = c.CTkButton(
            btn_frame,
            text="Send",
            font=("Montserrat Alternates", 16, "bold"),
            fg_color="#54ACBF",
            hover_color="#26658C",
            text_color="#fff",
            width=180,
            corner_radius=8,
            command=self.send_message  
        )
        self.send_btn.grid(row=0, column=0, padx=10)

        self.submit_btn = c.CTkButton(
            btn_frame,
            text="Cancel",
            font=("Montserrat Alternates", 16, "bold"),
            fg_color="#26658C",
            hover_color="#54ACBF",
            text_color="#fff",
            width=180,
            corner_radius=8,
            command=lambda : self.com_container.destroy()  
        )
        self.submit_btn.grid(row=0, column=1, padx=10)

    def send_message(self):

        msg_id = self.msg_id_entry.get().strip()
        phone = self.phone_entry.get().strip()
        message = self.message_body.get("1.0", "end").strip()

        if not msg_id or not phone or not message:
            messagebox.showwarning("Input Error", "Please fill in all fields before sending.")
            return

        # Replace with your actual Arkesel API key
        api_key = "YOUR_ARKESEL_API_KEY"
        url = "https://sms.arkesel.com/api/v2/sms/send"

        payload = {
            "sender": msg_id,
            "message": message,
            "recipients": [phone]
        }
        headers = {
            "api-key": api_key,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                resp_json = response.json()
                if resp_json.get("code") == "ok":
                    messagebox.showinfo("Success", "Message sent successfully!")
                else:
                    messagebox.showerror("Error", f"Failed to send message: {resp_json.get('message', 'Unknown error')}")
            else:
                messagebox.showerror("Error", f"HTTP Error: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    
    def dashboard(self):
        for widget in self.parent_widget.grid_slaves(row=1, column=1):
            widget.destroy()

        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.columnconfigure(0, weight=1)
        # --- DASHBOARD MAIN CONTAINER ---
        self.dash_container = c.CTkFrame(self.ams_parent_container, fg_color="#f8fafc", corner_radius=18)
        self.dash_container.grid(row=0, column=0, sticky="nsew", padx=24, pady=18)
        self.dash_container.rowconfigure(0, weight=1)
        self.dash_container.rowconfigure(1, weight=2)
        self.dash_container.rowconfigure(2, weight=2)
        self.dash_container.columnconfigure(0, weight=1)
        self.dash_container.columnconfigure(1, weight=1)
        self.dash_container.columnconfigure(2, weight=1)

        # --- DASHBOARD CARDS ---
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM students WHERE sex = 'Male'")
        total_boys = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM students WHERE sex = 'Female'")
        total_girls = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM students")
        total_students = cursor.fetchone()[0]
        conn.close()

        card_style = dict(height=120, corner_radius=16)
        self.card1 = c.CTkFrame(self.dash_container, fg_color="#26658C", **card_style)
        self.card1.grid(row=0, column=0, sticky="nwe", padx=(0, 12), pady=15, ipadx=40)
        c.CTkLabel(self.card1, text="Total Boys", font=("Montserrat Alternates", 18, "bold"), fg_color="#26658C", text_color="#fff").pack(pady=(18, 4))
        c.CTkLabel(self.card1, text=str(total_boys), font=("Montserrat Alternates", 36, "bold"), fg_color="#26658C", text_color="#fff").pack()
        c.CTkLabel(self.card1, text="", font=("Montserrat Alternates", 12), fg_color="#26658C", text_color="#cbe4f9").pack(pady=(2, 0))

        self.card2 = c.CTkFrame(self.dash_container, fg_color="#54ACBF", **card_style)
        self.card2.grid(row=0, column=1, sticky="nwe", padx=12, pady=15, ipadx=40)
        c.CTkLabel(self.card2, text="Total Girls", font=("Montserrat Alternates", 18, "bold"), fg_color="#54ACBF", text_color="#fff").pack(pady=(18, 4))
        c.CTkLabel(self.card2, text=str(total_girls), font=("Montserrat Alternates", 36, "bold"), fg_color="#54ACBF", text_color="#fff").pack()
        c.CTkLabel(self.card2, text="", font=("Montserrat Alternates", 12), fg_color="#54ACBF", text_color="#eaf6f6").pack(pady=(2, 0))

        self.card3 = c.CTkFrame(self.dash_container, fg_color="#7691AD", **card_style)
        self.card3.grid(row=0, column=2, sticky="nwe", padx=(12, 0), pady=15, ipadx=40)
        c.CTkLabel(self.card3, text="Total Students", font=("Montserrat Alternates", 18, "bold"), fg_color="#7691AD", text_color="#fff").pack(pady=(18, 4))
        c.CTkLabel(self.card3, text=str(total_students), font=("Montserrat Alternates", 36, "bold"), fg_color="#7691AD", text_color="#fff").pack()
        self.graph_card1 = c.CTkFrame(self.dash_container, fg_color="#fff", corner_radius=16, border_color="#54ACBF", border_width=2)
        self.graph_card1.grid(row=1, column=0, sticky="nsew", padx=(0, 12), pady=15, columnspan=2)
        self.dash_container.rowconfigure(1, weight=2)
        self.dash_container.columnconfigure(0, weight=2)
        self.dash_container.columnconfigure(1, weight=2)
        # --- BAR CHART: STUDENTS PER GRADE ---
        self.graph_card1 = c.CTkFrame(self.dash_container, fg_color="#fff", corner_radius=16, border_color="#54ACBF", border_width=2)
        self.graph_card1.grid(row=1, column=0, sticky="nsew", padx=(0, 12), pady=15, columnspan=2)
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT grade, COUNT(*) FROM students GROUP BY grade")
        data = cursor.fetchall()
        conn.close()
        grades = [row[0] for row in data]
        counts = [row[1] for row in data]
        bar_colors = ["#26658C", "#54ACBF", "#7691AD", "#EFEACD", "#3c507d", "#023859", "#011c40"]
        colors = [bar_colors[i % len(bar_colors)] for i in range(len(grades))]
        fig, ax = plt.subplots(figsize=(5.5, 3.2), dpi=120)
        bars = ax.bar(grades, counts, color=colors, edgecolor="#22223b", linewidth=1.2)
        ax.set_title("Number of Students per Grade", fontsize=14, fontweight="bold", color="#26658C")
        ax.set_xlabel("Grade", fontsize=12)
        ax.set_ylabel("Count", fontsize=12)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # Only label bars with their actual count, not with repeated numbers
        for bar, count in zip(bars, counts):
            ax.annotate(
            f"{count}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center', va='bottom',
            fontsize=10, fontweight="bold"
            )
        ax.grid(axis='y', linestyle='--', alpha=0.4)
        self.dash_container.columnconfigure(2, weight=1)
        canvas = FigureCanvasTkAgg(fig, master=self.graph_card1)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=12, pady=8)

        # --- PIE CHART: GENDER DISTRIBUTION ---
        self.graph_card2 = c.CTkFrame(self.dash_container, fg_color="#fff", corner_radius=16, border_color="#7691AD", border_width=2)
        self.graph_card2.grid(row=1, column=2, sticky="nsew", padx=(12, 0), pady=15)
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT sex, COUNT(*) FROM students GROUP BY sex")
        pie_data = cursor.fetchall()
        conn.close()
        labels = [row[0] for row in pie_data]
        sizes = [row[1] for row in pie_data]
        pie_colors = ["#26658C", "#54ACBF", "#7691AD", "#EFEACD"]
        fig2, ax2 = plt.subplots(figsize=(3.5, 3.2), dpi=120)
        wedges, texts, autotexts = ax2.pie(
            sizes, labels=labels, autopct='%1.1f%%', startangle=90,
            colors=pie_colors[:len(labels)], textprops={'fontsize': 12, 'color': "#22223b"}
        )
        for autotext in autotexts:
            autotext.set_color("#fff")
            autotext.set_fontweight("bold")
        ax2.set_title("Gender Distribution", fontsize=13, fontweight="bold", color="#7691AD")
        ax2.axis('equal')
        plt.tight_layout()
        canvas2 = FigureCanvasTkAgg(fig2, master=self.graph_card2)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill="both", expand=True, padx=12, pady=8)

        # --- TOP STUDENTS PROGRESS ---
        self.graph_card3 = c.CTkScrollableFrame(self.dash_container, fg_color="#FFFFFF", corner_radius=16, border_color="#26658C", border_width=2)
        self.graph_card3.grid(row=2, column=0, sticky="nsew", padx=0, pady=15, columnspan=3)
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.student_id, s.full_name, SUM(r.score) as total_score
            FROM students s
            JOIN results r ON s.student_id = r.student_id
            GROUP BY s.student_id
            ORDER BY total_score DESC
            LIMIT 3
        """)
        top_students = cursor.fetchall()
        conn.close()
        max_score = top_students[0][2] if top_students else 1
        c.CTkLabel(self.graph_card3, text="Top 3 Students", font=("Montserrat Alternates", 16, "bold"), text_color="#26658C").pack(pady=(16, 8), anchor="w", padx=24)
        for idx, (student_id, full_name, total_score) in enumerate(top_students):
            card = c.CTkFrame(self.graph_card3, fg_color="#f8fafc", corner_radius=12)
            card.pack(fill="x", padx=24, pady=(8 if idx == 0 else 4, 8))
            label = c.CTkLabel(card, text=f"{idx+1}. {full_name} (ID: {student_id})", font=("Montserrat Alternates", 14, "bold"), text_color="#3c507d")
            label.pack(pady=(10, 2), anchor="w", padx=16)
            progress = c.CTkProgressBar(card, width=420, height=18, progress_color="#54ACBF", fg_color="#e3e9f7", corner_radius=8)
            progress.set(total_score / max_score if max_score else 0)
            progress.pack(pady=2, padx=16)
            score_label = c.CTkLabel(card, text=f"Total Score: {total_score:.2f}", font=("Montserrat Alternates", 12), text_color="#26658C")
            score_label.pack(pady=(0, 8), anchor="w", padx=32)

    def Student(self):
        # Destroy previous content in the right panel if any
        for widget in self.parent_widget.grid_slaves(row=1, column=1):
            widget.destroy()

        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=1)
        self.ams_parent_container.columnconfigure(0, weight=1)

        self.ams_student_container = c.CTkFrame(self.ams_parent_container, fg_color="#F5F5F5")
        self.ams_student_container.grid(row=0, column=0, sticky="nsew")
        self.ams_student_container.rowconfigure(0, weight=0)  # Search bar row
        self.ams_student_container.rowconfigure(1, weight=1)  # Table row
        self.ams_student_container.rowconfigure(2, weight=0)  # Buttons row
        self.ams_student_container.columnconfigure((0, 1, 2), weight=1)

        # Search Frame
        self.searchframe = c.CTkFrame(self.ams_student_container, height=60, corner_radius=0, fg_color="#F5F5F5")
        self.searchframe.grid(row=0, column=0, columnspan=3, sticky="ew", padx=30, pady=(10, 5))
        self.searchframe.columnconfigure(0, weight=3)
        self.searchframe.columnconfigure(1, weight=1)
        self.searchframe.columnconfigure(2, weight=1)

        self.search_bar = c.CTkEntry(self.searchframe, placeholder_text="Search", font=("Montserrat Alternates", 16), fg_color="#F5F5F5", width=400)
        self.search_bar.grid(row=0, column=0, padx=0, pady=2, sticky="ew")
        self.search_bar.bind("<KeyRelease>", lambda event: self.filter_students())
        self.search_btn = c.CTkButton(self.searchframe, text="Search", font=("Montserrat Alternates", 16), fg_color="#3c507d", command=self.filter_students)
        self.search_btn.grid(row=0, column=1, padx=20, sticky="ew")
        self.sortoption = c.CTkOptionMenu(self.searchframe, values=["None", "Grade", "Sex"], font=("Montserrat Alternates", 16), fg_color="#3c507d", command=lambda _: self.filter_students())
        self.sortoption.set("None")
        self.sortoption.grid(row=0, column=2, padx=20, sticky="ew")

        # Table Frame
        self.ams_table_frame = c.CTkFrame(
            self.ams_student_container, 
            fg_color="#f8fafc", 
            border_color="#3c507d", 
            border_width=2
        )
        self.ams_table_frame.grid(
            row=1, column=0, columnspan=3, sticky="nsew", padx=30, pady=(0, 5)
        )
        self.ams_table_frame.rowconfigure(0, weight=1)
        self.ams_table_frame.columnconfigure(0, weight=1)

        self.columns = ("ID", "Name", "Sex", "Parent", "Occupation", "Phone", "Grade")
        self.tree = ttk.Treeview(
            self.ams_table_frame, 
            columns=self.columns, 
            show="headings", 
            height=16,
        )

        # Custom style for table
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="#f8fafc",
            foreground="#22223b",
            rowheight=36,
            fieldbackground="#f8fafc",
            font=("Montserrat Alternates", 13),
            borderwidth=0
        )
        style.configure(
            "Treeview.Heading",
            font=("Montserrat Alternates", 15, "bold"),
            background="#3c507d",
            foreground="#fff"
        )
        style.map("Treeview.Heading", background=[("active", "#26658C")])

        # Add striped row tags for alternate background colors
        self.tree.tag_configure("oddrow", background="#e3e9f7")
        self.tree.tag_configure("evenrow", background="#f8fafc")

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center", stretch=True)
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbars
        vsb = ttk.Scrollbar(self.ams_table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.grid(row=0, column=1, sticky="ns")
        hsb = ttk.Scrollbar(self.ams_table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=hsb.set)
        hsb.grid(row=1, column=0, sticky="ew")

        # Responsive loading with row tags
        def load_students_with_tags():
            for row in self.tree.get_children():
                self.tree.delete(row)
            students = get_all_students()
            for idx, student in enumerate(students):
                tag = "evenrow" if idx % 2 == 0 else "oddrow"
                self.tree.insert("", "end", values=student[:7], tags=(tag,))
        self.load_students = load_students_with_tags

        self.load_students()

        # Button Frame (for better responsiveness)
        self.button_frame = c.CTkFrame(self.ams_student_container, fg_color="#F5F5F5")
        self.button_frame.grid(row=2, column=0, columnspan=3, sticky="ew", padx=30, pady=(5, 20))
        self.button_frame.columnconfigure((0, 1, 2), weight=1)

        self.addbtn = c.CTkButton(self.button_frame, text="ADD STUDENT", font=("Montserrat Alternates", 16), fg_color="#3c507d", command=self.addStudent)
        self.addbtn.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        self.updatebtn = c.CTkButton(
            self.button_frame,
            text="UPDATE RECORD",
            font=("Montserrat Alternates", 16),
            fg_color="#3c507d",
            command=self.updateStudent
        )
        self.updatebtn.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        self.removebtn = c.CTkButton(
            self.button_frame,
            text="REMOVE STUDENT",
            font=("Montserrat Alternates", 16),
            fg_color="red",
            command=self.remove_student
        )
        self.removebtn.grid(row=0, column=2, sticky="ew", padx=10, pady=5)

    def remove_student(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a student record to remove.")
            return
        student_data = self.tree.item(selected_item)['values']
        if not student_data:
            messagebox.showerror("Error", "Failed to get student data from selection.")
            return
        student_id = student_data[0]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student ID: {student_id}?")
        if not confirm:
            return
        try:
            conn = sqlite3.connect("students.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
            cursor.execute("DELETE FROM results WHERE student_id = ?", (student_id,))
            conn.commit()
            conn.close()
            self.filter_students()
            messagebox.showinfo("Success", "Student record deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete student: {e}")

    def get_filtered_sorted_students(self):
        students = get_all_students()
        query = self.search_bar.get().strip().lower()
        sort_by = self.sortoption.get()
        if query:
            students = [
                s for s in students
                if query in str(s[0]).lower() or
                   query in str(s[1]).lower() or
                   query in str(s[2]).lower() or
                   query in str(s[3]).lower() or
                   query in str(s[4]).lower() or
                   query in str(s[5]).lower() or
                   query in str(s[6]).lower()
            ]
        if sort_by == "Grade":
            students.sort(key=lambda s: str(s[6]))
        elif sort_by == "Sex":
            students.sort(key=lambda s: str(s[2]))
        return students

    def filter_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for idx, student in enumerate(self.get_filtered_sorted_students()):
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=student[:7], tags=(tag,))

    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        students = get_all_students()
        for idx, student in enumerate(students):
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=student[:7], tags=(tag,))

    def addStudent(self):
        self.ams_add_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_add_container.grid(row=1, column=1, sticky="nsew")
        self.photoFrame = c.CTkFrame(self.ams_add_container, width=200, height=200, border_color="#3c507d")
        self.photoFrame.pack(padx=20, pady=10)
        self.uploadphoto = c.CTkButton(self.ams_add_container, text="Upload", font=("Montserrat Alternates", 16), width=200, fg_color="#3c507d", command=self.upload_passport)
        self.uploadphoto.pack(padx=20, pady=10)
        self.image_label = c.CTkLabel(self.photoFrame, text="", width=180, height=180)
        self.image_label.pack(padx=10, pady=10)
        # Auto-generate a unique Student ID
        def generate_unique_student_id():
            # Generate a unique student ID that does not exist in the database
            i = 1
            while True:
                student_id = f"AMS{i:03d}"
                conn = sqlite3.connect("students.db")
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM students WHERE student_id = ?", (student_id,))
                exists = cursor.fetchone()
                conn.close()
                if not exists:
                    return student_id
                i += 1

        self.idEntry = c.CTkEntry(self.ams_add_container, placeholder_text="Student ID", font=("Montserrat Alternates", 16), width=600)
        autogenerated_id = generate_unique_student_id()
        self.idEntry.insert(0, autogenerated_id)
        self.idEntry.pack(padx=0, pady=10)

        self.nameEntry = c.CTkEntry(self.ams_add_container, placeholder_text="Full Name", font=("Montserrat Alternates", 16), width=600)
        self.nameEntry.pack(padx=0, pady=10)

        self.sexEntry = c.CTkOptionMenu(self.ams_add_container, values=["Sex", "Male", "Female"], font=("Montserrat Alternates", 16), width=600, fg_color=None)
        self.sexEntry.pack(padx=0, pady=10)

        self.parentEntry = c.CTkEntry(self.ams_add_container, placeholder_text="Parent/Guardian", font=("Montserrat Alternates", 16), width=600)
        self.parentEntry.pack(padx=0, pady=10)

        self.occupationEntry = c.CTkEntry(self.ams_add_container, placeholder_text="Occupation", font=("Montserrat Alternates", 16), width=600)
        self.occupationEntry.pack(padx=0, pady=10)

        self.phoneEntry = c.CTkEntry(self.ams_add_container, placeholder_text="Phone Number", font=("Montserrat Alternates", 16), width=600)
        self.phoneEntry.pack(padx=0, pady=10)

        # Use OptionMenu for Grade selection
        grade_values = [f"Grade {i}" for i in range(1, 13)]
        self.gradeEntry = c.CTkOptionMenu(self.ams_add_container, values=grade_values, font=("Montserrat Alternates", 16), width=600)
        self.gradeEntry.set("Grade 1")
        self.gradeEntry.pack(padx=0, pady=10)
        self.submit = c.CTkButton(self.ams_add_container, text="SAVE", font=("Montserrat Alternates", 16), width=600, command=self.save_student_data)
        self.submit.pack(padx=0, pady=10)
        self.cancel = c.CTkButton(self.ams_add_container, text="CLOSE", font=("Montserrat Alternates", 16), width=600, command=lambda: self.ams_add_container.destroy())
        self.cancel.pack(padx=0, pady=5)

    def upload_passport(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            if not os.path.exists("images"):
                os.makedirs("images")
            filename = os.path.basename(file_path)
            destination_path = os.path.join("images", filename)
            shutil.copy(file_path, destination_path)
            self.saved_photo_path = destination_path
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
        photo_path = getattr(self, "saved_photo_path", None)
        if student_exists(student_id):
            messagebox.showwarning(title="Warning", message="Student ID already exists. Please use a unique ID.")
            return
        try:
            insert_student(student_id, full_name, sex, parent_name, occupation, phone, grade, photo_path)
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
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, sex, parent_name, occupation, phone, grade, photo_path FROM students WHERE student_id = ?", (student_id,))
        result = cursor.fetchone()
        conn.close()
        if not result:
            messagebox.showerror("Not Found", f"No data found for student ID: {student_id}")
            return
        full_name, sex, parent, occupation, phone, grade, photo_path = result
        self.ams_update_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_update_container.grid(row=1, column=1, sticky="nsew")
        self.photoFrame = c.CTkFrame(self.ams_update_container, width=200, height=200, border_color="#3c507d")
        self.photoFrame.pack(padx=20, pady=10)
        try:
            if photo_path and os.path.exists(photo_path):
                image = Image.open(photo_path)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            image = Image.new("RGB", (200, 200), color="gray")
        image = image.resize((200, 200))
        photo_image = ImageTk.PhotoImage(image)
        self.image_label = c.CTkLabel(self.photoFrame, image=photo_image, text="")
        self.image_label.image = photo_image
        self.image_label.pack()
        self.saved_photo_path = photo_path  # Save current photo path

        def upload_new_photo():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
            if file_path:
                if not os.path.exists("images"):
                    os.makedirs("images")
                filename = os.path.basename(file_path)
                destination_path = os.path.join("images", filename)
                shutil.copy(file_path, destination_path)
                self.saved_photo_path = destination_path
                img = Image.open(destination_path)
                img = img.resize((200, 200))
                new_photo = ImageTk.PhotoImage(img)
                self.image_label.configure(image=new_photo)
                self.image_label.image = new_photo

        self.uploadphoto = c.CTkButton(self.ams_update_container, text="Upload", font=("Montserrat Alternates", 16), width=200, command=upload_new_photo)
        self.uploadphoto.pack(padx=20, pady=10)
        self.idEntry = c.CTkEntry(self.ams_update_container, placeholder_text="Student ID", font=("Montserrat Alternates", 16), width=600)
        self.idEntry.insert(0, student_id)
        self.idEntry.configure(state="disabled")
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
        # Use OptionMenu for grade selection for consistency
        grade_values = [f"Grade {i}" for i in range(1, 13)]
        self.gradeEntry = c.CTkOptionMenu(self.ams_update_container, values=grade_values, font=("Montserrat Alternates", 16), width=600)
        self.gradeEntry.set(grade)
        self.gradeEntry.pack(padx=0, pady=10)

        def submit_update():
            new_full_name = self.nameEntry.get()
            new_sex = self.sexEntry.get()
            new_parent = self.parentEntry.get()
            new_occupation = self.occupationEntry.get()
            new_phone = self.phoneEntry.get()
            new_grade = self.gradeEntry.get()
            new_photo_path = getattr(self, "saved_photo_path", None)
            try:
                conn = sqlite3.connect("students.db")
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE students
                    SET full_name=?, sex=?, parent_name=?, occupation=?, phone=?, grade=?, photo_path=?
                    WHERE student_id=?
                """, (new_full_name, new_sex, new_parent, new_occupation, new_phone, new_grade, new_photo_path, student_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Student record updated successfully.")
                self.ams_update_container.destroy()
                self.filter_students()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update student: {e}")

        self.submit = c.CTkButton(self.ams_update_container, text="UPDATE", font=("Montserrat Alternates", 16), width=600, command=submit_update)
        self.submit.pack(padx=0, pady=10)
        self.cancel = c.CTkButton(self.ams_update_container, text="CLOSE", font=("Montserrat Alternates", 16), width=600, command=lambda: self.ams_update_container.destroy())
        self.cancel.pack(padx=0, pady=5)

    def report_popup(self):
        self.pop_window = c.CTkToplevel(self.ui)
        self.pop_window.geometry("500x380")
        self.pop_window.transient(self.ui)
        self.pop_window.grab_set()
        self.pop_window.title("Generate Report")
        self.pop_window.configure(fg_color="#f8fafc")
        # Title
        c.CTkLabel(
            self.pop_window,
            text="Generate Student Report",
            font=("Montserrat Alternates", 20, "bold"),
            text_color="#26658C",
            fg_color="#f8fafc"
        ).pack(pady=(18, 8))
        # Grade selection
        grades = ["Grade"] + [f"Grade {i}" for i in range(1, 13)]
        self.gradeAccess = c.CTkOptionMenu(
            self.pop_window,
            values=grades,
            width=340,
            font=("Montserrat Alternates", 16),
            fg_color="#26658C",
            button_color="#54ACBF",
            dropdown_fg_color="#f8fafc",
            dropdown_text_color="#26658C"
        )
        self.gradeAccess.pack(padx=10, pady=(10, 8))
        # Subject selection
        self.subjects_by_grade = {
            f"Grade {i}": ["Mathematics", "Science", "English", "Social Studies", "ICT"] for i in range(1, 7)
        }
        self.subjects_by_grade.update({
            f"Grade {i}": ["Mathematics", "Science", "Pre Algebra", "Bible", "English", "Social Studies", "ICT"] for i in range(7, 13)
        })
        self.subject_var = tk.StringVar(value="Subject")
        self.subject_menu = c.CTkOptionMenu(
            self.pop_window,
            variable=self.subject_var,
            values=["Subject"],
            width=340,
            font=("Montserrat Alternates", 16),
            fg_color="#26658C",
            button_color="#54ACBF",
            dropdown_fg_color="#f8fafc",
            dropdown_text_color="#26658C"
        )
        self.subject_menu.pack(padx=10, pady=(8, 18))
        # Update subject list when grade changes
        def update_subjects(*args):
            grade = self.gradeAccess.get()
            subjects = self.subjects_by_grade.get(grade, ["Subject"])
            self.subject_menu.configure(values=subjects)
            if subjects:
                self.subject_var.set(subjects[0])
            else:
                self.subject_var.set("Subject")
        self.gradeAccess.configure(command=lambda _: update_subjects())
        # Submit button
        self.subbtn = c.CTkButton(
            self.pop_window,
            text="Continue",
            width=340,
            font=("Montserrat Alternates", 16, "bold"),
            fg_color="#54ACBF",
            hover_color="#26658C",
            text_color="#fff",
            corner_radius=8,
            command=self.Report
        )
        self.subbtn.pack(padx=10, pady=(10, 18))

    def Report(self):
        grade = self.gradeAccess.get()
        subject = self.subject_var.get()
        self.pop_window.destroy()
        # Main container
        self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
        self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
        self.ams_parent_container.rowconfigure(0, weight=0)
        self.ams_parent_container.rowconfigure(1, weight=1)
        self.ams_parent_container.columnconfigure(0, weight=1)
        # ID entry frame
        self.report_id_frame = c.CTkFrame(self.ams_parent_container, fg_color="#f8fafc")
        self.report_id_frame.grid(row=0, column=0, pady=20, padx=20, sticky="ew")
        self.report_id_frame.columnconfigure(0, weight=0)
        self.report_id_frame.columnconfigure(1, weight=1)
        self.report_id_frame.columnconfigure(2, weight=0)
        self.report_id_label = c.CTkLabel(
            self.report_id_frame,
            text="Enter Student ID:",
            font=("Montserrat Alternates", 16, "bold"),
            text_color="#26658C"
        )
        self.report_id_label.grid(row=0, column=0, padx=(10, 5), pady=8, sticky="w")
        self.report_id_entry = c.CTkEntry(
            self.report_id_frame,
            placeholder_text="Student ID",
            font=("Montserrat Alternates", 16),
            width=200,
            fg_color="#fff"
        )
        self.report_id_entry.grid(row=0, column=1, padx=5, pady=8, sticky="ew")
        self.report_id_btn = c.CTkButton(
            self.report_id_frame,
            text="Load Student",
            font=("Montserrat Alternates", 16, "bold"),
            fg_color="#54ACBF",
            hover_color="#26658C",
            text_color="#fff",
            command=lambda: self.load_student_for_report(grade, subject)
        )
        self.report_id_btn.grid(row=0, column=2, padx=(5, 10), pady=8, sticky="e")

    def load_student_for_report(self, grade, subject):
        student_id = self.report_id_entry.get().strip()
        if not student_id:
            messagebox.showwarning("Input Error", "Please enter a Student ID.")
            return
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, grade FROM students WHERE student_id = ?", (student_id,))
        result = cursor.fetchone()
        conn.close()
        if not result:
            messagebox.showerror("Not Found", f"No student found with ID: {student_id}")
            return
        full_name, student_grade = result
        if hasattr(self, "report_sheet_frame"):
            self.report_sheet_frame.destroy()
        self.report_sheet_frame = c.CTkFrame(self.ams_parent_container, fg_color="#FFFFFF", border_color="#54ACBF", border_width=2, corner_radius=12)
        self.report_sheet_frame.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")
        self.ams_parent_container.rowconfigure(1, weight=1)
        # Student info
        info_text = f"Student: {full_name} (ID: {student_id})   Grade: {student_grade}   Subject: {subject}"
        self.student_info_label = c.CTkLabel(
            self.report_sheet_frame,
            text=info_text,
            font=("Montserrat Alternates", 16, "bold"),
            text_color="#26658C"
        )
        self.student_info_label.pack(pady=(18, 10))
        # Entry fields
        self.result_entries = {}
        entry_frame = c.CTkFrame(self.report_sheet_frame, fg_color="#f8fafc")
        entry_frame.pack(pady=10)
        test_types = ["Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam"]
        for ttype in test_types:
            row = c.CTkFrame(entry_frame, fg_color="#f8fafc")
            row.pack(fill="x", pady=2)
            label = c.CTkLabel(row, text=ttype + ":", font=("Montserrat Alternates", 14), width=120, anchor="w")
            label.pack(side="left", padx=(0, 8))
            entry = c.CTkEntry(row, placeholder_text=f"{ttype}", font=("Montserrat Alternates", 14), width=220, fg_color="#fff")
            entry.pack(side="left", padx=0)
            self.result_entries[ttype] = entry
        # Comment
        self.comment_label = c.CTkLabel(
            self.report_sheet_frame,
            text="Teacher's Comment:",
            font=("Montserrat Alternates", 14, "bold"),
            text_color="#26658C"
        )
        self.comment_label.pack(pady=(20, 5))
        self.comment_entry = c.CTkEntry(
            self.report_sheet_frame,
            placeholder_text="Enter comments...",
            font=("Montserrat Alternates", 14),
            width=400,
            fg_color="#fff"
        )
        self.comment_entry.pack(pady=5)
        # Buttons
        btn_row = c.CTkFrame(self.report_sheet_frame, fg_color="#FFFFFF")
        btn_row.pack(pady=18)
        self.save_report_btn = c.CTkButton(
            btn_row,
            text="Save Results",
            font=("Montserrat Alternates", 16, "bold"),
            fg_color="#54ACBF",
            hover_color="#26658C",
            text_color="#fff",
            width=180,
            corner_radius=8,
            command=lambda: self.save_student_results(student_id, subject)
        )
        self.save_report_btn.pack(side="left", padx=10)
        self.print_report_btn = c.CTkButton(
            btn_row,
            text="Show Report Card",
            font=("Montserrat Alternates", 16, "bold"),
            fg_color="#26658C",
            hover_color="#54ACBF",
            text_color="#fff",
            width=180,
            corner_radius=8,
            command=lambda: self.show_report_card_ctk(student_id)
        )
        self.print_report_btn.pack(side="left", padx=10)

    def save_student_results(self, student_id, subject):
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
                continue
            try:
                score = float(value)
            except ValueError:
                messagebox.showwarning("Input Error", f"Score for {subject} {ttype} must be a number.")
                return
            cursor.execute("DELETE FROM results WHERE student_id = ? AND subject = ? AND test_type = ?", (student_id, subject, ttype))
            cursor.execute(
                "INSERT INTO results (student_id, subject, test_type, score, comment) VALUES (?, ?, ?, ?, ?)",
                (student_id, subject, ttype, score, comment)
            )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Results saved successfully!")
        self.report_sheet_frame.destroy()

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
        subjects = defaultdict(dict)
        for subject, test_type, score in results:
            subjects[subject][test_type] = score

        popup = c.CTkToplevel(self.ui)
        popup.title("Report Card")
        popup.geometry("700x540")
        popup.grab_set()
        popup.configure(fg_color="#f8fafc")
        # Header
        header = c.CTkLabel(
            popup,
            text=f"Report Card for {full_name} (ID: {student_id})",
            font=("Montserrat Alternates", 20, "bold"),
            text_color="#26658C",
            fg_color="#f8fafc"
        )
        header.pack(pady=(18, 4))
        grade_label = c.CTkLabel(
            popup,
            text=f"Grade: {grade}",
            font=("Montserrat Alternates", 16, "bold"),
            text_color="#54ACBF",
            fg_color="#f8fafc"
        )
        grade_label.pack(pady=(0, 12))
        # Table
        table_frame = c.CTkScrollableFrame(popup, fg_color="#FFFFFF", border_color="#54ACBF", border_width=2, corner_radius=12, width=620, height=340)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)
        headers = ["Subject", "Quiz Avg", "Project Avg", "Exam Avg", "Total"]
        for col, h in enumerate(headers):
            lbl = c.CTkLabel(
                table_frame,
                text=h,
                font=("Montserrat Alternates", 14, "bold"),
                width=100,
                fg_color="#26658C",
                text_color="#fff",
                corner_radius=6
            )
            lbl.grid(row=0, column=col, padx=2, pady=2, sticky="nsew")
            table_frame.grid_columnconfigure(col, weight=1)
        for row, (subject, tests) in enumerate(subjects.items(), start=1):
            # Gather scores
            quiz_scores = [tests.get(q) for q in ["Quiz 1", "Quiz 2", "Quiz 3"] if isinstance(tests.get(q), (int, float, float))]
            project_scores = [tests.get(p) for p in ["Project 1", "Project 2"] if isinstance(tests.get(p), (int, float, float))]
            exam_scores = [tests.get("Exam")] if isinstance(tests.get("Exam"), (int, float, float)) else []
            quiz_avg = round(statistics.mean(quiz_scores), 2) if quiz_scores else "-"
            project_avg = round(statistics.mean(project_scores), 2) if project_scores else "-"
            exam_avg = round(statistics.mean(exam_scores), 2) if exam_scores else "-"
            total = 0
            for val in [quiz_avg, project_avg, exam_avg]:
                if isinstance(val, (int, float)):
                    total += val
            c.CTkLabel(
                table_frame,
                text=subject,
                font=("Montserrat Alternates", 13, "bold"),
                width=100,
                fg_color="#f8fafc",
                text_color="#26658C"
            ).grid(row=row, column=0, padx=2, pady=2, sticky="nsew")
            c.CTkLabel(
                table_frame,
                text=str(quiz_avg),
                font=("Montserrat Alternates", 13),
                width=100,
                fg_color="#fff",
                text_color="#22223b"
            ).grid(row=row, column=1, padx=2, pady=2, sticky="nsew")
            c.CTkLabel(
                table_frame,
                text=str(project_avg),
                font=("Montserrat Alternates", 13),
                width=100,
                fg_color="#e3e9f7",
                text_color="#22223b"
            ).grid(row=row, column=2, padx=2, pady=2, sticky="nsew")
            c.CTkLabel(
                table_frame,
                text=str(exam_avg),
                font=("Montserrat Alternates", 13),
                width=100,
                fg_color="#fff",
                text_color="#22223b"
            ).grid(row=row, column=3, padx=2, pady=2, sticky="nsew")
            c.CTkLabel(
                table_frame,
                text=str(round(total, 2)) if isinstance(total, (int, float)) else "-",
                font=("Montserrat Alternates", 13, "bold"),
                width=100,
                fg_color="#54ACBF",
                text_color="#fff"
            ).grid(row=row, column=4, padx=2, pady=2, sticky="nsew")
        # Close button
        close_btn = c.CTkButton(
            popup,
            text="Close",
            command=popup.destroy,
            fg_color="#26658C",
            hover_color="#54ACBF",
            text_color="#fff",
            font=("Montserrat Alternates", 15, "bold"),
            width=120,
            corner_radius=8
        )
        close_btn.pack(pady=18)
    # def show_report_card(self):
    #     self.ams_parent_container = c.CTkFrame(self.parent_widget, fg_color="#F5F5F5")
    #     self.ams_parent_container.grid(row=1, column=1, sticky="nsew")
    #     table_frame = c.CTkFrame(self.ams_parent_container, fg_color="#FFFFFF", border_color="#3c507d", border_width=2)
    #     table_frame.grid(row=0, column=0, columnspan=3, padx=30, pady=20, sticky="nsew")
    #     columns = ["Student ID", "Name", "Subject", "Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam", "Total"]
    #     tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=18)
    #     for col in columns:
    #         tree.heading(col, text=col)
    #         tree.column(col, width=100, anchor="center")
    #     style = ttk.Style()
    #     style.theme_use("default")
    #     style.configure("Treeview", background="#f0f0f0", foreground="black", rowheight=28, fieldbackground="#FFFFFF", font=("Montserrat Alternates", 12))
    #     style.configure("Treeview.Heading", font=("Montserrat Alternates", 13, "bold"))
    #     tree.pack(fill="both", expand=True, padx=5, pady=5)
    #     conn = sqlite3.connect("students.db")
    #     cursor = conn.cursor()
    #     cursor.execute("""
    #         SELECT s.student_id, s.full_name, r.subject, r.test_type, r.score
    #         FROM students s
    #         JOIN results r ON s.student_id = r.student_id
    #         ORDER BY s.student_id, r.subject, r.test_type
    #     """)
    #     rows = cursor.fetchall()
    #     conn.close()
    #     data = defaultdict(lambda: defaultdict(dict))
    #     for student_id, name, subject, test_type, score in rows:
    #         data[(student_id, name, subject)][test_type] = score
    #     test_types = ["Quiz 1", "Quiz 2", "Quiz 3", "Project 1", "Project 2", "Exam"]
    #     for (student_id, name, subject), scores in data.items():
    #         row_data = [student_id, name, subject]
    #         total = 0
    #         for ttype in test_types:
    #             score = scores.get(ttype, "-")
    #             row_data.append(score)
    #             if isinstance(score, (int, float)):
    #                 total += score
    #         row_data.append(total)
    #         tree.insert("", "end", values=row_data)
    #     close_btn = c.CTkButton(self.ams_parent_container, text="Close", command=self.ams_parent_container.destroy, fg_color="#3c507d")
    #     close_btn.grid(row=2, column=1, pady=10)
       

if __name__ == '__main__':
    systemWindow = c.CTk()
    classObject = AgapeSystem(systemWindow)
    systemWindow.mainloop()
