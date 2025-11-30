# 🥭 Klasifikasi Tingkat Kematangan Buah Pepaya

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)](https://opencv.org/)

---

## 🌟 Overview

Proyek **Klasifikasi Tingkat Kematangan Buah Pepaya** adalah sebuah solusi berbasis _Computer Vision_ yang dirancang untuk secara otomatis mengidentifikasi dan mengklasifikasikan tingkat kematangan buah pepaya. Sistem ini mampu membedakan pepaya ke dalam tiga kategori utama: **Mentah (Unripe)**, **Matang (Ripe)**, dan **Busuk (Spoiled)**.

Model ini dikembangkan menggunakan platform **Google Teachable Machine** dan diimplementasikan dengan kerangka kerja (framework) **TensorFlow** dan **OpenCV** di lingkungan Python. Tujuannya adalah untuk memberikan metode inspeksi kualitas yang cepat, konsisten, dan non-invasif, ideal untuk aplikasi Quality Control (QC) di industri pangan.



---

## ✨ Features

* **Klasifikasi 3-Tingkat:** Mengidentifikasi pepaya sebagai **Mentah**, **Matang**, atau **Busuk**.
* **_Real-Time_ Input:** Mendukung input video langsung dari **webcam** untuk klasifikasi instan.
* **Integrasi Model AI:** Menggunakan model _Deep Learning_ yang dilatih via **Teachable Machine** untuk akurasi tinggi.
* **Antarmuka Sederhana:** Tampilan output yang mudah dibaca, menunjukkan status klasifikasi secara langsung di _video feed_.

---

## 🛠️ Tech Stack

| Teknologi | Versi | Tujuan | Badge |
| :--- | :--- | :--- | :--- |
| **Python** | 3.10.0+ | Bahasa pemrograman utama. | [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/) |
| **TensorFlow** | 2.x | Kerangka kerja _Deep Learning_ untuk menjalankan model. | [![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/) |
| **OpenCV** | 4.x | Pustaka untuk pemrosesan gambar dan input webcam. | [![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)](https://opencv.org/) |
| **NumPy** | Terbaru | Pustaka komputasi numerik untuk operasi array. | [![NumPy](https://img.shields.io/badge/NumPy-latest-brightgreen.svg)](https://numpy.org/) |
| **Teachable Machine** | N/A | Platform untuk pelatihan model klasifikasi. | [![Teachable Machine](https://img.shields.io/badge/Teachable%20Machine-Google-yellow.svg)](https://teachablemachine.withgoogle.com/) |

---

## ⬇️ Installation

### Prerequisites

Pastikan Anda telah menginstal **Python 3.10.0** atau versi yang lebih baru di sistem Anda.

### Clone Repositori

```bash
git clone [https://github.com/Lyc-n/Klasifikasi_Tingkat_Kematangan_Buah_Pepaya](https://github.com/Lyc-n/Klasifikasi_Tingkat_Kematangan_Buah_Pepaya)
cd Klasifikasi_Tingkat_Kematangan_Buah_Pepaya
```

### Install Library

```bash
pip install tensorflow opencv-python numpy
```

### Jalankan Aplikasi

```bash
py cam.py
```

### Note

Untuk menghentikan aplikasi tekan 'q' pada keyboard