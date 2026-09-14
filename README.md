Nama : Mirza
NPM : 2506618572
Kelas : PBP A

=== Pertanyaan Reflektif ===
### Tugas 1
1. Saat ini, elemen <article> dan <aside> belum saya diterapkan karena struktur halaman baru mencakup penambahan bagian Education. Penggunaan kedua elemen tersebut direncanakan pada tahap pengembangan berikutnya seiring dengan penambahan fitur-fitur baru.
2. Setiap elemen harus selalu diikuti dengan align-items dan juga display:flex agar bisa sesuai dengan layar manapun berapapun ukurannya.
3. Data tidak bisa terupdate secara real-time, nantinya mau bikin tombol like di portofolio lalu mengarah ke kontak saya. Saya juga mau menyimpan berapa banyak yang udh memencet tombol like.

### Tugas 2
1. Saat membuka halama portofolio, browser mengirim permintaan ke urls.py, lalu meneruskannya ke view. Kemudian, view mengambil data dari model yang ada di databse, lalu mengirimnya ke template untuk mengatur halaman. Setelah itu, hasilnya dikirim kembali ke browser beserta dengan data yang akhirnya ditampilkan sebagai satu halaman yang utuh.
2. Data protofolio sebaiknya disimpan di model karena model terhubung dengan database sedangkan template hanya untuk mengatur tampilan. Kalau data ditulis langsung di template, saat ada perubahan data, kita harus mengubah kode template satu per satu.
3. makemigration digunakan untuk mencaat perubahan pada model dan membuat file migrations, sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database.

### Tugas 3
1.

=== DEKLARASI AI =====
Menggunakan Claude.ai
1. Menyempurnakan animasi typing pada teks judul, sebelumnya mengikuti tutorial youtube yang ternyata tidak dapat terintegrasi pada kode yang saya buat. AI dalam kasus ini dapat membantu tetapi masih kurang dalam penyesuaian lebar dan tinggi dalam animasinya sehingga cara mencocokkan kembali.
2. Membuat divider pada box dalam section education. 
3. Menyempurnakan halaman education dengan meminta menjelaskan tentang field dan model serta migrasi python
4. Meminta petunjuk kenapa data di shell tidak ada di PWS, tetapi tidak bisa terselesaikan masalahnya (https://claude.ai/chat/ee3ff184-2845-4561-b186-19241d35a368)