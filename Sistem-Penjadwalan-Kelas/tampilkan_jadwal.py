import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import csv

# Nama file CSV
FILENAME_JADWAL = "jadwal_kelas.csv"
HEADER_JADWAL = ["Mata Kuliah", "Dosen", "Kelas", "Hari", "Waktu", "Tanggal"]

# Fungsi untuk membaca data dari CSV
def read_csv(filename):
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

# Fungsi untuk menulis data ke CSV
def write_csv(filename, data, header):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

# Fungsi resize image
def resize_image(event, bg_image_original):
    global bg_image, resized_bg_image, background_label
    # Mengubah ukuran gambar sesuai dengan ukuran jendela
    resized_bg_image = bg_image_original.resize((event.width, event.height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_bg_image)
    background_label.config(image=bg_image)

# Fungsi untuk menghapus jadwal
def hapus_jadwal(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Kesalahan", "Silakan pilih jadwal yang akan dihapus!")
        return

    confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus jadwal ini?")
    if not confirm:
        return

    # Mendapatkan data dari Treeview
    selected_values = tree.item(selected_item, "values")
    mata_kuliah, dosen, kelas, hari, waktu, tanggal = selected_values

    # Membaca data dari CSV dan menghapus entri yang dipilih
    data = read_csv(FILENAME_JADWAL)
    data = [row for row in data if not (
        row["Mata Kuliah"] == mata_kuliah and
        row["Dosen"] == dosen and
        row["Kelas"] == kelas and
        row["Hari"] == hari and
        row["Waktu"] == waktu and
        row["Tanggal"] == tanggal
    )]

    # Menulis kembali data ke CSV
    write_csv(FILENAME_JADWAL, data, HEADER_JADWAL)

    # Menghapus entri dari Treeview
    tree.delete(selected_item)
    messagebox.showinfo("Berhasil", "Jadwal berhasil dihapus!")

# Fungsi untuk menampilkan data jadwal kelas
def tampilkan_jadwal_kelas(root, bg_image_original, back_to_menu):
    for widget in root.winfo_children():
        widget.destroy()
    add_background_to_window(root, bg_image_original)

    label = tk.Label(root, text="Data Jadwal Kelas", font=("Times New Roman", 16), bg="pink")
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    tree = ttk.Treeview(root, columns=HEADER_JADWAL, show="headings", height=10)
    tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    for col in HEADER_JADWAL:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    data = read_csv(FILENAME_JADWAL)
    for row in data:
        tree.insert("", "end", values=list(row.values()))

    # Tombol Hapus
    delete_button = tk.Button(root, text="Hapus", command=lambda: hapus_jadwal(tree), width=20, font=("times new roman", 10), bg="red", fg="white")
    delete_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Tombol Kembali
    back_button = tk.Button(root, text="Kembali", command=back_to_menu, width=20, font=("times new roman", 10), bg="pink")
    back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Fungsi untuk menambahkan background ke window
def add_background_to_window(window, bg_image_original):
    global bg_image, resized_bg_image, background_label
    bg_image = ImageTk.PhotoImage(bg_image_original)
    background_label = tk.Label(window, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    window.bind('<Configure>', lambda event: resize_image(event, bg_image_original))