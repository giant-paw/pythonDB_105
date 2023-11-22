import tkinter as tk
import sqlite3

conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                    id INTEGER PRIMARY KEY,
                    nama_siswa TEXT,
                    biologi INTEGER,
                    fisika INTEGER,
                    inggris INTEGER,
                    prediksi_fakultas TEXT
                )''')
conn.commit()

def prediksi():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_fakultas = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_fakultas = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Belum bisa diprediksi"

    luaran_label.config(text=f"Hasil Prediksi: {prediksi_fakultas}")

    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))
    conn.commit()

window = tk.Tk()
window.geometry("400x450")

#create frame
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#create labels
label_nama = tk.Label(frame, text="Nama Siswa:")
label_biologi = tk.Label(frame, text="Nilai Biologi:")
label_fisika = tk.Label(frame, text="Nilai Fisika:")
label_inggris = tk.Label(frame, text="Nilai Inggris:")

#create entry
entry_nama = tk.Entry(frame)
entry_biologi = tk.Entry(frame)
entry_fisika = tk.Entry(frame)
entry_inggris = tk.Entry(frame)

#create label
PrediksiProdi = tk.Label(frame, text="Aplikasi Prediksi Fakultas")
luaran_label = tk.Label(frame, text="Hasil Prediksi: ")

tombol = tk.Button(frame, text="Submit Nilai", command=prediksi)

PrediksiProdi.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label_nama.grid(row=1, column=0, padx=10, pady=10)
entry_nama.grid(row=1, column=1, padx=10, pady=10)
label_biologi.grid(row=2, column=0, padx=10, pady=10)
entry_biologi.grid(row=2, column=1, padx=10, pady=10)
label_fisika.grid(row=3, column=0, padx=10, pady=10)
entry_fisika.grid(row=3, column=1, padx=10, pady=10)
label_inggris.grid(row=4, column=0, padx=10, pady=10)
entry_inggris.grid(row=4, column=1, padx=10, pady=10)
tombol.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
luaran_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
