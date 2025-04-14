import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from configuration import DatabaseManager

class BankManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Initialize database
        try:
            self.db = DatabaseManager()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")
            root.destroy()
            return

        # Current selection tracking
        self.current_branch_id = None
        self.current_employee_id = None
        self.current_customer_id = None

        # Configure styles
        self._configure_styles()
        
        # Create login tabs interface
        self._create_login_tabs()

    def _configure_styles(self):
        """Configure widget styles and colors"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Color scheme
        self.bg_color = '#F0F8FF'  # Alice Blue
        self.primary_color = '#4682B4'  # Steel Blue
        self.secondary_color = '#5F9EA0'  # Cadet Blue
        self.highlight_color = '#B0E0E6'  # Powder Blue
        
        # Configure styles
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabel', background=self.bg_color, font=('Helvetica', 10))
        self.style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=5)
        self.style.configure('Treeview', font=('Helvetica', 9), rowheight=25, 
                           fieldbackground=self.bg_color)
        self.style.configure('Treeview.Heading', font=('Helvetica', 10, 'bold'))
        self.style.map('Treeview', 
                      background=[('selected', self.primary_color)],
                      foreground=[('selected', 'white')])
        self.style.configure('TLabelframe', background=self.bg_color)
        self.style.configure('TLabelframe.Label', background=self.bg_color)

    def _create_login_tabs(self):
        """Create login interface with role selection tabs"""
        self.login_notebook = ttk.Notebook(self.root)
        self.login_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs for each role
        self._create_admin_login_tab()
        self._create_employee_login_tab()
        self._create_customer_login_tab()

    def _create_admin_login_tab(self):
        """Admin login tab"""
        admin_tab = ttk.Frame(self.login_notebook)
        self.login_notebook.add(admin_tab, text="Admin")
        
        # Admin tab content
        content_frame = ttk.Frame(admin_tab)
        content_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        
        ttk.Label(content_frame, text="Admin Panel", font=('Helvetica', 16, 'bold')).pack(pady=20)
        ttk.Label(content_frame, text="Full access to all management functions").pack(pady=10)
        
        ttk.Button(content_frame, text="Enter Admin Dashboard", command=self._show_admin_interface,
                  style='Primary.TButton').pack(pady=20)

    def _create_employee_login_tab(self):
        """Employee login tab"""
        employee_tab = ttk.Frame(self.login_notebook)
        self.login_notebook.add(employee_tab, text="Employee")
        
        # Employee tab content
        content_frame = ttk.Frame(employee_tab)
        content_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        
        ttk.Label(content_frame, text="Employee Panel", font=('Helvetica', 16, 'bold')).pack(pady=20)
        ttk.Label(content_frame, text="Access to employee and customer management").pack(pady=10)
        
        ttk.Button(content_frame, text="Enter Employee Dashboard", command=self._show_employee_interface,
                  style='Primary.TButton').pack(pady=20)

    def _create_customer_login_tab(self):
        """Customer login tab"""
        customer_tab = ttk.Frame(self.login_notebook)
        self.login_notebook.add(customer_tab, text="Customer")
        
        # Customer tab content
        content_frame = ttk.Frame(customer_tab)
        content_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        
        ttk.Label(content_frame, text="Customer Panel", font=('Helvetica', 16, 'bold')).pack(pady=20)
        ttk.Label(content_frame, text="Access to customer management only").pack(pady=10)
        
        ttk.Button(content_frame, text="Enter Customer Dashboard", command=self._show_customer_interface,
                  style='Primary.TButton').pack(pady=20)

    def _show_admin_interface(self):
        """Switch to admin interface"""
        self.login_notebook.destroy()
        self._setup_interface("admin")

    def _show_employee_interface(self):
        """Switch to employee interface"""
        self.login_notebook.destroy()
        self._setup_interface("employee")

    def _show_customer_interface(self):
        """Switch to customer interface"""
        self.login_notebook.destroy()
        self._setup_interface("customer")

    def _setup_interface(self, role):
        """Create the main interface components"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs based on role
        if role == "admin":
            self._create_branch_tab()
            self._create_employee_tab()
            self._create_customer_tab()
            self.notebook.select(0)  # Select first tab
        elif role == "employee":
            self._create_employee_tab()
            self._create_customer_tab()
            self.notebook.select(0)  # Select first tab
        elif role == "customer":
            self._create_customer_tab()

    # ======================
    # BRANCH TAB IMPLEMENTATION
    # ======================
    def _create_branch_tab(self):
        """Create branch management tab"""
        self.branch_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.branch_tab, text="Branch Management")
        
        # Main container
        main_frame = ttk.Frame(self.branch_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Form frame
        form_frame = ttk.LabelFrame(main_frame, text="Branch Details")
        form_frame.pack(fill=tk.X, pady=5)
        
        # Form fields
        fields = ["Name:", "Address:", "City:", "State:", "PIN Code:"]
        self.branch_entries = []
        for i, field in enumerate(fields):
            ttk.Label(form_frame, text=field).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = ttk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=3)
            self.branch_entries.append(entry)

        # Form buttons (Save and Clear)
        form_btn_frame = ttk.Frame(form_frame)
        form_btn_frame.grid(row=len(fields), columnspan=2, pady=10)
        
        ttk.Button(form_btn_frame, text="Save", command=self._update_branch, 
                  style='Primary.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(form_btn_frame, text="Clear", command=self._new_branch).pack(side=tk.LEFT, padx=5)

        # Treeview frame
        tree_frame = ttk.LabelFrame(main_frame, text="Branch List")
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Treeview
        columns = ("ID", "Name", "Address", "City", "State", "PIN Code")
        self.branch_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode='browse')
        
        for col in columns:
            self.branch_tree.heading(col, text=col)
            self.branch_tree.column(col, width=120, anchor=tk.CENTER)
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.branch_tree.yview)
        x_scroll = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.branch_tree.xview)
        self.branch_tree.configure(yscroll=y_scroll.set, xscroll=x_scroll.set)
        
        # Layout
        self.branch_tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Treeview buttons (New, Update, Delete)
        tree_btn_frame = ttk.Frame(tree_frame)
        tree_btn_frame.grid(row=2, columnspan=2, pady=5)
        
        ttk.Button(tree_btn_frame, text="New", command=self._new_branch).pack(side=tk.LEFT, padx=5)
        ttk.Button(tree_btn_frame, text="Update", command=self._update_branch, 
                  style='Primary.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(tree_btn_frame, text="Delete", command=self._delete_branch, 
                  style='Danger.TButton').pack(side=tk.LEFT, padx=5)

        # Search frame (at bottom)
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(search_frame, text="Search Branch:").pack(side=tk.LEFT, padx=5)
        self.branch_search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.branch_search_var, width=40)
        search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Search", command=self._search_branches).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Clear", command=self._clear_branch_search).pack(side=tk.LEFT)
        
        # Bind Enter key to search
        search_entry.bind('<Return>', lambda e: self._search_branches())
        
        # Bind selection event
        self.branch_tree.bind("<<TreeviewSelect>>", self._on_branch_select)
        
        # Load initial data
        self._load_branches()

    def _load_branches(self):
        """Load branches into treeview"""
        for item in self.branch_tree.get_children():
            self.branch_tree.delete(item)
        
        try:
            branches = self.db.get_all_branches()
            for branch in branches:
                self.branch_tree.insert("", tk.END, values=(
                    branch["branch_id"],
                    branch["branch_name"],
                    branch["branch_address"],
                    branch["branch_city"],
                    branch["branch_state"],
                    branch["branch_zip"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load branches: {str(e)}")

    def _search_branches(self):
        """Search branches by name, city or state"""
        search_term = self.branch_search_var.get().strip()
        if not search_term:
            self._load_branches()
            return
        
        try:
            for item in self.branch_tree.get_children():
                self.branch_tree.delete(item)
            
            branches = self.db.search_branches(search_term)
            for branch in branches:
                self.branch_tree.insert("", tk.END, values=(
                    branch["branch_id"],
                    branch["branch_name"],
                    branch["branch_address"],
                    branch["branch_city"],
                    branch["branch_state"],
                    branch["branch_zip"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")

    def _clear_branch_search(self):
        """Clear search results"""
        self.branch_search_var.set("")
        self._load_branches()

    def _on_branch_select(self, event):
        """Handle branch selection in treeview"""
        selected_items = self.branch_tree.selection()
        if not selected_items:
            return
        
        selected_item = selected_items[0]
        branch_id = self.branch_tree.item(selected_item)["values"][0]
        
        try:
            branch = self.db.get_branch_by_id(branch_id)
            if branch:
                self.current_branch_id = branch["branch_id"]
                # Update form fields
                for i, field in enumerate(["branch_name", "branch_address", 
                                          "branch_city", "branch_state", "branch_zip"]):
                    self.branch_entries[i].delete(0, tk.END)
                    self.branch_entries[i].insert(0, branch[field])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load branch details: {str(e)}")

    def _update_branch(self):
        """Update selected branch"""
        if not hasattr(self, 'current_branch_id') or not self.current_branch_id:
            messagebox.showwarning("Warning", "Please select a branch to update")
            return
        
        data = [entry.get().strip() for entry in self.branch_entries]
        if not all(data):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            success = self.db.update_branch(
                self.current_branch_id,
                data[0],  # name
                data[1],  # address
                data[2],  # city
                data[3],  # state
                data[4]   # zip
            )
            if success:
                messagebox.showinfo("Success", "Branch updated successfully")
                self._load_branches()
            else:
                messagebox.showerror("Error", "Failed to update branch")
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {str(e)}")

    def _new_branch(self):
        """Clear form for new branch entry"""
        self.current_branch_id = None
        for entry in self.branch_entries:
            entry.delete(0, tk.END)

    def _delete_branch(self):
        """Delete selected branch"""
        selected_items = self.branch_tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a branch to delete")
            return
        
        selected_item = selected_items[0]
        branch_id = self.branch_tree.item(selected_item)["values"][0]
        branch_name = self.branch_tree.item(selected_item)["values"][1]
        
        if messagebox.askyesno("Confirm", f"Delete branch '{branch_name}'?"):
            try:
                if self.db.delete_branch(branch_id):
                    messagebox.showinfo("Success", "Branch deleted")
                    self._load_branches()
                    self._new_branch()  # Clear form
                else:
                    messagebox.showerror("Error", "Failed to delete branch")
            except Exception as e:
                messagebox.showerror("Error", f"Delete failed: {str(e)}")

    # ======================
    # EMPLOYEE TAB IMPLEMENTATION
    # ======================
    def _create_employee_tab(self):
        """Create employee management tab"""
        self.employee_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.employee_tab, text="Employee Management")
        
        # Main container
        main_frame = ttk.Frame(self.employee_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Form frame
        form_frame = ttk.LabelFrame(main_frame, text="Employee Details")
        form_frame.pack(fill=tk.X, pady=5)
        
        # Form fields
        fields = [
            "Name:", 
            "Date of Birth (YYYY-MM-DD):", 
            "Phone:", 
            "Email:", 
            "Position:", 
            "Branch ID:"
        ]
        self.employee_entries = []
        for i, field in enumerate(fields):
            ttk.Label(form_frame, text=field).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = ttk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=3)
            self.employee_entries.append(entry)

        # Form buttons (Save and Clear)
        form_btn_frame = ttk.Frame(form_frame)
        form_btn_frame.grid(row=len(fields), columnspan=2, pady=10)
        
        ttk.Button(form_btn_frame, text="Save", command=self._update_employee, 
                  style='Primary.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(form_btn_frame, text="Clear", command=self._new_employee).pack(side=tk.LEFT, padx=5)

        # Treeview frame
        tree_frame = ttk.LabelFrame(main_frame, text="Employee List")
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Treeview
        columns = ("ID", "Name", "DOB", "Phone", "Email", "Position", "Branch ID")
        self.employee_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode='browse')
        
        for col in columns:
            self.employee_tree.heading(col, text=col)
            self.employee_tree.column(col, width=120, anchor=tk.CENTER)
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.employee_tree.yview)
        x_scroll = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.employee_tree.xview)
        self.employee_tree.configure(yscroll=y_scroll.set, xscroll=x_scroll.set)
        
        # Layout
        self.employee_tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Treeview buttons (New, Update, Delete)
        tree_btn_frame = ttk.Frame(tree_frame)
        tree_btn_frame.grid(row=2, columnspan=2, pady=5)
        
        ttk.Button(tree_btn_frame, text="New", command=self._new_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(tree_btn_frame, text="Update", command=self._update_employee, 
                  style='Primary.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(tree_btn_frame, text="Delete", command=self._delete_employee, 
                  style='Danger.TButton').pack(side=tk.LEFT, padx=5)

        # Search frame (at bottom)
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(search_frame, text="Search Employee:").pack(side=tk.LEFT, padx=5)
        self.employee_search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.employee_search_var, width=40)
        search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Search", command=self._search_employees).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Clear", command=self._clear_employee_search).pack(side=tk.LEFT)
        
        # Bind Enter key to search
        search_entry.bind('<Return>', lambda e: self._search_employees())
        
        # Bind selection event
        self.employee_tree.bind("<<TreeviewSelect>>", self._on_employee_select)
        
        # Load initial data
        self._load_employees()

    def _load_employees(self):
        """Load employees into treeview"""
        for item in self.employee_tree.get_children():
            self.employee_tree.delete(item)
        
        try:
            employees = self.db.get_all_employees()
            for emp in employees:
                self.employee_tree.insert("", tk.END, values=(
                    emp["emp_id"],
                    emp["emp_name"],
                    emp["emp_dob"],
                    emp["emp_phone"],
                    emp["emp_email"],
                    emp["emp_position"],
                    emp["branch_id"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load employees: {str(e)}")

    def _search_employees(self):
        """Search employees by name, email or position"""
        search_term = self.employee_search_var.get().strip()
        if not search_term:
            self._load_employees()
            return
        
        try:
            for item in self.employee_tree.get_children():
                self.employee_tree.delete(item)
            
            employees = self.db.search_employees(search_term)
            for emp in employees:
                self.employee_tree.insert("", tk.END, values=(
                    emp["emp_id"],
                    emp["emp_name"],
                    emp["emp_dob"],
                    emp["emp_phone"],
                    emp["emp_email"],
                    emp["emp_position"],
                    emp["branch_id"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")

    def _clear_employee_search(self):
        """Clear employee search results"""
        self.employee_search_var.set("")
        self._load_employees()

    def _on_employee_select(self, event):
        """Handle employee selection in treeview"""
        selected_items = self.employee_tree.selection()
        if not selected_items:
            return
        
        selected_item = selected_items[0]
        emp_id = self.employee_tree.item(selected_item)["values"][0]
        
        try:
            employee = self.db.get_employee_by_id(emp_id)
            if employee:
                self.current_employee_id = employee["emp_id"]
                # Update form fields
                for i, field in enumerate(["emp_name", "emp_dob", "emp_phone", 
                                          "emp_email", "emp_position", "branch_id"]):
                    self.employee_entries[i].delete(0, tk.END)
                    self.employee_entries[i].insert(0, employee[field])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load employee details: {str(e)}")

    def _update_employee(self):
        """Update selected employee"""
        if not hasattr(self, 'current_employee_id') or not self.current_employee_id:
            messagebox.showwarning("Warning", "Please select an employee to update")
            return
        
        data = [entry.get().strip() for entry in self.employee_entries]
        if not all(data):
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Validate date format
        try:
            datetime.strptime(data[1], "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return
        
        try:
            success = self.db.update_employee(
                self.current_employee_id,
                data[0],  # name
                data[1],  # dob
                data[2],  # phone
                data[3],  # email
                data[4],  # position
                data[5]   # branch_id
            )
            if success:
                messagebox.showinfo("Success", "Employee updated successfully")
                self._load_employees()
            else:
                messagebox.showerror("Error", "Failed to update employee")
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {str(e)}")

    def _new_employee(self):
        """Clear form for new employee entry"""
        self.current_employee_id = None
        for entry in self.employee_entries:
            entry.delete(0, tk.END)

    def _delete_employee(self):
        """Delete selected employee"""
        selected_items = self.employee_tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select an employee to delete")
            return
        
        selected_item = selected_items[0]
        emp_id = self.employee_tree.item(selected_item)["values"][0]
        emp_name = self.employee_tree.item(selected_item)["values"][1]
        
        if messagebox.askyesno("Confirm", f"Delete employee '{emp_name}'?"):
            try:
                if self.db.delete_employee(emp_id):
                    messagebox.showinfo("Success", "Employee deleted")
                    self._load_employees()
                    self._new_employee()  # Clear form
                else:
                    messagebox.showerror("Error", "Failed to delete employee")
            except Exception as e:
                messagebox.showerror("Error", f"Delete failed: {str(e)}")

    # ======================
    # CUSTOMER TAB IMPLEMENTATION
    # ======================
    def _create_customer_tab(self):
        """Create customer management tab"""
        self.customer_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_tab, text="Customer Management")
        
        # Main container
        main_frame = ttk.Frame(self.customer_tab)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Form frame
        form_frame = ttk.LabelFrame(main_frame, text="Customer Details")
        form_frame.pack(fill=tk.X, pady=5)
        
        # Form fields
        fields = [
            "Name:", 
            "Date of Birth (YYYY-MM-DD):", 
            "Phone:", 
            "Email:", 
            "Address:", 
            "Branch ID:"
        ]
        self.customer_entries = []
        for i, field in enumerate(fields):
            ttk.Label(form_frame, text=field).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = ttk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=3)
            self.customer_entries.append(entry)

        # Form buttons (Save and Clear)
        form_btn_frame = ttk.Frame(form_frame)
        form_btn_frame.grid(row=len(fields), columnspan=2, pady=10)
        
        ttk.Button(form_btn_frame, text="Save", command=self._update_customer, 
                  style='Primary.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(form_btn_frame, text="Clear", command=self._new_customer).pack(side=tk.LEFT, padx=5)

        # Treeview frame
        tree_frame = ttk.LabelFrame(main_frame, text="Customer List")
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Treeview
        columns = ("ID", "Name", "DOB", "Phone", "Email", "Address", "Branch ID")
        self.customer_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode='browse')
        
        for col in columns:
            self.customer_tree.heading(col, text=col)
            self.customer_tree.column(col, width=120, anchor=tk.CENTER)
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.customer_tree.yview)
        x_scroll = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.customer_tree.xview)
        self.customer_tree.configure(yscroll=y_scroll.set, xscroll=x_scroll.set)
        
        # Layout
        self.customer_tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Treeview buttons (New, Update, Delete)
        tree_btn_frame = ttk.Frame(tree_frame)
        tree_btn_frame.grid(row=2, columnspan=2, pady=5)
        
        ttk.Button(tree_btn_frame, text="New", command=self._new_customer).pack(side=tk.LEFT, padx=5)
        ttk.Button(tree_btn_frame, text="Update", command=self._update_customer, 
                  style='Primary.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(tree_btn_frame, text="Delete", command=self._delete_customer, 
                  style='Danger.TButton').pack(side=tk.LEFT, padx=5)

        # Search frame (at bottom)
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(search_frame, text="Search Customer:").pack(side=tk.LEFT, padx=5)
        self.customer_search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.customer_search_var, width=40)
        search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Search", command=self._search_customers).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Clear", command=self._clear_customer_search).pack(side=tk.LEFT)
        
        # Bind Enter key to search
        search_entry.bind('<Return>', lambda e: self._search_customers())
        
        # Bind selection event
        self.customer_tree.bind("<<TreeviewSelect>>", self._on_customer_select)
        
        # Load initial data
        self._load_customers()

    def _load_customers(self):
        """Load customers into treeview"""
        for item in self.customer_tree.get_children():
            self.customer_tree.delete(item)
        
        try:
            customers = self.db.get_all_customers()
            for cust in customers:
                self.customer_tree.insert("", tk.END, values=(
                    cust["cust_id"],
                    cust["name"],
                    cust["dob"],
                    cust["phone"],
                    cust["email"],
                    cust["address"],
                    cust["branch_id"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load customers: {str(e)}")

    def _search_customers(self):
        """Search customers by name, email or phone"""
        search_term = self.customer_search_var.get().strip()
        if not search_term:
            self._load_customers()
            return
        
        try:
            for item in self.customer_tree.get_children():
                self.customer_tree.delete(item)
            
            customers = self.db.search_customers(search_term)
            for cust in customers:
                self.customer_tree.insert("", tk.END, values=(
                    cust["cust_id"],
                    cust["name"],
                    cust["dob"],
                    cust["phone"],
                    cust["email"],
                    cust["address"],
                    cust["branch_id"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")

    def _clear_customer_search(self):
        """Clear customer search results"""
        self.customer_search_var.set("")
        self._load_customers()

    def _on_customer_select(self, event):
        """Handle customer selection in treeview"""
        selected_items = self.customer_tree.selection()
        if not selected_items:
            return
        
        selected_item = selected_items[0]
        cust_id = self.customer_tree.item(selected_item)["values"][0]
        
        try:
            customer = self.db.get_customer_by_id(cust_id)
            if customer:
                self.current_customer_id = customer["cust_id"]
                # Update form fields
                for i, field in enumerate(["name", "dob", "phone", 
                                          "email", "address", "branch_id"]):
                    self.customer_entries[i].delete(0, tk.END)
                    self.customer_entries[i].insert(0, customer[field])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load customer details: {str(e)}")

    def _update_customer(self):
        """Update selected customer"""
        if not hasattr(self, 'current_customer_id') or not self.current_customer_id:
            messagebox.showwarning("Warning", "Please select a customer to update")
            return
        
        data = [entry.get().strip() for entry in self.customer_entries]
        if not all(data):
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Validate date format
        try:
            datetime.strptime(data[1], "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return
        
        try:
            success = self.db.update_customer(
                self.current_customer_id,
                data[0],  # name
                data[1],  # dob
                data[2],  # phone
                data[3],  # email
                data[4],  # address
                data[5]   # branch_id
            )
            if success:
                messagebox.showinfo("Success", "Customer updated successfully")
                self._load_customers()
            else:
                messagebox.showerror("Error", "Failed to update customer")
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {str(e)}")

    def _new_customer(self):
        """Clear form for new customer entry"""
        self.current_customer_id = None
        for entry in self.customer_entries:
            entry.delete(0, tk.END)

    def _delete_customer(self):
        """Delete selected customer"""
        selected_items = self.customer_tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a customer to delete")
            return
        
        selected_item = selected_items[0]
        cust_id = self.customer_tree.item(selected_item)["values"][0]
        cust_name = self.customer_tree.item(selected_item)["values"][1]
        
        if messagebox.askyesno("Confirm", f"Delete customer '{cust_name}'?"):
            try:
                if self.db.delete_customer(cust_id):
                    messagebox.showinfo("Success", "Customer deleted")
                    self._load_customers()
                    self._new_customer()  # Clear form
                else:
                    messagebox.showerror("Error", "Failed to delete customer")
            except Exception as e:
                messagebox.showerror("Error", f"Delete failed: {str(e)}")

    import tkinter as tk
from tkinter import ttk, messagebox
from configuration import DatabaseManager
from datetime import datetime

class BankManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        self.root.configure(bg="#A3D1C6")

        # Initialize database connection
        try:
            self.db = DatabaseManager()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")
            root.destroy()
            return

        # Current user information
        self.current_user = None
        self.user_type = None

        # Setup the login interface
        self._setup_login_interface()

    def _setup_login_interface(self):
        """Create the login interface with admin, employee, and customer options"""
        self.clear_window()
        
        # Main frame
        login_frame = ttk.Frame(self.root, padding="30 15 30 15")
        login_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(login_frame, text="Bank Management System", 
                 font=("Helvetica", 20, "bold")).pack(pady=20)
        
        # Login options frame
        options_frame = ttk.Frame(login_frame)
        options_frame.pack(pady=30)
        
        # Buttons for each user type
        ttk.Button(options_frame, text="Admin Login", 
                  command=lambda: self._show_admin_interface(), 
                  width=20).pack(pady=10)
        
        ttk.Button(options_frame, text="Employee Login", 
                  command=lambda: self._show_employee_interface(), 
                  width=20).pack(pady=10)
        
        ttk.Button(options_frame, text="Customer Login", 
                  command=lambda: self._show_customer_interface(), 
                  width=20).pack(pady=10)

    def _show_admin_interface(self):
        """Show the admin interface with branch management"""
        self.user_type = "admin"
        self.clear_window()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Branch tab
        self.branch_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.branch_tab, text="Branch Management")
        
        # Create branch management interface
        self._create_branch_interface()
        
        # Back button
        back_button = ttk.Button(self.root, text="Logout", 
                                command=self._setup_login_interface)
        back_button.pack(pady=10)

    def _show_employee_interface(self):
        """Show the employee interface with employee management"""
        self.user_type = "employee"
        self.clear_window()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Employee tab
        self.employee_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.employee_tab, text="Employee Management")
        
        # Create employee management interface
        self._create_employee_interface()
        
        # Back button
        back_button = ttk.Button(self.root, text="Logout", 
                                command=self._setup_login_interface)
        back_button.pack(pady=10)

    def _show_customer_interface(self):
        """Show the customer interface with customer management"""
        self.user_type = "customer"
        self.clear_window()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Customer tab
        self.customer_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_tab, text="Customer Management")
        
        # Create customer management interface
        self._create_customer_interface()
        
        # Back button
        back_button = ttk.Button(self.root, text="Logout", 
                                command=self._setup_login_interface)
        back_button.pack(pady=10)

    def _create_branch_interface(self):
        """Create branch management interface in the branch tab"""
        # Form for branch details
        details_frame = ttk.LabelFrame(self.branch_tab, text="Branch Details", padding="10 5 10 10")
        details_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Labels and entries for branch attributes
        labels = ["Branch Name:", "Address:", "City:", "State:", "PIN Code:"]
        self.branch_entries = []
        
        for i, label_text in enumerate(labels):
            ttk.Label(details_frame, text=label_text).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = ttk.Entry(details_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=3)
            self.branch_entries.append(entry)
        
        # Buttons frame
        btn_frame = ttk.Frame(details_frame)
        btn_frame.grid(row=len(labels), columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Save", command=self._save_branch).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="New", command=self._new_branch).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self._delete_branch).pack(side=tk.LEFT, padx=5)
        
        # Branch list
        list_frame = ttk.LabelFrame(self.branch_tab, text="Branch List", padding="10 5 10 10")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Treeview for displaying branches
        columns = ("ID", "Name", "Address", "City", "State", "PIN Code")
        self.branch_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        for col in columns:
            self.branch_tree.heading(col, text=col)
            self.branch_tree.column(col, width=120, anchor=tk.CENTER)
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.branch_tree.yview)
        x_scroll = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=self.branch_tree.xview)
        self.branch_tree.configure(yscroll=y_scroll.set, xscroll=x_scroll.set)
        
        # Grid layout
        self.branch_tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # Bind selection event
        self.branch_tree.bind("<<TreeviewSelect>>", self._on_branch_select)
        
        # Load initial data
        self._load_branches()

    def _create_employee_interface(self):
        """Create employee management interface in the employee tab"""
        # Form for employee details
        details_frame = ttk.LabelFrame(self.employee_tab, text="Employee Details", padding="10 5 10 10")
        details_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Labels and entries for employee attributes
        labels = [
            "Name:", "Date of Birth (YYYY-MM-DD):", 
            "Phone:", "Email:", 
            "Position:", "Branch ID:"
        ]
        self.employee_entries = []
        
        for i, label_text in enumerate(labels):
            ttk.Label(details_frame, text=label_text).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = ttk.Entry(details_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=3)
            self.employee_entries.append(entry)
        
        # Buttons frame
        btn_frame = ttk.Frame(details_frame)
        btn_frame.grid(row=len(labels), columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Save", command=self._save_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="New", command=self._new_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self._delete_employee).pack(side=tk.LEFT, padx=5)
        
        # Employee list
        list_frame = ttk.LabelFrame(self.employee_tab, text="Employee List", padding="10 5 10 10")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Treeview for displaying employees
        columns = ("ID", "Name", "DOB", "Phone", "Email", "Position", "Branch ID", "Branch Name")
        self.employee_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        for col in columns:
            self.employee_tree.heading(col, text=col)
            self.employee_tree.column(col, width=120, anchor=tk.CENTER)
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.employee_tree.yview)
        x_scroll = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=self.employee_tree.xview)
        self.employee_tree.configure(yscroll=y_scroll.set, xscroll=x_scroll.set)
        
        # Grid layout
        self.employee_tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # Bind selection event
        self.employee_tree.bind("<<TreeviewSelect>>", self._on_employee_select)
        
        # Load initial data
        self._load_employees()

    def _create_customer_interface(self):
        """Create customer management interface in the customer tab"""
        # Form for customer details
        details_frame = ttk.LabelFrame(self.customer_tab, text="Customer Details", padding="10 5 10 10")
        details_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Labels and entries for customer attributes
        labels = [
            "Name:", "Date of Birth (YYYY-MM-DD):", 
            "Phone:", "Email:", 
            "Address:", "Branch ID:"
        ]
        self.customer_entries = []
        
        for i, label_text in enumerate(labels):
            ttk.Label(details_frame, text=label_text).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = ttk.Entry(details_frame, width=40)
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=3)
            self.customer_entries.append(entry)
        
        # Buttons frame
        btn_frame = ttk.Frame(details_frame)
        btn_frame.grid(row=len(labels), columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Save", command=self._save_customer).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="New", command=self._new_customer).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self._delete_customer).pack(side=tk.LEFT, padx=5)
        
        # Customer list
        list_frame = ttk.LabelFrame(self.customer_tab, text="Customer List", padding="10 5 10 10")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Treeview for displaying customers
        columns = ("ID", "Name", "DOB", "Phone", "Email", "Address", "Branch ID", "Branch Name")
        self.customer_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        for col in columns:
            self.customer_tree.heading(col, text=col)
            self.customer_tree.column(col, width=120, anchor=tk.CENTER)
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.customer_tree.yview)
        x_scroll = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=self.customer_tree.xview)
        self.customer_tree.configure(yscroll=y_scroll.set, xscroll=x_scroll.set)
        
        # Grid layout
        self.customer_tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # Bind selection event
        self.customer_tree.bind("<<TreeviewSelect>>", self._on_customer_select)
        
        # Load initial data
        self._load_customers()

    # ======================
    # BRANCH METHODS
    # ======================
    
    def _load_branches(self):
        """Load branches from database into the treeview"""
        for item in self.branch_tree.get_children():
            self.branch_tree.delete(item)
        
        try:
            branches = self.db.get_all_branches()
            for branch in branches:
                self.branch_tree.insert("", tk.END, values=(
                    branch["branch_id"],
                    branch["branch_name"],
                    branch["branch_address"],
                    branch["branch_city"],
                    branch["branch_state"],
                    branch["branch_zip"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load branches: {str(e)}")

    def _save_branch(self):
        """Save branch details to database"""
        data = [entry.get().strip() for entry in self.branch_entries]
        
        # Validate all fields are filled
        if not all(data):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            if hasattr(self, 'current_branch_id') and self.current_branch_id:
                # Update existing branch
                success = self.db.update_branch(
                    self.current_branch_id, 
                    data[0], data[1], data[2], data[3], data[4]
                )
                if success:
                    messagebox.showinfo("Success", "Branch updated successfully")
                else:
                    messagebox.showerror("Error", "Failed to update branch")
            else:
                # Create new branch
                branch_id = self.db.insert_branch(
                    data[0], data[1], data[2], data[3], data[4]
                )
                if branch_id:
                    messagebox.showinfo("Success", "Branch added successfully")
                    self.current_branch_id = branch_id
                else:
                    messagebox.showerror("Error", "Failed to add branch")
            
            # Refresh the branch list and clear form
            self._load_branches()
            self._clear_branch_fields()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def _new_branch(self):
        """Clear the form for a new branch"""
        self.current_branch_id = None
        self._clear_branch_fields()

    def _delete_branch(self):
        """Delete the selected branch"""
        selected_items = self.branch_tree.selection()
        if not selected_items:
            messagebox.showinfo("Information", "Please select a branch to delete")
            return
        
        selected_item = selected_items[0]
        branch_id = self.branch_tree.item(selected_item)["values"][0]
        branch_name = self.branch_tree.item(selected_item)["values"][1]
        
        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Deletion", 
            f"Are you sure you want to delete branch '{branch_name}'?"
        )
        if not confirm:
            return
        
        try:
            success = self.db.delete_branch(branch_id)
            if success:
                messagebox.showinfo("Success", "Branch deleted successfully")
                self._clear_branch_fields()
                self._load_branches()
            else:
                messagebox.showerror("Error", "Failed to delete branch")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete branch: {str(e)}")

    def _on_branch_select(self, event):
        """Handle branch selection in treeview"""
        selected_items = self.branch_tree.selection()
        if not selected_items:
            return
        
        selected_item = selected_items[0]
        branch_id = self.branch_tree.item(selected_item)["values"][0]
        
        try:
            branch = self.db.get_branch_by_id(branch_id)
            if branch:
                self.current_branch_id = branch["branch_id"]
                self.branch_entries[0].delete(0, tk.END)
                self.branch_entries[0].insert(0, branch["branch_name"])
                self.branch_entries[1].delete(0, tk.END)
                self.branch_entries[1].insert(0, branch["branch_address"])
                self.branch_entries[2].delete(0, tk.END)
                self.branch_entries[2].insert(0, branch["branch_city"])
                self.branch_entries[3].delete(0, tk.END)
                self.branch_entries[3].insert(0, branch["branch_state"])
                self.branch_entries[4].delete(0, tk.END)
                self.branch_entries[4].insert(0, branch["branch_zip"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load branch details: {str(e)}")

    def _clear_branch_fields(self):
        """Clear all branch form fields"""
        for entry in self.branch_entries:
            entry.delete(0, tk.END)
        if hasattr(self, 'current_branch_id'):
            del self.current_branch_id

    # ======================
    # EMPLOYEE METHODS
    # ======================
    
    def _load_employees(self):
        """Load employees from database into the treeview"""
        for item in self.employee_tree.get_children():
            self.employee_tree.delete(item)
        
        try:
            employees = self.db.get_all_employees()
            for emp in employees:
                self.employee_tree.insert("", tk.END, values=(
                    emp["emp_id"],
                    emp["emp_name"],
                    emp["emp_dob"],
                    emp["emp_phone"],
                    emp["emp_email"],
                    emp["emp_position"],
                    emp["branch_id"],
                    emp["branch_name"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load employees: {str(e)}")

    def _save_employee(self):
        """Save employee details to database"""
        data = [entry.get().strip() for entry in self.employee_entries]
        
        # Validate all fields are filled
        if not all(data):
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Validate date format
        try:
            datetime.strptime(data[1], "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return
        
        try:
            if hasattr(self, 'current_employee_id') and self.current_employee_id:
                # Update existing employee
                success = self.db.update_employee(
                    self.current_employee_id,
                    data[0], data[1], data[2], data[3], data[4], data[5]
                )
                if success:
                    messagebox.showinfo("Success", "Employee updated successfully")
                else:
                    messagebox.showerror("Error", "Failed to update employee")
            else:
                # Create new employee
                emp_id = self.db.insert_employee(
                    data[0], data[1], data[2], data[3], data[4], data[5]
                )
                if emp_id:
                    messagebox.showinfo("Success", "Employee added successfully")
                    self.current_employee_id = emp_id
                else:
                    messagebox.showerror("Error", "Failed to add employee")
            
            # Refresh the employee list and clear form
            self._load_employees()
            self._clear_employee_fields()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def _new_employee(self):
        """Clear the form for a new employee"""
        self.current_employee_id = None
        self._clear_employee_fields()

    def _delete_employee(self):
        """Delete the selected employee"""
        selected_items = self.employee_tree.selection()
        if not selected_items:
            messagebox.showinfo("Information", "Please select an employee to delete")
            return
        
        selected_item = selected_items[0]
        emp_id = self.employee_tree.item(selected_item)["values"][0]
        emp_name = self.employee_tree.item(selected_item)["values"][1]
        
        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Deletion", 
            f"Are you sure you want to delete employee '{emp_name}'?"
        )
        if not confirm:
            return
        
        try:
            success = self.db.delete_employee(emp_id)
            if success:
                messagebox.showinfo("Success", "Employee deleted successfully")
                self._clear_employee_fields()
                self._load_employees()
            else:
                messagebox.showerror("Error", "Failed to delete employee")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete employee: {str(e)}")

    def _on_employee_select(self, event):
        """Handle employee selection in treeview"""
        selected_items = self.employee_tree.selection()
        if not selected_items:
            return
        
        selected_item = selected_items[0]
        emp_id = self.employee_tree.item(selected_item)["values"][0]
        
        try:
            employee = self.db.get_employee_by_id(emp_id)
            if employee:
                self.current_employee_id = employee["emp_id"]
                self.employee_entries[0].delete(0, tk.END)
                self.employee_entries[0].insert(0, employee["emp_name"])
                self.employee_entries[1].delete(0, tk.END)
                self.employee_entries[1].insert(0, employee["emp_dob"])
                self.employee_entries[2].delete(0, tk.END)
                self.employee_entries[2].insert(0, employee["emp_phone"])
                self.employee_entries[3].delete(0, tk.END)
                self.employee_entries[3].insert(0, employee["emp_email"])
                self.employee_entries[4].delete(0, tk.END)
                self.employee_entries[4].insert(0, employee["emp_position"])
                self.employee_entries[5].delete(0, tk.END)
                self.employee_entries[5].insert(0, employee["branch_id"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load employee details: {str(e)}")

    def _clear_employee_fields(self):
        """Clear all employee form fields"""
        for entry in self.employee_entries:
            entry.delete(0, tk.END)
        if hasattr(self, 'current_employee_id'):
            del self.current_employee_id

    # ======================
    # CUSTOMER METHODS
    # ======================
    
    def _load_customers(self):
        """Load customers from database into the treeview"""
        for item in self.customer_tree.get_children():
            self.customer_tree.delete(item)
        
        try:
            customers = self.db.get_all_customers()
            for cust in customers:
                self.customer_tree.insert("", tk.END, values=(
                    cust["cust_id"],
                    cust["name"],
                    cust["dob"],
                    cust["phone"],
                    cust["email"],
                    cust["address"],
                    cust["branch_id"],
                    cust["branch_name"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load customers: {str(e)}")

    def _save_customer(self):
        """Save customer details to database"""
        data = [entry.get().strip() for entry in self.customer_entries]
        
        # Validate all fields are filled
        if not all(data):
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Validate date format
        try:
            datetime.strptime(data[1], "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return
        
        try:
            if hasattr(self, 'current_customer_id') and self.current_customer_id:
                # Update existing customer
                success = self.db.update_customer(
                    self.current_customer_id,
                    data[0], data[1], data[2], data[3], data[4], data[5]
                )
                if success:
                    messagebox.showinfo("Success", "Customer updated successfully")
                else:
                    messagebox.showerror("Error", "Failed to update customer")
            else:
                # Create new customer
                cust_id = self.db.insert_customer(
                    data[0], data[1], data[2], data[3], data[4], data[5]
                )
                if cust_id:
                    messagebox.showinfo("Success", "Customer added successfully")
                    self.current_customer_id = cust_id
                else:
                    messagebox.showerror("Error", "Failed to add customer")
            
            # Refresh the customer list and clear form
            self._load_customers()
            self._clear_customer_fields()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def _new_customer(self):
        """Clear the form for a new customer"""
        self.current_customer_id = None
        self._clear_customer_fields()

    def _delete_customer(self):
        """Delete the selected customer"""
        selected_items = self.customer_tree.selection()
        if not selected_items:
            messagebox.showinfo("Information", "Please select a customer to delete")
            return
        
        selected_item = selected_items[0]
        cust_id = self.customer_tree.item(selected_item)["values"][0]
        cust_name = self.customer_tree.item(selected_item)["values"][1]
        
        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Deletion", 
            f"Are you sure you want to delete customer '{cust_name}'?"
        )
        if not confirm:
            return
        
        try:
            success = self.db.delete_customer(cust_id)
            if success:
                messagebox.showinfo("Success", "Customer deleted successfully")
                self._clear_customer_fields()
                self._load_customers()
            else:
                messagebox.showerror("Error", "Failed to delete customer")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete customer: {str(e)}")

    def _on_customer_select(self, event):
        """Handle customer selection in treeview"""
        selected_items = self.customer_tree.selection()
        if not selected_items:
            return
        
        selected_item = selected_items[0]
        cust_id = self.customer_tree.item(selected_item)["values"][0]
        
        try:
            customer = self.db.get_customer_by_id(cust_id)
            if customer:
                self.current_customer_id = customer["cust_id"]
                self.customer_entries[0].delete(0, tk.END)
                self.customer_entries[0].insert(0, customer["name"])
                self.customer_entries[1].delete(0, tk.END)
                self.customer_entries[1].insert(0, customer["dob"])
                self.customer_entries[2].delete(0, tk.END)
                self.customer_entries[2].insert(0, customer["phone"])
                self.customer_entries[3].delete(0, tk.END)
                self.customer_entries[3].insert(0, customer["email"])
                self.customer_entries[4].delete(0, tk.END)
                self.customer_entries[4].insert(0, customer["address"])
                self.customer_entries[5].delete(0, tk.END)
                self.customer_entries[5].insert(0, customer["branch_id"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load customer details: {str(e)}")

    def _clear_customer_fields(self):
        """Clear all customer form fields"""
        for entry in self.customer_entries:
            entry.delete(0, tk.END)
        if hasattr(self, 'current_customer_id'):
            del self.current_customer_id

    # ======================
    # UTILITY METHODS
    # ======================
    
    def clear_window(self):
        """Clear all widgets from the root window"""
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def __del__(self):
        """Cleanup database connection"""
        if hasattr(self, 'db'):
            self.db.close()
