import contextlib
import os
from datetime import datetime,timedelta
import logging
from zipfile import ZipFile

i = 19
f = open('Inputdata.data')
f = f.read()
b = f.replace('\n', ';')
Elemente = b.split(';')
newelemente = (len(Elemente) +1)
path = Elemente[8] + '_' + Elemente[0].split('_')[1] + '_invoice.txt'
try:


        date1 = Elemente[3]
        datetime_obj = datetime.strptime(date1 , '%d.%m.%Y')
        AdddateNr = Elemente[5].split('_')[1]
        end_date = datetime_obj + timedelta(days=int(AdddateNr))
        EndDate = '('+ str(end_date.day) + '.' +  str(end_date.month) +'.' + str(end_date.year) + ')'

        with open(path, 'w') as w:
            print('\n\n\n\n' + Elemente[9], file=w)
            print(Elemente[10], file=w)
            print(Elemente[11] + '\n', file=w)
            print(Elemente[12], file=w)
            print('\n\n\n\n'+Elemente[11].split(' ')[1] +', '+'den ' + Elemente[3]  + "{:>39}".format(Elemente[16]), file=w)
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
                manena1 = '  '+AnfangsZahl + '   '+TitelRechnung
                langeabstand = 45 - len(manena1)
                beksabs = ''
                for bn in range(langeabstand):
                    beksabs += ' '
                manena2 = manena1 + beksabs
                neymar = behan[45].replace(behan[45], Elemente[i + 3])
                manena = manena2 + neymar +"{:>11}".format(Betrag1) + "{:>5}".format('CHF') + "{:>12}".format(Betrag2) +\
                     "{:>7}".format(MWSTProzent.split('_')[1])
                print(manena, file=w)
                i = i + 7
            zeh = ("{:.2f}".format(Total))
            print("{:>74}".format(Rechnungsline),file=w)
            print( "{:>58}".format('Total CHF') + "{:>16}".format("{:.2f}".format(Total)),file=w)
            print('',file=w)
            print("{:>57}".format('MWST CHF'),file=w)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nZahlungsziel ohne Abzug 30 Tage'+ "{:>13}".format(EndDate),file=w)
            print('\nEinzahlungsschein',file=w)
            print("\n\n\n\n\n\n\n\n\n\n\n\n{:>8}".format(zeh.split('.')[0])+"{:>2}".format('.')+"{:>3}".format(zeh.split('.')[1])
            +"{:>24}".format(zeh.split('.')[0])+"{:>2}".format('.')+"{:>3}".format(zeh.split('.')[1])+
            "     "+(Elemente[16]),file=w)
            print("                                               " + (Elemente[17]),file=w)
            print("{:>19}".format('0 00000 00000 00000')+"                            "+Elemente[18],file=w)
            print("\n"+ Elemente[16],file=w)
            print(Elemente[17],file=w)
            print(Elemente[18],file=w)
        zipObj = ZipFile(r'C:\Users\bek\Desktop\FTPprj-main\Abgabe.zip', 'w')
        zipObj.write(path)
        zipObj.close()

except IndexError:

    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="logfile.log",
                        filemode="w",
                        format=Log_Format,
                        level=logging.ERROR)
    logger = logging.getLogger()
    logger.error("Unreadable")
    os.remove(path)






