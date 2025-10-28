import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
import threading
from pathlib import Path

class ImageUpscalerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Upscaler - 2x Maximum")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.selected_files = []
        self.output_folder = tk.StringVar()
        self.scale_factor = tk.DoubleVar(value=2.0)
        self.processing = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Image Upscaler", font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Scale factor selection
        scale_frame = ttk.LabelFrame(main_frame, text="Scale Factor", padding="10")
        scale_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(scale_frame, text="Pilih faktor skala:").grid(row=0, column=0, padx=(0, 10))
        scale_combo = ttk.Combobox(scale_frame, textvariable=self.scale_factor, 
                                  values=[1.25, 1.5, 1.75, 2.0], state="readonly", width=10)
        scale_combo.grid(row=0, column=1)
        scale_combo.set(2.0)
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="Pilih Gambar", padding="10")
        file_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Single file selection
        ttk.Button(file_frame, text="Pilih 1 Gambar", 
                  command=self.select_single_file).grid(row=0, column=0, padx=(0, 10))
        
        # Multiple files selection
        ttk.Button(file_frame, text="Pilih Multiple Gambar (Batch)", 
                  command=self.select_multiple_files).grid(row=0, column=1, padx=(0, 10))
        
        # Clear selection
        ttk.Button(file_frame, text="Clear Selection", 
                  command=self.clear_selection).grid(row=0, column=2)
        
        # Selected files display
        self.files_listbox = tk.Listbox(file_frame, height=6, width=80)
        self.files_listbox.grid(row=1, column=0, columnspan=3, pady=(10, 0), sticky=(tk.W, tk.E))
        
        # Scrollbar for listbox
        scrollbar = ttk.Scrollbar(file_frame, orient="vertical", command=self.files_listbox.yview)
        scrollbar.grid(row=1, column=3, sticky=(tk.N, tk.S))
        self.files_listbox.configure(yscrollcommand=scrollbar.set)
        
        # Output folder selection
        output_frame = ttk.LabelFrame(main_frame, text="Folder Output", padding="10")
        output_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Entry(output_frame, textvariable=self.output_folder, width=60).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(output_frame, text="Browse", command=self.select_output_folder).grid(row=0, column=1)
        
        # Progress frame
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        progress_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                          maximum=100, length=400)
        self.progress_bar.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        self.status_label = ttk.Label(progress_frame, text="Siap untuk memproses")
        self.status_label.grid(row=1, column=0, columnspan=2, pady=(5, 0))
        
        # Process button
        self.process_button = ttk.Button(main_frame, text="Mulai Upscale", 
                                       command=self.start_processing, style='Accent.TButton')
        self.process_button.grid(row=5, column=0, columnspan=3, pady=20)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        file_frame.columnconfigure(0, weight=1)
        output_frame.columnconfigure(0, weight=1)
        progress_frame.columnconfigure(0, weight=1)
        
    def select_single_file(self):
        file_path = filedialog.askopenfilename(
            title="Pilih gambar",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp")]
        )
        if file_path:
            self.selected_files = [file_path]
            self.update_files_display()
            
    def select_multiple_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Pilih multiple gambar",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp")]
        )
        if file_paths:
            self.selected_files = list(file_paths)
            self.update_files_display()
            
    def clear_selection(self):
        self.selected_files = []
        self.update_files_display()
        
    def update_files_display(self):
        self.files_listbox.delete(0, tk.END)
        for file_path in self.selected_files:
            self.files_listbox.insert(tk.END, os.path.basename(file_path))
            
    def select_output_folder(self):
        folder_path = filedialog.askdirectory(title="Pilih folder output")
        if folder_path:
            self.output_folder.set(folder_path)
            
    def validate_inputs(self):
        if not self.selected_files:
            messagebox.showerror("Error", "Pilih minimal 1 gambar untuk diproses!")
            return False
            
        if not self.output_folder.get():
            messagebox.showerror("Error", "Pilih folder output!")
            return False
            
        if not os.path.exists(self.output_folder.get()):
            messagebox.showerror("Error", "Folder output tidak ditemukan!")
            return False
            
        return True
        
    def start_processing(self):
        if not self.validate_inputs():
            return
            
        if self.processing:
            messagebox.showwarning("Warning", "Sedang memproses, tunggu hingga selesai!")
            return
            
        # Start processing in separate thread
        self.processing = True
        self.process_button.configure(state='disabled')
        
        thread = threading.Thread(target=self.process_images)
        thread.daemon = True
        thread.start()
        
    def process_images(self):
        try:
            total_files = len(self.selected_files)
            scale = self.scale_factor.get()
            
            for i, file_path in enumerate(self.selected_files):
                # Update status
                self.root.after(0, lambda: self.status_label.configure(
                    text=f"Memproses: {os.path.basename(file_path)}"))
                
                # Process image
                success = self.upscale_image(file_path, scale)
                
                if not success:
                    self.root.after(0, lambda: messagebox.showerror(
                        "Error", f"Gagal memproses: {os.path.basename(file_path)}"))
                    continue
                    
                # Update progress
                progress = ((i + 1) / total_files) * 100
                self.root.after(0, lambda p=progress: self.progress_var.set(p))
                
            # Processing complete
            self.root.after(0, self.processing_complete)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}"))
            self.root.after(0, self.processing_complete)
            
    def upscale_image(self, input_path, scale_factor):
        try:
            # Open image
            with Image.open(input_path) as img:
                # Calculate new size
                original_width, original_height = img.size
                new_width = int(original_width * scale_factor)
                new_height = int(original_height * scale_factor)
                
                # Upscale using LANCZOS resampling for better quality
                upscaled_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Generate output filename
                input_name = Path(input_path).stem
                input_ext = Path(input_path).suffix
                output_filename = f"{input_name}_upscaled_{scale_factor}x{input_ext}"
                output_path = os.path.join(self.output_folder.get(), output_filename)
                
                # Save upscaled image
                upscaled_img.save(output_path, quality=95, optimize=True)
                
            return True
            
        except Exception as e:
            print(f"Error processing {input_path}: {str(e)}")
            return False
            
    def processing_complete(self):
        self.processing = False
        self.process_button.configure(state='normal')
        self.progress_var.set(100)
        self.status_label.configure(text="Proses selesai!")
        
        messagebox.showinfo("Sukses", 
                           f"Berhasil memproses {len(self.selected_files)} gambar!\n"
                           f"Output disimpan di: {self.output_folder.get()}")
        
        # Reset progress after 3 seconds
        self.root.after(3000, lambda: (
            self.progress_var.set(0),
            self.status_label.configure(text="Siap untuk memproses")
        ))

def main():
    root = tk.Tk()
    app = ImageUpscalerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()