import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from cryptography.fernet import Fernet

def create_key(password):
    return Fernet.generate_key()

def encrypt_file(file_name, data, password):
    key = create_key(password)
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    with open(file_name, 'wb') as f:
        f.write(key + b'::' + encrypted_data)
    messagebox.showinfo("Başarılı", "Dosya başarıyla şifrelendi ve kaydedildi.")
    clear_form()

def decrypt_file(file_name, password):
    with open(file_name, 'rb') as f:
        file_data = f.read()
    key, encrypted_data = file_data.split(b'::')
    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data
    except:
        messagebox.showerror("Hata", "Şifre yanlış!")
        return None

def save_and_encrypt():
    file_name = Dosya_giris.get()
    content = text.get("1.0", tk.END)
    password = Dosya_giris_sifre.get()
    if file_name and content and password:
        encrypt_file(file_name + '.txt', content, password)
    else:
        messagebox.showwarning("Uyarı", "Tüm alanları doldurun!")

def select_and_decrypt():
    file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    password = Dosya_giris_sifre.get()
    if file_name and password:
        decrypted_content = decrypt_file(file_name, password)
        if decrypted_content:
            text.delete("1.0", tk.END)
            text.insert(tk.END, decrypted_content)
    else:
        messagebox.showwarning("Uyarı", "Dosya ve şifre girin!")

def clear_form():
    Dosya_giris.delete(0, tk.END)
    text.delete("1.0", tk.END)
    Dosya_giris_sifre.delete(0, tk.END)

# UI
window = tk.Tk()
window.title("SecretNotes")
window.geometry("400x600")

# İkonu yükle ve pencereye ekle
img = Image.open("örnek.png")
img = img.resize((64, 64), Image.Resampling.LANCZOS)  # İkon boyutunu ayarla
icon = ImageTk.PhotoImage(img)
window.iconphoto(False, icon)

# Dosya Başlığı
Dosya_etiketi = tk.Label(window, text="Dosya Başlığını Giriniz")
Dosya_etiketi.config(fg="black")
Dosya_etiketi.grid(row=1, column=0, padx=10, pady=10, sticky='e')

Dosya_giris = tk.Entry(window, width=30)
Dosya_giris.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Dosya İçeriği
Dosya_icerik = tk.Label(window, text="Dosya İçeriğini Giriniz")
Dosya_icerik.config(fg="black")
Dosya_icerik.grid(row=2, column=0, padx=10, pady=10, sticky='ne')

text = tk.Text(window, width=30, height=10)
text.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Dosya Şifresi
Dosya_sifresi = tk.Label(window, text="Dosya Şifresini Giriniz")
Dosya_sifresi.config(fg="black")
Dosya_sifresi.grid(row=3, column=0, padx=10, pady=10, sticky='e')

Dosya_giris_sifre = tk.Entry(window, width=30)
Dosya_giris_sifre.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Kaydet ve Şifrele Butonu
save_button = tk.Button(window, text="Kaydet ve Şifrele", command=save_and_encrypt)
save_button.grid(row=4, column=0, columnspan=2, pady=10)

# Şifre Çöz Butonu
decrypt_button = tk.Button(window, text="Şifre Çöz", command=select_and_decrypt)
decrypt_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
