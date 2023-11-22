import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Teendok:
    def __init__(self, ablak):
        self.ablak = ablak
        self.ablak.title("Teendők")

        self.feladatok = []


        menusor = tk.Menu(ablak)
        szerkesztes = tk.Menu(menusor)
        ablak.config(menu=menusor)
        kilepes = tk.Menu(menusor)

        menusor.add_cascade(label='Szerkesztés', menu=szerkesztes)
        szerkesztes.add_command(label='Feladat hozzáadása', command=self.feladat_ad)
        szerkesztes.add_command(label='Feladat törlése', command=self.feladat_torles)
        menusor.add_cascade(label='Kilépés', menu=kilepes)
        kilepes.add_command(label='Kilépés', command=ablak.destroy)


        self.feladat_mezo = tk.Entry(ablak, width=40)


        self.hozzaad_gomb = tk.Button(ablak, text="Feladat hozzáadása", command= self.feladat_ad)
        self.feladat_lista = tk.Listbox(ablak, width=40)
        self.torles_gomb = tk.Button(ablak, text="Feladat törlése", command=self.feladat_torles)
        self.kilepes_gomb = tk.Button(ablak, text="Kilépés", command=self.Kilepes)


        self.feladat_mezo.grid(row=0, column=0, pady=10, columnspan=2)
        self.hozzaad_gomb.grid(row=1, column=0, pady=10, sticky="w")
        self.feladat_lista.grid(row=2, column=0, pady=10, columnspan=2)
        self.torles_gomb.grid(row=3, column=0, pady=10, sticky="w")
        self.kilepes_gomb.grid(row=3, column=1, pady=10, sticky="e")

        self.ablak.mainloop()

    def feladat_ad(self):
        feladat = self.feladat_mezo.get()
        if feladat:
            idopont = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            idopont_feladat = f"{idopont} - {feladat}"
            self.feladatok.append(idopont_feladat)
            self.feladat_lista.insert(tk.END, idopont_feladat)
            self.feladat_mezo.delete(0, tk.END)


    def feladat_torles(self):
        kijelolt_sor = self.feladat_lista.curselection()
        if kijelolt_sor:
            megerosit = messagebox.askyesno(title="Törlés", message="Biztos törli?")
            if megerosit:
                feladat_sorszama = kijelolt_sor[0]
                torolt_feladat = self.feladatok.pop(feladat_sorszama)
                self.feladat_lista.delete(feladat_sorszama)
                messagebox.showinfo("Feladat törölve", f"A feladat '{torolt_feladat}' törölve lett.")
        else:
            messagebox.showwarning("Törlés", "Válaszd ki a törölni kívánt feladatot.")


    def Kilepes(self):
        megerosit = messagebox.askyesno(title="Kilépés", message="Biztos kilép?")
        if megerosit is not None:
            if megerosit:
                self.ablak.destroy()



if __name__ == "__main__":
    ablak = tk.Tk()
    app = Teendok(ablak)
