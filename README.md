# 13C Sistem Penjadwalan Kelas
### Anggota :
- Muhammad Faizan Yudha Nugraha I0324119
- Sakkhiya Aziza Tara Mumtaz I0324122

Sistem Penjadwalan Kelas adalah program yang dirancang untuk membantu  dalam mengatur jadwal kelas kuliah secara efisien. Sistem ini bertujuan untuk mengoptimalkan penggunaan ruang kelas, waktu pengajar, dan kebutuhan mata kuliah sehingga jadwal yang dihasilkan bebas dari konflik.

## Fitur:
- Sistem dapat menambah daftar kelas
- Sistem dapat menampilkan daftar kelas yang ditambahkan
- Sitem dapat menambah dan menampilkan jadwal pada kelas yang ditambahkan

## Cara Kerja:
1. Start untuk memulai program
2. Muncul 5 Menu
3. Klik Tambah Kelas untuk menambah daftar kelas
4. Klik Tambah Jadwal Kelas untuk menambah jadwal pada kelas yang tersedia
5. Klik Tampilkan Kelas untuk menampilkan daftar kelas yang tersedia
6. Klik Tampilkan Jadwal Kelas untuk menampilkan daftar jadwal kelas yang telah ditambahkan
7. Klik Keluar untuk menutup program sekaligus mengakhiri, tetapi tidak menghapus kelas dan jadwal yang telah ditambahkan
8. Cara menghapus daftar kelas dan jadwal kelas yang telah ditambahkan adalah dengan menghapusnya secara manual.
9. Buka salah satu dokumen dalam folder dengan nama **data_kelas.csv** dan pilih kelas yang ingin dihapus
10. Buka salah satu dokumen dalam folder dengan nama **jadwal_kelas.csv** dan pilih jadwal kelas yang ingin dihapus

## Library
- tkinter : untuk membuat aplikasi GUI. hal ini digunakan untuk membuat antarmuka pengguna grafis di aplikasi
- PIL (Pillow) : Library untuk memproses gambar. Disini digunakan untuk memanipulasi gambar background (bg.png)
- menu_utama, tampilkan_kelas, tampilkan_jadwal, tambah_kelas, tambah_jadwal : Merupakan modul-modul eksternal yang sudah dibuat yang menyediakan berbagai fungsi terkait tampilan dan pengelolaan data penjadwalan kelas

## Fungsi Utama dan Cara Kerjanya:
- Inisialisasi GUI:
  root = tk.Tk()
  root.title("Sistem Penjadwalan Kelas")
  root.geometry("600x400")
  bagian ini untuk membuat jendela utama (root) dari aplikasi dan memberikan judul 
  serta ukuran windows (600x400 piksel).
- Event Binding untuk Resize:
  root.bind('<configure>', lambda event: resize_image(event, bg_image_original))
  event ini menangani perubahan ukuran windows. ketika ukuran berubah, fungsi 
  resize_image() akan dipanggil untuk menyesuaikan ukuran gambar background agar 
  tetap sesuai dengan ukutan windows aplikasi.
- Memuat Gambar Background:
  bg_image_originial = Image.open("bg.png")
  gambar bg.png dimuat sebagai gambar background yang nantinya akan di tampilkan.
- Memulai Aplikasi
  root.mainloop()
  fungsinya adalah loop utama untuk menjaga agar aplikasi GUI tetap berjalan dan 
  menunggu interaksi selanjutnya
- Fungsi back_to_menu()
  def back_to_menu():
    main_menu(root, bg_image_original, lambda: tampilkan_kelas(root, bg_image_original, back_to_menu),
              lambda: tampilkan_jadwal_kelas(root, bg_image_original, back_to_menu), 
              lambda: tambah_kelas(root, bg_image_original, back_to_menu, add_background_to_window),
              lambda: tambah_jadwal_kelas(root, bg_image_original, back_to_menu, add_background_to_window),
              keluar_aplikasi)
hal ini digunakan untuk kembali ke menu utama. ketika dipanggil, fungsi ini akan memanggil main_menu dengan beberapa parameter fungsi lambda yang memungkinkan untuk berpindah antara tampilan kelas, jadwal, menambah kelas, dan menambah jadwal.
- fungsi keluar_aplikasi()
  def keluar_aplikasi():
      root.destroy()
  fungsi ini digunakan untuk keluar dari aplikasi

## Cara Menjalankan Program:
1. Persiapkan Semua File yang Diperlukan:
   - file gambar bg.png yang digunakan sebagai latar belakang aplikasi
   - modul-modul menu_utama, tampilkan_kelas, tampilkan_jadwal, tambah_kelas, dan 
     tambah_jadwal sudah ada dan berfungsi dengan benar, karena mereka akan 
     dipanggil di dalam kode utama
2. instalasi Dependencies:
   - harus mengintsal pustakal tkinter dam pillow
3. Jalankan Program melalui terminal

## Program Bekerja:
- program ini berkerja berdasarkan antarmuka grafis yang menggunakan tkinter sebagai library utama
- menu utama akan menampilkan berbagai opsi (seperti tampilan kelas, tampilan jadwal, dam penambahan data) yang dapat diakses dengan memilih opsi tertentu.
- gambar background akan ditampilkan menyesuaikan ukuran windows aplikasi dari fungsi resize_image()
- memilih untuk menambahkan kelas atau jadwal, fungsi terkait akan dipanggil dan aplikasi akan menampikan tampilan untuk memasukan data baru.
- fungi back_to_menu() memungkinkan untuk kembali ke menu kapan saja.
- fungsi keluar_aplikasi() untuk keluar dari aplikasi dengan menutup jendela utama.

## Kesimpulan
secara keseluruhan, kode ini merupakan bagian dari aplikasi sistem penjadwalan kelas berbasis GUI menggunakan tkinter. Program ini memungkinkan untuk melihat data kelas, melihat jadwal, serta menambah kelas dan jadwal baru. Aplikasi ini juga dilengkapi dengan fungsionalitas untuk menyesuaikan gambar background dan memungkinkan untuk kembali ke menu atau keluar dari aplikasi
  
  
