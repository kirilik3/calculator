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
