import customtkinter as ctk


ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self): 
        super().__init__()
        self.resizable(False, False)

        self.teraz_gra = "X"
        self.liczba_ruchow = 0

        self.napis_tura_gracza = ctk.CTkLabel(self, text=f"Teraz gra: {self.teraz_gra}", corner_radius=8,
                                              font=("Roboto", 40), fg_color="gray22")
        self.napis_tura_gracza.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="we")

        self.plansza = [""] * 9
        self.frame_plansza = ctk.CTkFrame(self)
        self.frame_plansza.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="we")

        self.button_width = 70
        self.button_height = 70

        self.guzik_1 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_1.configure(command=lambda: self.zaznacz_pole(1, self.guzik_1))
        self.guzik_1.grid(row=0, column=0, padx=3, pady=3)

        self.guzik_2 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_2.configure(command=lambda: self.zaznacz_pole(2, self.guzik_2))
        self.guzik_2.grid(row=0, column=1, padx=3, pady=3)

        self.guzik_3 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_3.configure(command=lambda: self.zaznacz_pole(3, self.guzik_3))
        self.guzik_3.grid(row=0, column=2, padx=3, pady=3)

        self.guzik_4 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_4.configure(command=lambda: self.zaznacz_pole(4, self.guzik_4))
        self.guzik_4.grid(row=1, column=0, padx=3, pady=3)

        self.guzik_5 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_5.configure(command=lambda: self.zaznacz_pole(5, self.guzik_5))
        self.guzik_5.grid(row=1, column=1, padx=3, pady=3)

        self.guzik_6 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_6.configure(command=lambda: self.zaznacz_pole(6, self.guzik_6))
        self.guzik_6.grid(row=1, column=2, padx=3, pady=3)

        self.guzik_7 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_7.configure(command=lambda: self.zaznacz_pole(7, self.guzik_7))
        self.guzik_7.grid(row=2, column=0, padx=3, pady=3)

        self.guzik_8 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_8.configure(command=lambda: self.zaznacz_pole(8, self.guzik_8))
        self.guzik_8.grid(row=2, column=1, padx=3, pady=3)

        self.guzik_9 = ctk.CTkButton(self.frame_plansza, width=self.button_width, height=self.button_height, text="", font=("Roboto", 30))
        self.guzik_9.configure(command=lambda: self.zaznacz_pole(9, self.guzik_9))
        self.guzik_9.grid(row=2, column=2, padx=3, pady=3)

    def zaznacz_pole(self, index: int, guzik: ctk.CTkButton):
        index -= 1
        if self.plansza[index] != "":
            return
        self.plansza[index] = self.teraz_gra
        self.liczba_ruchow += 1
        guzik.configure(text=str(self.teraz_gra), state="disabled", text_color_disabled="white")

        wynik = self.sprawdz_wynik()
        if wynik:
            self.napis_tura_gracza.configure(text=f"Wygrywa: {self.teraz_gra}")
            for guzik in self.frame_plansza.winfo_children():
                guzik.configure(state="disabled")
            return
        elif self.liczba_ruchow == 9:
            self.napis_tura_gracza.configure(text="Remis!")
            return

        if self.teraz_gra == "X":
            self.teraz_gra = "O"
        else:
            self.teraz_gra = "X"
        self.napis_tura_gracza.configure(text=f"Teraz gra: {self.teraz_gra}")

    def sprawdz_wynik(self) -> bool:
        """ Sprawdź poziomy """
        for i in range(0, 9, 3):
            if self.plansza[i] != "" and self.plansza[i] == self.plansza[i+1] and self.plansza[i+1] == self.plansza[i+2]:
                return True

        """ Sprawdź piony """
        for i in range(3):
            if self.plansza[i] != "" and self.plansza[i] == self.plansza[i+3] and self.plansza[i+3] == self.plansza[i+6]:
                return True

        if self.plansza[0] != "" and self.plansza[0] == self.plansza[4] and self.plansza[4] == self.plansza[8]:
            return True

        if self.plansza[2] != "" and self.plansza[2] == self.plansza[4] and self.plansza[4] == self.plansza[6]:
            return True

        return False

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = App()
    app.start()