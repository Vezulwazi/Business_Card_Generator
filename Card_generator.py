import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Create GUI window
class BusinessCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Business Card Generator")
        self.root.geometry("500x400")
        
        # Load the background image using Pillow
        self.bg_image = Image.open("building.png")
        self.bg_image = self.bg_image.resize((500, 400), Image.LANCZOS)  # Resize to fit the window
        self.background_image = ImageTk.PhotoImage(self.bg_image)  # Convert the image for Tkinter
        
        # Add background image to label
        bg_label = tk.Label(self.root, image=self.background_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Title
        title_label = tk.Label(self.root, text="Create Your Business Card", font=("Helvetica", 16, "bold"), bg="lightgray")
        title_label.pack(pady=10)
        
        # Name Entry
        self.name_label = tk.Label(self.root, text="Name:", bg="lightgray")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root, width=40)
        self.name_entry.pack(pady=5)
        
        # Job Title Entry
        self.job_label = tk.Label(self.root, text="Job Title:", bg="lightgray")
        self.job_label.pack()
        self.job_entry = tk.Entry(self.root, width=40)
        self.job_entry.pack(pady=5)
        
        # Phone Number Entry
        self.phone_label = tk.Label(self.root, text="Phone Number:", bg="lightgray")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root, width=40)
        self.phone_entry.pack(pady=5)
        
        # Email Entry
        self.email_label = tk.Label(self.root, text="Email:", bg="lightgray")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root, width=40)
        self.email_entry.pack(pady=5)
        
        # Generate Button
        self.generate_button = tk.Button(self.root, text="Generate Business Card", command=self.generate_card)
        self.generate_button.pack(pady=20)

    def generate_card(self):
        # Get the details from the entry fields
        name = self.name_entry.get()
        job_title = self.job_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        
        # Check if all fields are filled
        if not (name and job_title and phone and email):
            messagebox.showerror("Error", "Please fill all fields.")
            return
        
        # Load the background image for the card generation
        card_image = Image.open("building.png")
        draw = ImageDraw.Draw(card_image)
        
        # Define fonts (change the font path as per your system)
        try:
            font_name = ImageFont.truetype("arial.ttf", 40)
            font_details = ImageFont.truetype("arial.ttf", 25)
        except:
            messagebox.showerror("Error", "Could not load font. Please ensure 'arial.ttf' is installed.")
            return
        
        # Define text positions
        text_x, text_y = 100, 50
        
        # Add text to the image
        draw.text((text_x, text_y), name, font=font_name, fill="white")
        draw.text((text_x, text_y + 60), job_title, font=font_details, fill="white")
        draw.text((text_x, text_y + 110), f"Phone: {phone}", font=font_details, fill="white")
        draw.text((text_x, text_y + 160), f"Email: {email}", font=font_details, fill="white")
        
        # Save the image
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            card_image.save(save_path)
            messagebox.showinfo("Success", f"Business card saved at {save_path}")
        else:
            messagebox.showerror("Error", "Saving canceled.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = BusinessCardApp(root)
    root.mainloop()
