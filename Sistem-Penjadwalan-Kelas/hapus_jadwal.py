import tkinter as tk
from tkinter import messagebox

def hapus_jadwal_kelas(root, bg_image_original, back_to_menu):
    # Contoh data jadwal yang bisa dihapus
    jadwal = ["Senin: Matematika", "Selasa: Fisika", "Rabu: Kimia"]
    
    def hapus_aksi():
        selected = listbox.curselection()
        if selected:
            jadwal_terpilih = jadwal[selected[0]]
            if messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus jadwal {jadwal_terpilih}?"):
                jadwal.pop(selected[0])
                listbox.delete(selected)
                messagebox.showinfo("Sukses", f"Jadwal {jadwal_terpilih} berhasil dihapus.")
        else:
            messagebox.showwarning("Peringatan", "Pilih jadwal yang ingin dihapus.")
    
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    listbox = tk.Listbox(frame)
    for item in jadwal:
        listbox.insert(tk.END, item)
    listbox.pack()

    btn_hapus = tk.Button(frame, text="Hapus", command=hapus_aksi)
    btn_hapus.pack()

    btn_kembali = tk.Button(frame, text="Kembali", command=lambda: [frame.destroy(), back_to_menu()])
    btn_kembali.pack()
