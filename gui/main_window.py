import customtkinter as ctk
#from backend.encryption import encrypt_message, decrypt_message
from gui.styles import theme
import tkinter.filedialog as fd
#from backend.storage import save_to_file, load_from_file
from config import APP_NAME, MASTER_PASSWORD
import pyperclip

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Basic window config
        self.title(APP_NAME)

        # Size and center
        window_width = 600
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(False, False)

        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.configure(bg=theme["bg_color"])

        # Title label
        self.title_label = ctk.CTkLabel(
            self, text="🔐 Text Encryptor & Decryptor",
            font=theme["font_bold"], text_color=theme["fg_color"]
        )
        self.title_label.pack(pady=(20, 10))

        # Password input
        self.password_box = ctk.CTkEntry(
            self, placeholder_text="Enter password", show="*", width=400
        )
        self.password_box.pack(pady=10)

        # Text input
        self.input_box = ctk.CTkEntry(
            self, placeholder_text="Enter your message here...", width=400
        )
        self.input_box.pack(pady=10)

        # Encrypt & Decrypt buttons side by side
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        self.encrypt_btn = ctk.CTkButton(button_frame, text="🔐 Encrypt", command=self.encrypt_dummy, width=180)
        self.encrypt_btn.grid(row=0, column=0, padx=10)

        self.decrypt_btn = ctk.CTkButton(button_frame, text="🔓 Decrypt", command=self.decrypt_dummy, width=180)
        self.decrypt_btn.grid(row=0, column=1, padx=10)

        # Output box
        self.output_box = ctk.CTkTextbox(self, width=500, height=100)
        self.output_box.pack(pady=10)

        # Copy & Clear buttons side by side
        utility_frame = ctk.CTkFrame(self, fg_color="transparent")
        utility_frame.pack(pady=5)

        self.copy_btn = ctk.CTkButton(utility_frame, text="📋 Copy Output", command=self.copy_output, width=180)
        self.copy_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = ctk.CTkButton(utility_frame, text="🧹 Clear", command=self.clear_fields, width=180)
        self.clear_btn.grid(row=0, column=1, padx=10)

        # Save & Load buttons side by side
        file_frame = ctk.CTkFrame(self, fg_color="transparent")
        file_frame.pack(pady=10)

        self.save_btn = ctk.CTkButton(file_frame, text="💾 Save to File", command=self.save_to_file, width=180)
        self.save_btn.grid(row=0, column=0, padx=10)

        self.load_btn = ctk.CTkButton(file_frame, text="📂 Load from File", command=self.load_from_file, width=180)
        self.load_btn.grid(row=0, column=1, padx=10)