def skaičiatuvas():
    print("Pasirinkite veiksmą:")
    print("1. Sudėtis")
    print("2. Atimtis")
    print("3. Daugyba")
    print("4. Dalyba")

    pasirinkimas = input("Įveskite pasirinkto veiksmo numerį (1/2/3/4): ")

	if pasirinkimas in ['1', '2', '3', '4']:
        	num1 = float(input("Įveskite pirmą skaičių: "))
        	num2 = float(input("Įveskite antrą skaičių: "))

		if pasirinkimas == '1':
            print(f"Rezultatas: {num1} + {num2} = {num1 + num2}")
        	elif pasirinkimas == '2':
            print(f"Rezultatas: {num1} - {num2} = {num1 - num2}")
        	elif pasirinkimas == '3':
            print(f"Rezultatas: {num1} * {num2} = {num1 * num2}")
        	elif pasirinkimas == '4':
                print(f"Rezultatas: {num1} / {num2} = {num1 / num2}")
    	else:
        	print("Neteisingas pasirinkimas. Bandykite dar kartą.")

skaičiatuvas()


def skaiciuotuvas(pasirinkimas, num1, num2):
    if pasirinkimas in ['1', '2', '3', '4']:
        if pasirinkimas == '1':
            return num1 + num2
        elif pasirinkimas == '2':
            return num1 - num2
        elif pasirinkimas == '3':
            return num1 * num2
        elif pasirinkimas == '4':
            if num2 == 0:
                raise ValueError("Negalima dalinti iš nulio.")
            return num1 / num2
    else:
        raise ValueError("Neteisingas pasirinkimas.")

def test_skaiciuotuvas():
    result = skaiciuotuvas('1', 5, 3)
    assert result == 8, f"Tikėtasi 8, bet gauta {result}"
    result = skaiciuotuvas('2', 5, 3)
    assert result == 2, f"Tikėtasi 2, bet gauta {result}"
    result = skaiciuotuvas('3', 5, 3)
    assert result == 15, f"Tikėtasi 15, bet gauta {result}"
    result = skaiciuotuvas('4', 6, 3)
    assert result == 2, f"Tikėtasi 2, bet gauta {result}"
    try:
        skaiciuotuvas('4', 6, 0)
        assert False, "Tikėtasi ValueError dėl dalinimo iš nulio"
    except ValueError as e:
        assert str(e) == "Negalima dalinti iš nulio.", f"Netikėta klaidos žinutė: {e}"
    try:
        skaiciuotuvas('5', 6, 3)
        assert False, "Tikėtasi ValueError dėl neteisingo veiksmo"
    except ValueError as e:
        assert str(e) == "Neteisingas pasirinkimas.", f"Netikėta klaidos žinutė: {e}"
    print("Visi testai praėjo sėkmingai.")

test_skaiciuotuvas()
