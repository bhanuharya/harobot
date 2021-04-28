# Harobot! Your Personal Deadline Reminder
Harobot adalah sebuah chatbot yang dapat mencatat deadline tugas atau ujian. Chatbot ini dibuat dengan memanfaatkan algoritma
String Matching dan Regular Expression serta kakas pembantu seperti Flask, HTML, CSS, JavaScript, dan MySQL. 

# Ketentuan Penggunaan Chatbot
Untuk dapat menggunakan Harobot, pengguna perlu melakukan instalasi kakas Flask, MariaDB, dan MySQL connector
```Shell
pip install -U Flask
```
```Shell
pip install mysql-connector-python
```
Setelah semua sudah terpasang, jalankan chatbot dengan command
```python
run flask
```

## Ketentuan Format Penggunaan Chatbot
1. Menambah Task Baru
   1. Tanggal
      1. DD-MM-YYYY
      2. DD/MM/YYYY
   2. Kode Mata Kuliah
      1. Dua huruf diikuti oleh 4 angka (contoh: IF2211)
   3. Jenis Tugas
      1. Harus Merupakan salah satu dari 7 jenis task yang dapat dicatat
   4. Topik Tugas
      1. Penulisan topik tugas harus dikutip oleh petik satu atau petik dua
2. Melihat Daftar Task yang Harus Dikerjakan
   1. Tanggal
      1. DD-MM-YYYY
      2. DD/MM/YYYY
   2. Kode Mata Kuliah
      1. Dua huruf diikuti oleh 4 angka (contoh: IF2211)
   3. Jenis Tugas
      1. Harus Merupakan salah satu dari 7 jenis task yang dapat dicatat
   4. Topik Tugas
      1. Penulisan topik tugas harus dikutip oleh petik satu atau petik dua
   5. Perintah masukan mengandung "deadline" dan "apa saja". Contoh : "Ada deadline apa saja?"
3. Menampilkan Deadline Suatu Task
   1. Kode Mata Kuliah
      1. Dua huruf diikuti oleh 4 angka (contoh: IF2211)
   2. Jenis Tugas
      1. Harus Merupakan salah satu dari 7 jenis task yang dapat dicatat
   3. Topik Tugas
      1. Penulisan topik tugas harus dikutip oleh petik satu atau petik dua
   4. Perintah masukan mengandung "deadline", "kapan", dan kode mata kuliah yang valid. Contoh : "Deadline tugas IF2211 kapan?"
4. Memperbaharui Deadline Task
   1. Tanggal
      1. DD-MM-YYYY
      2. DD/MM/YYYY
   2. ID Task
      1. Berupa angka yang karakter sebelum dan sesudah angka adalah spasi (Contoh: 3 ) <- terdapat dua spasi di antara angka
5. Menandai Suatu Task Sudah Selesai Dikerjakan
   1. ID Task
      1. Berupa angka yang karakter sebelum dan sesudah angka adalah spasi (Contoh: 3 ) <- terdapat dua spasi di antara angka
6. Menampilkan Opsi Help
   1. Perintah masukan mengandung "bisa" dan "lakukan". Contoh : "Bot bisa lakukan apa?"

# Author
* 13519049 Dzaki Muhammad
* 13519203 Ramadhana Bhanuharya Wishnumurti
* 13519207 Rafidika Samekto