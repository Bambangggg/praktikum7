def cek_prima(angka):
    if angka > 1:
        for i in range(2, int(angka/2) + 1):
            if (angka % i) == 0:
                return False
        else:
            return True
    else:
        return False

bilangan = int(input("Masukkan bilangan: "))
if cek_prima(bilangan):
    print(bilangan, "adalah bilangan prima")
else:
    print(bilangan, "bukan bilangan prima")
