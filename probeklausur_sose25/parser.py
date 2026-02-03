def parse_weight(str_input: str) -> tuple[float, str]:
    str_input = str_input.strip()

    for unit in ["kg", "mg", "g"]: #die längste Einheit zuerst prüfen, sonst erkennt das Programm nur "g" ung gibt Fehlermeldung

        if str_input.endswith(unit):
            zahl = str_input[:-len(unit)].strip()

            try:
                value = float(zahl)
                return value, unit

            except ValueError:
                raise ValueError("Ungültiges Zahlenformat.")

    raise ValueError("Ungültige Einheit.")


def normalize(start_weight: tuple[float, str], target_unit: str) -> tuple[float, str]:
    value, unit = start_weight

    if unit == "kg":
        zahl = value * 1000

    elif unit == "g":
        zahl = value

    elif unit == "mg":
        zahl = value / 1000

    else:
        raise ValueError("Ungültige Einheit.")


    if target_unit == "kg":
        return zahl / 1000, "kg"

    elif target_unit == "g":
        return zahl, "g"

    elif target_unit == "mg":
        return zahl * 1000, "mg"

    else:
        raise ValueError("Ungültige Zieleinheit.")



def add(weight1: str, weight2: str) -> tuple[float, str]:
    w1 = parse_weight(weight1)
    w2 = parse_weight(weight2)

    w2_norm = normalize(w2, w1[1])

    return w1[0] + w2_norm[0], w1[1]