#Fussballmannschaft

import random
import math

tor: list[str] = ["Neuer", "ter Stegen", "Trapp"]
abwehr: list[str] = ["Boateng", "Ginter", "Hector", "Hummels", "Ruediger", "Schulz", "Suele"]
mittelfeld: list[str] = ["Brandt", "Can", "Draxler", "Goretzka", "Guendogan", "Kroos", "Mueller", "Rudy"]
angriff: list[str] = ["Gnabry", "Reus", "Sane", "Werner"]

torwart = random.sample(tor, 1)
abwehrspieler = random.sample(abwehr, 4)


mittelfeldspieler = random.sample(mittelfeld, 4)
angreifer = random.sample(angriff, 2)

print("*** Team *** \n"
      f"Tor: {torwart} \n"
      f"Abwehr: {abwehrspieler} \n"
      f"Mittelfeld: {mittelfeldspieler} \n"
      f"Angriff: {angreifer} ")

#Kombinatorik: Kombination ohne Wdh
zufall1 = math.factorial(3) / (math.factorial(1) * math.factorial(3 - 1))
zufall2 = math.factorial(7) / (math.factorial(4) * math.factorial(7 - 4))
zufall3 = math.factorial(8) / (math.factorial(4) * math.factorial(8 - 4))
zufall4 = math.factorial(4) / (math.factorial(2) * math.factorial(4 - 2))

zufall = zufall1 * zufall2 * zufall3 * zufall4

print(f"Es sind {zufall} verschiedene Aufstellung möglich.")



