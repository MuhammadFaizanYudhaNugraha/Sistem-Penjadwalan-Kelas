import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

#coba push
# Nama file CSV
FILENAME_KELAS = "data_kelas.csv"
FILENAME_JADWAL = "jadwal_kelas.csv"

# Data awal jika file CSV belum ada
HEADER_KELAS = ["Kelas", "Gedung"]
HEADER_JADWAL = ["Mata Kuliah", "Dosen", "Kelas", "Hari", "Waktu", "Tanggal"]

# Fungsi untuk memeriksa dan membuat file CSV jika belum ada
def initialize_csv(filename, header):
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)

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

# Frame untuk kembali ke menu utama
def back_to_menu():
    for widget in root.winfo_children():
        widget.destroy()
    main_menu()

# Fungsi keluar aplikasi
def keluar_aplikasi():
    root.destroy()

# Fungsi untuk menambah kelas baru
def tambah_kelas():
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

    tk.Label(root, text="Tambah Kelas Baru", font=("Arial", 16)).pack(pady=10)

    frame_input = tk.Frame(root)
    frame_input.pack(pady=10)
    tk.Label(frame_input, text="Kelas:").grid(row=0, column=0, padx=5, pady=5)
    entry_kelas = tk.Entry(frame_input)
    entry_kelas.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Gedung:").grid(row=1, column=0, padx=5, pady=5)
    entry_gedung = tk.Entry(frame_input)
    entry_gedung.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(root, text="Simpan", command=simpan_kelas).pack(pady=5)
    tk.Button(root, text="Kembali", command=back_to_menu).pack(pady=5)

# Frame untuk menampilkan data kelas
def tampilkan_kelas():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Data Kelas", font=("Arial", 16)).pack(pady=10)

    tree = ttk.Treeview(root, columns=HEADER_KELAS, show="headings", height=10)
    tree.pack(pady=10, fill="x")

    for col in HEADER_KELAS:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    data = read_csv(FILENAME_KELAS)
    for row in data:
        tree.insert("", "end", values=list(row.values()))

    tk.Button(root, text="Kembali", command=back_to_menu).pack(pady=5)

# Frame untuk menambah jadwal kelas
def tambah_jadwal_kelas():
    def simpan_jadwal():
        mata_kuliah = entry_mata_kuliah.get()
        dosen = entry_dosen.get()
        kelas = combo_kelas.get()
        hari = combo_hari.get()
        waktu = entry_waktu.get()
        tanggal = entry_tanggal.get()

        if not all([mata_kuliah, dosen, kelas, hari, waktu, tanggal]):
            messagebox.showerror("Kesalahan", "Semua field harus diisi!")
            return

        jadwal_baru = {
            "Mata Kuliah": mata_kuliah,
            "Dosen": dosen,
            "Kelas": kelas,
            "Hari": hari,
            "Waktu": waktu,
            "Tanggal": tanggal,
        }

        data = read_csv(FILENAME_JADWAL)
        data.append(jadwal_baru)
        write_csv(FILENAME_JADWAL, data, HEADER_JADWAL)

        messagebox.showinfo("Berhasil", "Jadwal berhasil ditambahkan!")
        clear_entries()

    def clear_entries():
        entry_mata_kuliah.delete(0, tk.END)
        entry_dosen.delete(0, tk.END)
        combo_kelas.set("")
        combo_hari.set("")
        entry_waktu.delete(0, tk.END)
        entry_tanggal.delete(0, tk.END)

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Tambah Jadwal Kelas Baru", font=("Arial", 16)).pack(pady=10)

    frame_input = tk.Frame(root)
    frame_input.pack(pady=10)

    tk.Label(frame_input, text="Mata Kuliah:").grid(row=0, column=0, padx=5, pady=5)
    entry_mata_kuliah = tk.Entry(frame_input)
    entry_mata_kuliah.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Dosen:").grid(row=1, column=0, padx=5, pady=5)
    entry_dosen = tk.Entry(frame_input)
    entry_dosen.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Kelas:").grid(row=2, column=0, padx=5, pady=5)
    combo_kelas = ttk.Combobox(frame_input, values=[kelas["Kelas"] for kelas in read_csv(FILENAME_KELAS)])
    combo_kelas.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Hari:").grid(row=3, column=0, padx=5, pady=5)
    combo_hari = ttk.Combobox(frame_input, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
    combo_hari.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Waktu(HH.MM-HH.MM):").grid(row=4, column=0, padx=5, pady=5)
    entry_waktu = tk.Entry(frame_input)
    entry_waktu.grid(row=4, column=1, padx=5, pady=5)
    
    tk.Label(frame_input, text="Tanggal(DD-MM-YYYY):").grid(row=5, column=0, padx=5, pady=5)
    entry_tanggal = tk.Entry(frame_input)
    entry_tanggal.grid(row=5, column=1, padx=5, pady=5)

    tk.Button(root, text="Simpan", command=simpan_jadwal).pack(pady=5)
    tk.Button(root, text="Kembali", command=back_to_menu).pack(pady=5)

# Frame untuk menampilkan jadwal kelas
def tampilkan_jadwal_kelas():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Data Jadwal Kelas", font=("Arial", 16)).pack(pady=10)

    tree = ttk.Treeview(root, columns=HEADER_JADWAL, show="headings", height=10)
    tree.pack(pady=10, fill="x")

    for col in HEADER_JADWAL:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    data = read_csv(FILENAME_JADWAL)
    for row in data:
        tree.insert("", "end", values=list(row.values()))

    tk.Button(root, text="Kembali", command=back_to_menu).pack(pady=5)

# Frame menu utama
def main_menu():
    tk.Label(root, text="Sistem Penjadwalan Kelas", font=("Arial", 18)).pack(pady=10)

    tk.Button(root, text="Tampilkan Kelas", command=tampilkan_kelas, width=20).pack(pady=5)
    tk.Button(root, text="Tampilkan Jadwal Kelas", command=tampilkan_jadwal_kelas, width=20).pack(pady=5)
    tk.Button(root, text="Tambah Kelas", command=tambah_kelas, width=20).pack(pady=5)
    tk.Button(root, text="Tambah Jadwal Kelas", command=tambah_jadwal_kelas, width=20).pack(pady=5)
    tk.Button(root, text="Keluar", command=keluar_aplikasi, width=20).pack(pady=5)

# Inisialisasi file CSV
initialize_csv(FILENAME_KELAS, HEADER_KELAS)
initialize_csv(FILENAME_JADWAL, HEADER_JADWAL)

# Inisialisasi GUI
root = tk.Tk()
root.title("Sistem Penjadwalan Kelas")
root.geometry("600x400")

main_menu()

root.mainloop()
