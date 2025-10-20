from flask import Flask, render_template, request
import numpy as np
import random

app = Flask(__name__)

# --- Simulasi Model AI/ML sederhana ---
def talent_score(ipk, toefl, umur, universitas, jurusan):
    # bobot simulasi (bisa diganti dengan model logistic regression / random forest)
    base = 50
    base += (ipk - 2.5) * 10         # semakin tinggi IPK → skor naik
    base += (toefl - 400) / 10       # setiap 10 poin TOEFL → +1 skor
    base -= abs(25 - umur) * 0.8     # umur ideal sekitar 25 tahun
    if universitas.lower() in ['ui', 'ugm', 'itb', 'undip', 'unair', 'ipb', 'usu', 'its', 'unpad', 'ub']:
        base += 10                   # universitas top
    if "informatics" in jurusan.lower() or "management" in jurusan.lower():
        base += 5                    # jurusan relevan
    return max(0, min(100, round(base, 2)))  # batas 0–100

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form['nama']
    universitas = request.form['universitas']
    jurusan = request.form['jurusan']
    ipk = float(request.form['ipk'])
    toefl = int(request.form['toefl'])
    umur = int(request.form['umur'])

    skor = talent_score(ipk, toefl, umur, universitas, jurusan)
    status = "Lolos Seleksi" if skor >= 65 else "Belum Lolos"
    warna = "success" if skor >= 65 else "danger"

    return render_template('result.html', nama=nama, skor=skor, status=status, warna=warna)

if __name__ == '__main__':
    app.run(debug=True)