import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import csv
from menu_utama import add_background_to_window

# Nama file CSV
FILENAME_KELAS = "data_kelas.csv"
HEADER_KELAS = ["Kelas", "Gedung"]

# Fungsi untuk membaca data dari CSV
def read_csv(filename):
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        # Jika file tidak ditemukan, buat file dengan header kosong
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADER_KELAS)
            writer.writeheader()
        return []

# Fungsi untuk menulis data ke CSV
def write_csv(filename, data, header):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

# Fungsi untuk menghapus data kelas
def hapus_kelas(tree):
    selected_item = tree.selection()  # Mendapatkan item yang dipilih
    if not selected_item:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
        return

    # Konfirmasi penghapusan
    if not messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?"):
        return

    # Ambil nilai dari item yang dipilih
    values = tree.item(selected_item, "values")
    kelas_dihapus = values[0]  # Kolom "Kelas"

    # Baca data dari CSV dan hapus item yang sesuai
    data = read_csv(FILENAME_KELAS)
    data = [row for row in data if row["Kelas"] != kelas_dihapus]

    # Tulis ulang CSV tanpa data yang dihapus
    write_csv(FILENAME_KELAS, data, HEADER_KELAS)

    # Hapus item dari Treeview
    tree.delete(selected_item)

    messagebox.showinfo("Info", "Data berhasil dihapus!")

# Fungsi untuk menampilkan data kelas
def tampilkan_kelas(root, bg_image_original, back_to_menu):
    for widget in root.winfo_children():
        widget.destroy()
    
    # Menggunakan fungsi add_background_to_window dari modul menu_utama
    add_background_to_window(root, bg_image_original)

    # Menambahkan Label dan Treeview di Atas Background
    label = tk.Label(root, text="Data Kelas", font=("times new roman", 16), bg="pink")
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    tree = ttk.Treeview(root, columns=HEADER_KELAS, show="headings", height=10)
    tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    for col in HEADER_KELAS:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    data = read_csv(FILENAME_KELAS)
    for row in data:
        tree.insert("", "end", values=list(row.values()))

    # Tombol "Hapus"
    delete_button = tk.Button(root, text="Hapus", command=lambda: hapus_kelas(tree), width=20, font=("times new roman", 10), bg="red", fg="white")
    delete_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Tombol "Kembali"
    back_button = tk.Button(root, text="Kembali", command=back_to_menu, width=20, font=("times new roman", 10), bg="pink")
    back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)