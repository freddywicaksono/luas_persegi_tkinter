import tkinter as tk

def hitung_luas_keliling():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    
    luas_label.config(text=f"Luas: {luas}")
    keliling_label.config(text=f"Keliling: {keliling}")

app = tk.Tk()
app.title("Kalkulator Luas dan Keliling Persegi Panjang")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

panjang_label = tk.Label(frame, text="Panjang:")
panjang_label.pack()

panjang_entry = tk.Entry(frame)
panjang_entry.pack()

lebar_label = tk.Label(frame, text="Lebar:")
lebar_label.pack()

lebar_entry = tk.Entry(frame)
lebar_entry.pack()

hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_keliling)
hitung_button.pack()

luas_label = tk.Label(frame, text="Luas: ")
luas_label.pack()

keliling_label = tk.Label(frame, text="Keliling: ")
keliling_label.pack()

app.mainloop()