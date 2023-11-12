def ordinal (angka):
    angka_ordinal = angka[-1]
    if angka_ordinal == '1' :
        return "st"
    elif angka_ordinal == '2':
        return "nd"
    elif angka_ordinal == '3':
        return "th"
    elif angka_ordinal > '3':
        return "th"

def main ():
    ulang = "y"
    while ulang.lower() == "y":
        angka_biasa = input("masukkan angka:")
        hasil = ordinal(angka_biasa)
        print(f"({hasil}, {angka_biasa})")

        ulang = str(input("Ulang? (y/n) "))
        if ulang.lower() != "y" :
            break


main()
        
