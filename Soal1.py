'''Soal 1: 
Topik : urutkan data.
Deskripsi : Anda diminta mengurutkan data produk dengan bentuk seperti dibawah ini :

nama          |  harga  | rating | likes |
indomie       |   3000  |    5   |  150  |
Laptop        | 4000000 |   4.5  |  123  |
Aqua          |   3000  |    4   |  250  |
Smart TV      | 4000000 |   4.5  |   42  |
Headphone     | 4000000 |   3.5  |   90  |
Very Smart TV | 4000000 |   3.5  |   87  |

Urutkan array di atas dengan prioritas sebagai berikut :
    1. harga ascending
    2. rating descending
    3. like descending
'''
#Kode :
import csv


def mySort(data):
    data.sort(key= lambda x: (x[1], -x[2], -x[3]))

def printData(data):
    print ("sorted Data : ")
    for i in range (len(data)):
        print (data[i][0], data[i][1], data[i][2], data[i][3])

def importData(fileName):
    data = []
    if fileName.endswith('.csv'):
        with open(fileName, 'r') as f :
            file = csv.reader(f)
            next(file)
            # print ("euy")
            for row in file :
                temp = []
                temp.append (row[0])
                temp.append (int(row[1]))
                temp.append (float(row[2]))
                temp.append (int(row[3]))
                data.append(temp)
                del(temp)
            return data

filenm = "contoh.csv"
data = importData(filenm)
mySort(data)
print (data)