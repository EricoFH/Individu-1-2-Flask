from flask import Flask, render_template

app = Flask(__name__)

PROFIL = [
    {"label": "Nama", "isi": "Erico Faizal Hakim"},
    {"label": "NIM", "isi": "1482500062"},
    {"label": "Angkatan", "isi": "2025"},
]

MATA_KULIAH = [
    {"no": 1, "nama": "Teknologi dan Aplikasi Bisnis Berkembang", "nilai": "AB"},
    {"no": 2, "nama": "Pemrograman Berorientasi Objek", "nilai": "A"},
    {"no": 3, "nama": "Arsitektur dan Organisasi Komputer", "nilai": "AB"},
    {"no": 4, "nama": "Sistem Basis Data", "nilai": "B"},
    {"no": 5, "nama": "Statistika dan Probabilitas", "nilai": "B"},
    {"no": 6, "nama": "Algoritma dan Struktur Data", "nilai": "AB"},
    {"no": 7, "nama": "Interaksi Manusia Komputer", "nilai": "AB"},
]

SEMESTER = [
    {"semester": 1, "ip": 3.67},
    {"semester": 2, "ip": 3.57},
]
IP_MAKSIMAL = 4.0

# persentase bar dihitung dari IP, bukan ditulis manual
for s in SEMESTER:
    s["persen"] = round(s["ip"] / IP_MAKSIMAL * 100, 1)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tentang")
def tentang():
    return render_template("tentang.html", profil=PROFIL)


@app.route("/nilai")
def nilai():
    return render_template("nilai.html",
                           mata_kuliah=MATA_KULIAH, semester=SEMESTER)


@app.route("/progress")
def progress():
    return render_template("progress.html", semester=SEMESTER)


@app.route("/admin")
def admin_dashboard():
    total = len(MATA_KULIAH)
    bagus = sum(1 for m in MATA_KULIAH if m["nilai"] in ("A", "AB"))
    rata_ip = round(sum(s["ip"] for s in SEMESTER) / len(SEMESTER), 2)

    statistik = [
        {"label": "Mata Kuliah", "nilai": total, "warna": "primary"},
        {"label": "Nilai A / AB", "nilai": bagus, "warna": "success"},
        {"label": "Rata-rata IP", "nilai": rata_ip, "warna": "warning"},
    ]
    return render_template("admin/dashboard.html",
                           statistik=statistik, mata_kuliah=MATA_KULIAH)


@app.route("/admin/semester")
def admin_semester():
    return render_template("admin/semester.html", semester=SEMESTER)


if __name__ == "__main__":
    app.run(debug=True)