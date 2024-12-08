# menu_utama.py

import tkinter as tk
from tkinter import Label, Button
from PIL import ImageTk, Image

# Inisialisasi variabel global
bg_image = None
resized_bg_image = None
background_label = None

# Fungsi untuk menambahkan background ke window
def add_background_to_window(window, bg_image_original):
    global bg_image, resized_bg_image, background_label
    bg_image = ImageTk.PhotoImage(bg_image_original)
    background_label = Label(window, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    window.bind('<Configure>', lambda event: resize_image(event, bg_image_original))

def resize_image(event, bg_image_original):
    global bg_image, resized_bg_image, background_label
    if background_label and background_label.winfo_exists():
        resized_bg_image = bg_image_original.resize((event.width, event.height), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(resized_bg_image)
        background_label.config(image=bg_image)

# Fungsi untuk menampilkan menu utama
def main_menu(root, bg_image_original, tampilkan_kelas, tampilkan_jadwal_kelas, tambah_kelas, tambah_jadwal_kelas, keluar_aplikasi):
    global background_label
    for widget in root.winfo_children():
        widget.destroy()
    add_background_to_window(root, bg_image_original)

    label = Label(root, text="🍪  🎀  𝓢𝓲𝓼𝓽𝓮𝓶 𝓟𝓮𝓷𝓳𝓪𝓭𝔀𝓪𝓵𝓪𝓷 𝓚𝓮𝓵𝓪𝓼 🍪  🎀", font=("Arial", 18), bg="pink")
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    btn_tampilkan_kelas = Button(root, text="Tampilkan Kelas", command=tampilkan_kelas, width=20, font=("Times New Roman", 10), bg="pink")
    btn_tampilkan_kelas.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    btn_tampilkan_jadwal_kelas = Button(root, text="Tampilkan Jadwal Kelas", command=tampilkan_jadwal_kelas, width=20, font=("Times New Roman", 10), bg="pink")
    btn_tampilkan_jadwal_kelas.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    btn_tambah_kelas = Button(root, text="Tambah Kelas", command=tambah_kelas, width=20, font=("times new roman", 10), bg="pink")
    btn_tambah_kelas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    btn_tambah_jadwal_kelas = Button(root, text="Tambah Jadwal Kelas", command=tambah_jadwal_kelas, width=20, font=("times new roman", 10), bg="pink")
    btn_tambah_jadwal_kelas.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    btn_keluar = Button(root, text="Keluar", command=keluar_aplikasi, width=20, font=("times new roman", 10), bg="pink")
    btn_keluar.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
