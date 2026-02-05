text: str = """Ein kleiner Mann mit einem Spitzbart wartet im Vorzimmer einer Künstleragentur. Endlich wird er beim Direktor vorgelassen. Dieser thront in seinem Büro und raucht eine Zigarre.
Direktor: Was kann ich für Sie tun?
Kleiner Mann: Ich möchte mich gerne um einen Job bewerben.
Direktor: Ja, was können Sie denn?
Kleiner Mann: Ich kann Vögel imitieren.
Zirkusdirektor: Haben Sie eine Ahnung, wie viele Pfeifen hier jeden Tag reinkommen, die glauben, nur weil sie „Piep, Piep, Piep, …“ machen können, hätte ich jetzt einen Job für sie? Das letzte was ich brauche ist ein Vogelstimmen Imitator. Fort mit Ihnen!"""
print(text)
print("\nAnzahl von 'ich' wenn:")

print("der Text normal geschrieben wäre: ", text.count("ich"))

t1 = text.lower()

print("der Text klein geschrieben wäre:", t1.count("ich"))

