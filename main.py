
class Pracownik:
    
   def __init__(self, imie, pensja):
     self.imie = str(imie)
     self.pensja = int(pensja)

   def __repr__(self):
       return f"{self.imie} {self.pensja}"

   def __obliczanie_netto__(self):
       a = round(round(self.pensja * 0.0976,2) + round(self.pensja * 0.015,2) + round(self.pensja * 0.0245,2), 2)
       b = round(self.pensja-a,2)
       c = round(b*0.09, 2)
       e = round(b*0.0775, 2)
       f = round(111.25, 2)
       g = round(self.pensja - f - a, 2)
       h = round(g, 0)
       i = round(((h)*0.18)-46.33,2)
       j = round(i-e, 2)
       k = round(j, 0)
       self.pensjanetto = round((self.pensja - a - c - k), 2)
       return self.pensjanetto  
    
    def __obliczanie_skladki__(self):
        self.skladki = round(self.pensja *0.0976, 2) + round(self.pensja*0.065, 2) + round(self.pensja*0.0193,2) + round(self.pensja*0.0245,2) + round(self.pensja*0.001,2)
			return round(self.skladki, 2)

		def suma_koszt(self):
			self.koszt = self.pensja + round(self.pensja *0.0976,2) + round(self.pensja*0.065,2) + round(self.pensja*0.0193,2) + round(self.pensja*0.0245,2) + round(self.pensja*0.001,2)
			return round(self.koszt, 2)

		def suma_calkowity(self):
			return round(self.pensja + self.suma_skladki(),2)  
   def __skladki_pracodawcy__(self):
   def __laczny_koszt_na_pracownika__(self):




liczba_pracownikow = int(input())
pracownicy = []

for x in range (liczba_pracownikow):
    dane = input().split()
    imie = dane[0]
    pensja = int(dane[1])
    obiekt_pracownik = Pracownik(imie,pensja)
    pracownicy.append(obiekt_pracownik)
    
print(pracownicy)










        
