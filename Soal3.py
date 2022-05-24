'''Soal 3
Topik : Kalkulator Sederhana
Deskripsi : Anda diminta untuk membuat fungsi kalkulator sederhana dengan input 
            dalam bentuk string yang terdiri dari 3 bagian:
                - Operand 1 (angka maksimal 1 juta)
                - Operator (+, -, *, /)
                - Operand 2 (angka maksimal 1 juta)
            Antar operand dan operator akan dipisahkan oleh spasi. 
            Output dari aplikasi anda adalah hasil kalkulasi dari input yang diberikan.
            Method signature dari fungsi yang dibuat adalah sebagai berikut
                function kalkulator (string input) : integer
'''
def printError():
    print("Masukan salah. Tolong masukkan sesuai dengan format")
    print("Format : a operator b")
    print("operator : (/,+,-*)")
    print("Contoh: 2 + 5")
def kalkulator(m):
    if (m == ""):
        printError()
        return None
    splitted = m.split()
    if (not splitted[0].isnumeric() or not splitted[2].isnumeric()):
        printError()
        return None
    if len(splitted) != 3:
        printError()
        return None
    if (splitted[1] == "+"):
        return(int(splitted[0]) + int(splitted[2]))
    elif (splitted[1] == "-"):
        return(int(splitted[0]) - int(splitted[2]))
    elif (splitted[1] == "*"):
        return(int(splitted[0]) * int(splitted[2]))
    elif (splitted[1] == "/"):
        return(int(splitted[0]) / int(splitted[2]))
    else:
        return("Please input correct operator (/,+,-*)")

def main():
    print("Kalkulator Sederhana")
    print("Format : a operator b")
    print("Contoh : 2 + 5")
    print("Press E to exit")
    while True:
        m = input("")
        if (m == "E"):
            break
        else:
            answer = kalkulator(m)
        if (answer):
            print(answer)
main()