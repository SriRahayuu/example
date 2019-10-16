import modulku

def main():
    # keliling segitiga
    s = 6

    keliling = modulku.kelilingsegitigasamasisi(s)

    print("KELILING SEGITIGA")
    print("sisi\t: ", s)
    print("keliling\t: ", keliling)


    # luas segitiga
    a = 2
    t = 6

    luas  = modulku.luassegitiga(a, t)

    print("LUAS SEGITIGA")
    print("alas\t: ", a)
    print("tinggi\t: ", t)
    print("luas\t: ", luas)

    #tinggi lingkaran
    a = 2
    l = 2

    tinggi = modulku.tinggisegitiga(l,a)

    print("TINGGI SEGITIGA")
    print("alas\t: ", a)
    print("luas\t: ", l)
    print("tinggi\t: ", tinggi)

if __name__ == "__main":
    main()
