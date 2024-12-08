import tkinter as tk
from tkinter import ttk, messagebox
import csv

# Nama file CSV
FILENAME_KELAS = "data_kelas.csv"
HEADER_KELAS = ["Kelas", "Gedung"]

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

# Fungsi untuk menambah kelas baru
def tambah_kelas(root, bg_image_original, back_to_menu, add_background_to_window):
    def simpan_kelas():
        kelas = entry_kelas.get()
        gedung = entry_gedung.get()
        if not kelas or not gedung:
            messagebox.showerror("Kesalahan", "Semua field harus diisi!")
            return

        kelas_baru = {"Kelas": kelas, "Gedung": gedung}
        data = read_csv(FILENAME_KELAS)
        data.append(kelas_baru)
        write_csv(FILENAME_KELAS, data, HEADER_KELAS)

        messagebox.showinfo("Berhasil", "Kelas berhasil ditambahkan!")
        entry_kelas.delete(0, tk.END)
        entry_gedung.delete(0, tk.END)

    for widget in root.winfo_children():
        widget.destroy()
    add_background_to_window(root, bg_image_original)

    label = tk.Label(root, text="Tambah Kelas Baru", font=("times new roman", 16), bg="pink")
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    frame_input = tk.Frame(root, bg="pink")
    frame_input.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(frame_input, text="Kelas:", font=("times new roman", 10), bg="pink").grid(row=0, column=0, padx=5, pady=5)
    entry_kelas = tk.Entry(frame_input)
    entry_kelas.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Gedung:", font=("times new roman", 10), bg="pink").grid(row=1, column=0, padx=5, pady=5)
    entry_gedung = tk.Entry(frame_input)
    entry_gedung.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(root, text="Simpan", command=simpan_kelas, font=("times new roman", 10), bg="pink").place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    tk.Button(root, text="Kembali", command=back_to_menu, font=("times new roman", 10), bg="pink").place(relx=0.5, rely=0.85, anchor=tk.CENTER)
