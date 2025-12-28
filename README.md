# 📊 Analisis Efisiensi Bubble Sort: Iteratif vs Rekursif

Project ini merupakan **Tugas Besar mata kuliah Analisis Kompleksitas Algoritma (AKA)** pada program studi **Informatika, Telkom University**. Fokus utama eksperimen ini adalah membandingkan performa *running time* antara pendekatan **Iteratif** (*Nested Loop*) dan **Rekursif** untuk algoritma pengurutan Bubble Sort.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## 🚀 Fitur Utama
- **Uji Coba Spesifik**: Menghitung waktu eksekusi untuk nilai masukan $n$ tertentu secara instan.
- **Visualisasi Grafik**: Menampilkan kurva pertumbuhan waktu untuk memverifikasi teori kompleksitas asimtotik.
- **Analisis Selisih**: Menghitung nilai $\Delta t$ (selisih waktu) antara kedua metode untuk melihat degradasi performa pada rekursi.

## 📝 Analisis Kompleksitas (Asymptotic Notation)
Berdasarkan tinjauan teoretis dalam studi AKA, berikut adalah analisis dari kedua metode yang diuji:

### 1. Pendekatan Iteratif (Nested Loop)
* **Kompleksitas Waktu**: Algoritma ini menggunakan dua lapis perulangan bersarang, sehingga dalam skenario terburuk (*worst case*) memiliki kompleksitas $O(n^2)$.
* **Kompleksitas Ruang**: Bersifat *in-place sorting* dengan kebutuhan memori tambahan sebesar $O(1)$.

### 2. Pendekatan Rekursif
* **Relasi Rekurens**: Hubungan waktu eksekusi didefinisikan sebagai $T(n) = T(n-1) + n$.
* **Kompleksitas Waktu**: Melalui metode substitusi atau *master theorem*, didapatkan kompleksitas asimtotik sebesar $O(n^2)$.
* **Kompleksitas Ruang**: Karena setiap pemanggilan fungsi membutuhkan *stack frame*, algoritma ini memiliki beban memori sebesar $O(n)$.



## 📈 Temuan Eksperimen
Meskipun secara teoretis keduanya memiliki kelas kompleksitas yang identik ($O(n^2)$), hasil eksperimen menunjukkan perbedaan signifikan pada nilai $n$ yang besar ($n > 5000$):
* **Overhead Rekursi**: Pemanggilan fungsi yang berulang pada rekursi menambah beban konstanta $c$ yang lebih besar dibandingkan iterasi biasa.
* **Stabilitas Sistem**: Pada nilai $n \approx 5000$, algoritma rekursif cenderung mencapai batas *stack depth* sistem, sementara iteratif tetap berjalan stabil hingga $n = 10000$.

## 🛠️ Cara Menjalankan
1. **Clone Repository**:
   ```bash
   git clone [https://github.com/Petriichor/Analisis-Kompleksitas-Algoritma-Iteratif-Nested-Loop-vs-Rekursif.git](https://github.com/Petriichor/Analisis-Kompleksitas-Algoritma-Iteratif-Nested-Loop-vs-Rekursif.git)
2. **Install Dependensi:**
    pip install -r requirements.txt
3. **Jalankan Aplikasi:**
    python app.py
4. **Akses Dashboard:**
    Buka https://127.0.0.1:500 pada browser Anda.



