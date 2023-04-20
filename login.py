import tkinter as tk


class ResumeForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
       
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.phone_label = tk.Label(self, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()

        self.skills_label = tk.Label(self, text="Skills:")
        self.skills_label.pack()
        self.skills_entry = tk.Entry(self)
        self.skills_entry.pack()

       
        self.submit_button = tk.Button(self, text="Submit", command=self.preview_resume)
        self.submit_button.pack()
    
    def preview_resume(self):
     
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        skills = self.skills_entry.get()

   
        self.controller.show_resume_preview(name, email, phone, skills)

class ResumePreview(tk.Toplevel):
    def __init__(self, parent, name, email, phone, skills):
        tk.Toplevel.__init__(self, parent)
        
    
    
        self.name_label = tk.Label(self, text="Name: " + name)
        self.name_label.pack()
        self.email_label = tk.Label(self, text="Email: " + email)
        self.email_label.pack()
        self.phone_label = tk.Label(self, text="Phone: " + phone)
        self.phone_label.pack()
        self.skills_label = tk.Label(self, text="Skills: " + skills)
        self.skills_label.pack()

class MainController:
    def __init__(self, parent):
        self.parent = parent
        self.show_resume_form()
        
    def show_resume_form(self):
        self.resume_form = ResumeForm(self.parent, self)
        self.resume_form.pack()
        
    def show_resume_preview(self, name, email, phone, skills):
        self.resume_preview = ResumePreview(self.parent, name, email, phone, skills)

if __name__ == '__main__':
    root = tk.Tk()
    app = MainController(root)
    root.mainloop()
