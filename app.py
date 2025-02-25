import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db',  
        user='root',
        password='root',
        database='siswa_db'
    )

# 🔹 READ - Tampilkan daftar siswa
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM siswa")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)

# 🔹 CREATE - Tambah siswa baru
@app.route('/add', methods=['POST'])
def add_student():
    nama = request.form['nama']
    kelas = request.form['kelas']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO siswa (nama, kelas) VALUES (%s, %s)", (nama, kelas))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 🔹 UPDATE - Edit data siswa
@app.route('/edit/<int:id>', methods=['POST'])
def edit_student(id):
    nama = request.form['nama']
    kelas = request.form['kelas']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE siswa SET nama=%s, kelas=%s WHERE id=%s", (nama, kelas, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 🔹 DELETE - Hapus siswa
@app.route('/delete/<int:id>', methods=['GET'])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM siswa WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
