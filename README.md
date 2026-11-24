# Biodataku (Flask)

Project website sederhana yang dibuat untuk tugas perkuliahan. Awalnya website ini berupa halaman statis (HTML, CSS, Bootstrap, JavaScript) pada Tugas Individu 1-2, lalu diintegrasikan ke dalam aplikasi **Flask** pada Tugas Individu 6.

## Tentang Website

Website ini menampilkan informasi akademik seperti biodata, daftar mata kuliah beserta nilai, dan progress IP per semester. Pada versi Flask ditambahkan halaman **dashboard admin** untuk melihat ringkasan dan data dalam bentuk tabel.

## Yang Digunakan

* Python dan Flask untuk routing dan rendering template
* Jinja2 untuk template inheritance (`base.html`) dan menampilkan data dari Python
* HTML untuk struktur halaman
* CSS (dengan CSS variable) untuk tampilan dan tema
* Bootstrap 5 untuk grid, komponen, dan tampilan responsif
* JavaScript untuk fitur pencarian pada tabel di dashboard

## Fitur

* Semua halaman memakai template inheritance dari `base.html`
* CSS, JS, dan gambar dipanggil dengan `url_for('static', ...)`
* Navbar dengan menu aktif dinamis (memakai `request.endpoint`)
* Dashboard admin: sidebar, 3 stat card, dan tabel data dari list Python
* Tampilan responsif (sidebar admin diganti menu pill pada layar kecil)

## Halaman

| URL | Fungsi |
| --- | --- |
| `/` | Beranda |
| `/tentang` | Biodata (nama, NIM, angkatan) |
| `/nilai` | Tabel nilai mata kuliah dan IP semester |
| `/progress` | Progress bar IP per semester |
| `/admin` | Dashboard admin: stat card dan tabel mata kuliah |
| `/admin/semester` | Tabel data semester |

## Struktur Project

```text
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       └── background.jpg
└── templates/
    ├── base.html
    ├── index.html
    ├── tentang.html
    ├── nilai.html
    ├── progress.html
    ├── partials/
    │   └── navbar.html
    └── admin/
        ├── base_admin.html
        ├── dashboard.html
        └── semester.html
```

## Cara Menjalankan

1. Pastikan Python sudah terpasang.
2. Pasang Flask:

   ```
   pip install flask
   ```

3. Jalankan aplikasi dari folder yang berisi `app.py`:

   ```
   python app.py
   ```

4. Buka `http://127.0.0.1:5000` di browser.

Jika menggunakan Visual Studio Code, jalankan perintah di atas melalui terminal bawaan.

## Tujuan

Project ini dibuat sebagai latihan untuk memahami integrasi HTML dan CSS dengan Flask, mulai dari struktur folder `templates/` dan `static/`, template inheritance, sampai pembuatan halaman dashboard admin.

---

**Dibuat untuk keperluan tugas dan pembelajaran.**
