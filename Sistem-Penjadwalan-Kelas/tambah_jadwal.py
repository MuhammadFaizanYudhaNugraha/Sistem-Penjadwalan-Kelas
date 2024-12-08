import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import Calendar
import csv

# Nama file CSV
FILENAME_JADWAL = "jadwal_kelas.csv"
HEADER_JADWAL = ["Mata Kuliah", "Dosen", "Kelas", "Hari", "Waktu", "Tanggal"]
FILENAME_KELAS = "data_kelas.csv"

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

def tambah_jadwal_kelas(root, bg_image_original, back_to_menu, add_background_to_window):
    def simpan_jadwal():
        mata_kuliah = entry_mata_kuliah.get()
        dosen = entry_dosen.get()
        kelas = combo_kelas.get()
        hari = combo_hari.get()
        waktu_mulai = f"{spinbox_jam_mulai.get()}:{spinbox_menit_mulai.get()}"
        waktu_selesai = f"{spinbox_jam_selesai.get()}:{spinbox_menit_selesai.get()}"
        tanggal = entry_tanggal.get()

        # Validasi waktu
        waktu_mulai_dt = datetime.strptime(waktu_mulai, "%H:%M")
        waktu_selesai_dt = datetime.strptime(waktu_selesai, "%H:%M")
        if waktu_mulai_dt >= waktu_selesai_dt:
            messagebox.showerror("Kesalahan", "Waktu mulai harus lebih awal dari waktu selesai!")
            return

        if not all([mata_kuliah, dosen, kelas, hari, waktu_mulai, waktu_selesai, tanggal]):
            messagebox.showerror("Kesalahan", "Semua field harus diisi!")
            return

        jadwal_baru = {
            "Mata Kuliah": mata_kuliah,
            "Dosen": dosen,
            "Kelas": kelas,
            "Hari": hari,
            "Waktu": f"{waktu_mulai}-{waktu_selesai}",
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
        spinbox_jam_mulai.delete(0, tk.END)
        spinbox_menit_mulai.delete(0, tk.END)
        spinbox_jam_selesai.delete(0, tk.END)
        spinbox_menit_selesai.delete(0, tk.END)
        entry_tanggal.delete(0, tk.END)

    def pilih_tanggal():
        def pilih():
            selected_date = cal.selection_get()
            entry_tanggal.delete(0, tk.END)
            entry_tanggal.insert(0, selected_date.strftime('%d-%m-%Y'))

            # Tentukan hari dalam minggu
            hari = selected_date.strftime('%A')
            hari_id = {
                'Monday': 'Senin',
                'Tuesday': 'Selasa',
                'Wednesday': 'Rabu',
                'Thursday': 'Kamis',
                'Friday': 'Jumat',
                'Saturday': 'Sabtu',
                'Sunday': 'Minggu'
            }
            combo_hari.set(hari_id[hari])
            top.destroy()

        top = tk.Toplevel(root)
        cal = Calendar(top, selectmode='day', date_pattern='dd-mm-yyyy')
        cal.pack(pady=20)

        tk.Button(top, text="Pilih", command=pilih).pack()

    for widget in root.winfo_children():
        widget.destroy()
    add_background_to_window(root, bg_image_original)

    label = tk.Label(root, text="Tambah Jadwal Kelas Baru", font=("times new roman", 16), bg="pink")
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    frame_input = tk.Frame(root, bg="pink")
    frame_input.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(frame_input, text="Mata Kuliah:", font=("times new roman", 10), bg="pink").grid(row=0, column=0, padx=5, pady=5)
    entry_mata_kuliah = tk.Entry(frame_input)
    entry_mata_kuliah.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Dosen:", font=("times new roman", 10), bg="pink").grid(row=1, column=0, padx=5, pady=5)
    entry_dosen = tk.Entry(frame_input)
    entry_dosen.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Kelas:", font=("times new roman", 10), bg="pink").grid(row=2, column=0, padx=5, pady=5)
    combo_kelas = ttk.Combobox(frame_input, values=[kelas["Kelas"] for kelas in read_csv(FILENAME_KELAS)])
    combo_kelas.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Hari:", font=("times new roman", 10), bg="pink").grid(row=3, column=0, padx=5, pady=5)
    combo_hari = ttk.Combobox(frame_input, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
    combo_hari.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Waktu Mulai:", font=("times new roman", 10), bg="pink").grid(row=4, column=0, padx=5, pady=5)
    spinbox_jam_mulai = tk.Spinbox(frame_input, from_=0, to=23, width=3, format="%02.0f")
    spinbox_jam_mulai.grid(row=4, column=1, padx=5, pady=5)
    spinbox_menit_mulai = tk.Spinbox(frame_input, from_=0, to=59, width=3, format="%02.0f")
    spinbox_menit_mulai.grid(row=4, column=2, padx=5, pady=5)

    tk.Label(frame_input, text="Waktu Selesai:", font=("times new roman", 10), bg="pink").grid(row=5, column=0, padx=5, pady=5)
    spinbox_jam_selesai = tk.Spinbox(frame_input, from_=0, to=23, width=3, format="%02.0f")
    spinbox_jam_selesai.grid(row=5, column=1, padx=5, pady=5)
    spinbox_menit_selesai = tk.Spinbox(frame_input, from_=0, to=59, width=3, format="%02.0f")
    spinbox_menit_selesai.grid(row=5, column=2, padx=5, pady=5)

    tk.Label(frame_input, text="Tanggal:", font=("times new roman", 10), bg="pink").grid(row=6, column=0, padx=5, pady=5)
    entry_tanggal = tk.Entry(frame_input)
    entry_tanggal.grid(row=6, column=1, padx=5, pady=5)

    tk.Button(frame_input, text="Pilih Tanggal", command=pilih_tanggal, font=("times new roman", 10), bg="pink").grid(row=6, column=2, padx=5, pady=5)

    tk.Button(root, text="Simpan", command=simpan_jadwal, font=("times new roman", 10), bg="pink").place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    tk.Button(root, text="Kembali", command=back_to_menu, font=("times new roman", 10), bg="pink").place(relx=0.5, rely=0.85, anchor=tk.CENTER)
