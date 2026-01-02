# 📊 Analisis Efisiensi Deret Aritmetika: Iteratif vs Rekursif

Project ini merupakan **Tugas Besar mata kuliah Analisis Kompleksitas Algoritma (AKA)** pada program studi **Informatika, Telkom University**. Fokus utama eksperimen ini adalah membandingkan performa *running time* antara pendekatan **Iteratif** (menggunakan simulasi *Nested Loop*) dan **Rekursif** (Linear) untuk menyelesaikan masalah Penjumlahan Deret Aritmetika.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## 🚀 Fitur Utama
- **Uji Coba Spesifik**: Menghitung waktu eksekusi untuk nilai masukan $n$ tertentu (bebas input).
- **Visualisasi Grafik**: Menampilkan perbandingan kurva pertumbuhan waktu: Parabola (O(n^2)) vs Linear (O(n)).
- **Analisis Selisih**: Menghitung $\Delta t$ untuk melihat seberapa jauh efisiensi algoritma linear dibandingkan kuadratik.

## 📝 Analisis Kompleksitas (Asymptotic Notation)
Berdasarkan eksperimen dan tinjauan teoretis, berikut adalah analisis dari kedua metode yang diuji:

### 1. Pendekatan Iteratif (Nested Loop)
Algoritma ini diimplementasikan dengan logika penjumlahan bertahap (*counting by one*) di dalam loop.
* **Logika**: Untuk setiap suku ke-i, program melakukan perulangan sebanyak i kali untuk menambahkan nilai 1.
* **Kompleksitas Waktu**: Menggunakan dua lapis perulangan bersarang (*nested loop*), sehingga memiliki kompleksitas **Kuadratik O(n^2)**.
* **Kompleksitas Ruang**: Bersifat iteratif sederhana dengan kebutuhan memori konstan sebesar O(1).

### 2. Pendekatan Rekursif (Linear)
Algoritma ini menggunakan pemanggilan fungsi diri sendiri secara langsung.
* **Logika**: Menggunakan relasi rekurens $S(n) = \text{suku}_n + S(n-1)$.
* **Kompleksitas Waktu**: Fungsi dipanggil sebanyak $n$ kali dengan operasi konstan di setiap pemanggilan, menghasilkan kompleksitas **Linear $O(n)$**.
* **Kompleksitas Ruang**: Membutuhkan memori untuk *stack frame* sebanyak $n$ panggilan, sehingga kompleksitas ruang adalah $O(n)$.

## 📈 Temuan Eksperimen
Hasil pengujian menunjukkan perbedaan performa yang sangat signifikan, terutama pada nilai $n > 1000$:

* **Perbedaan Kelas Kompleksitas**: Grafik Iteratif melengkung ke atas (Parabola) karena beban kerja bertambah secara kuadratik, sedangkan grafik Rekursif berbentuk garis lurus (Linear).
* **Kemenangan Rekursif**: Meskipun metode rekursif memiliki *overhead* memori (*stack*), efisiensi algoritma $O(n)$ membuatnya **jauh lebih cepat** dibandingkan metode iteratif yang dipaksa bekerja pada $O(n^2)$.
* **Kesimpulan**: Pemilihan algoritma yang tepat (Linear vs Kuadratik) memiliki dampak yang jauh lebih besar terhadap performa dibandingkan sekadar overhead pemanggilan fungsi.

## 🛠️ Cara Menjalankan
1. **Clone Repository**:
   ```bash
   git clone [https://github.com/Petriichor/Analisis-Kompleksitas-Algoritma-Iteratif-Nested-Loop-vs-Rekursif.git](https://github.com/Petriichor/Analisis-Kompleksitas-Algoritma-Iteratif-Nested-Loop-vs-Rekursif.git)

2. **Install Dependensi**:
   ```bash
   pip install -r requirements.txt
4. **Jalankan Aplikasi**:
   ```bash
   python app.py
6. **Akses Dashboard**:
   Buka http://127.0.0.1:5000 pada browser Anda.
