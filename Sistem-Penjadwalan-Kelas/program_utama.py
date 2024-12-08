import tkinter as tk
from PIL import ImageTk, Image
from menu_utama import main_menu, resize_image, add_background_to_window
from tampilkan_kelas import tampilkan_kelas
from tampilkan_jadwal import tampilkan_jadwal_kelas
from tambah_kelas import tambah_kelas
from tambah_jadwal import tambah_jadwal_kelas

# Inisialisasi GUI
root = tk.Tk()
root.title("Sistem Penjadwalan Kelas")
root.geometry("600x400")

# Simpan referensi gambar
bg_image_original = Image.open("bg.png")

# Fungsi untuk kembali ke menu utama
def back_to_menu():
    main_menu(root, bg_image_original, lambda: tampilkan_kelas(root, bg_image_original, back_to_menu),
              lambda: tampilkan_jadwal_kelas(root, bg_image_original, back_to_menu), 
              lambda: tambah_kelas(root, bg_image_original, back_to_menu, add_background_to_window),
              lambda: tambah_jadwal_kelas(root, bg_image_original, back_to_menu, add_background_to_window),
              keluar_aplikasi)

# Fungsi untuk keluar aplikasi
def keluar_aplikasi():
    root.destroy()

# Panggil fungsi main_menu dari modul
main_menu(root, bg_image_original, lambda: tampilkan_kelas(root, bg_image_original, back_to_menu),
          lambda: tampilkan_jadwal_kelas(root, bg_image_original, back_to_menu), 
          lambda: tambah_kelas(root, bg_image_original, back_to_menu, add_background_to_window),
          lambda: tambah_jadwal_kelas(root, bg_image_original, back_to_menu, add_background_to_window),
          keluar_aplikasi)

# Bind event resize untuk menyesuaikan ukuran gambar background
root.bind('<Configure>', lambda event: resize_image(event, bg_image_original))

root.mainloop()
