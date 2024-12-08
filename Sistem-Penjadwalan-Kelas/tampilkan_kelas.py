import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import csv
from menu_utama import add_background_to_window

# Nama file CSV
FILENAME_KELAS = "data_kelas.csv"
HEADER_KELAS = ["Kelas", "Gedung"]

# Fungsi untuk membaca data dari CSV
def read_csv(filename):
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

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

    back_button = tk.Button(root, text="Kembali", command=back_to_menu, width=20, font=("times new roman", 10), bg="pink")
    back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
