
import contextlib

i = 19
path = r'C:\Users\bek\Desktop\FTPProjekt\testpython.txt'
file_path = 'randomfile.txt'
f = open(r'C:\Users\bek\Desktop\FTPProjekt\Rechnung - Kopie.txt')
f = f.read()
b = f.replace('\n', ';')
Elemente = b.split(';')
with open('filebeks.txt', 'w') as l:
    for y in Elemente:
        x = print(y, file=l)

with open(path, 'w') as w:
    print('\n\n\n\n' + Elemente[9], file=w)
    print(Elemente[10], file=w)
    print(Elemente[11] + '\n', file=w)
    print(Elemente[12], file=w)
    print('\n\n\n\nUster, ' + Elemente[3] + '                            ' + Elemente[16], file=w)
    print('                                                ' + Elemente[17], file=w)
    print('                                                ' + Elemente[18], file=w)
    print('\n' + 'Kundennummer:      ' + Elemente[8], file=w)
    print('Auftragsnummer:    ' + Elemente[1].split('_')[1], file=w)
    print('\n' + 'Rechnung Nr:       ' + Elemente[0].split('_')[1], file=w)
    print('-----------------------', file=w)
    loop_anzahl = int((len(Elemente) - 20) / 7)
    Total = 0
    for l in range(loop_anzahl):
        AnfangsZahl = Elemente[i+1]
        TitelRechnung = Elemente[i + 2]
        ZwischenZahl = Elemente[i+3]
        Betrag1 = Elemente[i+4]
        Betrag2 = Elemente[i+5]
        MWSTProzent = Elemente[i+6]
        Rechnungsline = '-----------'
        behan = ('  ' + AnfangsZahl + '   ' + TitelRechnung + '              '
                 + '      ' + Betrag1 + '      ' + Betrag2+ '      ' + MWSTProzent)
        Total += float(Betrag2)
        neymar = behan[45].replace(behan[45], Elemente[i + 3])
        teilstring = '                                   '
        teilstringformat = (teilstring.format(Elemente[i + 6].split('_')[1]))
        manena = behan[0:44] + neymar +"{:>11}".format(Betrag1) + "{:>5}".format('CHF') + "{:>12}".format(Betrag2) +\
                 "{:>7}".format(MWSTProzent.split('_')[1])
        print(manena, file=w)
        i = i + 7
    print("{:>73}".format(Rechnungsline),file=w)
    print( "{:>57}".format('Total CHF') + "{:>16}".format("{:.2f}".format(Total)),file=w)
    print('',file=w)
    print("{:>57}".format('MWST CHF'),file=w)







