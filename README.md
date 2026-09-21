Nama : Mirza
NPM : 2506618572
Kelas : PBP A

============ Deskripsi ============
Website portofolio pribadi Mirza Al Fathi, dibuat untuk menampilkan profil, riwayat pendidikan, pengalaman, dan lainnya. Proyek ini dibuat sebagai bagian dari tugas mata kuliah pemrograman berbasis platform menggunakan Django.

======= Pertanyaan Reflektif ======
### Tugas 1
1. Saat ini, elemen <article> dan <aside> belum saya diterapkan karena struktur halaman baru mencakup penambahan bagian Education. Penggunaan kedua elemen tersebut direncanakan pada tahap pengembangan berikutnya seiring dengan penambahan fitur-fitur baru.
2. Setiap elemen harus selalu diikuti dengan align-items dan juga display:flex agar bisa sesuai dengan layar manapun berapapun ukurannya.
3. Data tidak bisa terupdate secara real-time, nantinya mau bikin tombol like di portofolio lalu mengarah ke kontak saya. Saya juga mau menyimpan berapa banyak yang udh memencet tombol like.

### Tugas 2
1. Saat membuka halama portofolio, browser mengirim permintaan ke urls.py, lalu meneruskannya ke view. Kemudian, view mengambil data dari model yang ada di databse, lalu mengirimnya ke template untuk mengatur halaman. Setelah itu, hasilnya dikirim kembali ke browser beserta dengan data yang akhirnya ditampilkan sebagai satu halaman yang utuh.
2. Data protofolio sebaiknya disimpan di model karena model terhubung dengan database sedangkan template hanya untuk mengatur tampilan. Kalau data ditulis langsung di template, saat ada perubahan data, kita harus mengubah kode template satu per satu.
3. makemigration digunakan untuk mencaat perubahan pada model dan membuat file migrations, sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database.

### Tugas 3
1. ModelForm lebih baik digunakan daripada HTML manual karena field-fieldnya otomatis akan mengikuti model, jadi tidak perlu nulis ulang aturannya. Validasinya juga akan otomatis sesuai aturan di model. Selain itu, ModelForm juga akan selalu sinkron dengan modelnya. {% csrf_token %} digunakan untuk menjaga-jaga dari serangan CSRF. Token ini seperti kode yang akan dicek oleh Django tiap form disubmit, kalau memang tidak cocok ataupun tidak ada, requestnya akan ditolak.
2. JSON lebih disukai dibanding XML karena lebih simpel, tanpa tag pembuka-penutup. Browser juga dapat langsung membaca JSON tanpa tools lain, beda dengan XML yang butuh parser sendiri. Selain itu JSON lebih gampang dibaca dan telah menjadi standar hampir semua bahasa pemrograman untuk mengirim data lewat API.
3. Request masuk --> view yang sesuai dipanggil --> view ambil data dari database pakai Django. Tapi, data hasil ini masih berbentuk Python, bukan JSON. Nah, JSON hanya digunakan untuk tipe data yang bisa dibilang cukup sederhana seperti teks, angka, atau list, oleh karena itu kita harus melakukan serialization terlebih dahulu, lalu mengubah objek model jadi bentuk yang lebih sederhana (dictionary/list) pakai serializers.serialize(). Setelah itu, dibungkus jadi JsonResponse dan dikirim ke client biar bisa langsung dipakai/ditampilkan. Jadi serialization seperti jembatan antara Django dengan format JSON.

========= DEKLARASI AI ===========
Menggunakan Claude.ai
1. Menyempurnakan animasi typing pada teks judul, sebelumnya mengikuti tutorial youtube yang ternyata tidak dapat terintegrasi pada kode yang saya buat. AI dalam kasus ini dapat membantu tetapi masih kurang dalam penyesuaian lebar dan tinggi dalam animasinya sehingga cara mencocokkan kembali.
2. Membuat divider pada box dalam section education. 
3. Menyempurnakan halaman education dengan meminta menjelaskan tentang field dan model serta migrasi python
4. Meminta petunjuk kenapa data di shell tidak ada di PWS, tetapi tidak bisa terselesaikan masalahnya (https://claude.ai/share/543e5e64-f628-43cf-b186-3894275d15b3)
5. Membuat adjusting pada footer agar tidak terpotong dan meminta penjelasan form
