import contextlib
import os
from os import path
from datetime import datetime,timedelta
import logging
from zipfile import ZipFile

i = 19
f = open('Inputdata.data')
f = f.read()
b = f.replace('\n', ';')
Elemente = b.split(';')
newelemente = (len(Elemente) +1)
try:
        pathtxt = Elemente[8] + '_' + Elemente[0].split('_')[1] + '_invoice.txt'
        date1 = Elemente[3]
        datetime_obj = datetime.strptime(date1 , '%d.%m.%Y')
        AdddateNr = Elemente[5].split('_')[1]
        end_date = datetime_obj + timedelta(days=int(AdddateNr))
        EndDate = '('+ str(end_date.day) + '.' +  str(end_date.month) +'.' + str(end_date.year) + ')'

        with open(pathtxt, 'w') as w:
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
        zipObj.write(pathtxt)


except IndexError and NameError:

    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="logfile.log",
                        filemode="w",
                        format=Log_Format,
                        level=logging.ERROR)
    logger = logging.getLogger()
    logger.error("Unreadable")


XMLPath = 'XML.txt'
f = open('Inputdata.data')
f = f.read()
b = f.replace('\n', ';')
Elemente = b.split(';')
pathxml = Elemente[8] + '_' + Elemente[0].split('_')[1] + '_invoice.xml'
finalelemlen = (len(Elemente) + 1)
if finalelemlen >= 35 and (finalelemlen % 7 == 0):
    d = open(XMLPath)
    d = d.read()

    with open('filebeks.txt', 'w') as l:
        for y in Elemente:
            x = print(y, file=l)
    XMLlist = d.split('\n')
    date = (Elemente[3] + ' ' + Elemente[4])
    date_time = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    ts = datetime.timestamp(date_time)
    TsTrue = (str(ts)).split('.')[0]
    dateNoForm = Elemente[3]
    dateNoFormsplit = Elemente[3].split('.')
    DateForm = dateNoFormsplit[2] + dateNoFormsplit[1] + dateNoFormsplit[0]
    Rechnungsnummer = Elemente[0].split('_')[1]
    Auftragsnummer = Elemente[1].split('_')[1]

    loop_anzahl = int((len(Elemente) - 20) / 7)
    Total = 0
    i = 19
    for zja in range(loop_anzahl):
        Betrag2 = Elemente[i + 5]
        Total += float(Betrag2)
        i = i + 7
    TotalFormat = ("{:.2f}".format(Total).split('.')[0] + "{:.2f}".format(Total).split('.')[1]).rjust(10, '0')
    PayDays = Elemente[5].split('_')[1]
    Date_30 = date_time + timedelta(days=int(PayDays))
    Enddate_30 = (str(Date_30).split(' ')[0].split('-')[0] + str(Date_30).split(' ')[0].split('-')[1] +
                    str(Date_30).split(' ')[0].split('-')[2])
    Referenceday = str(int(PayDays) + 1)

    with open(pathxml, 'w') as w:
        XMLlist[3] = '      <Pid>' + Elemente[7] + '</Pid>'
        XMLlist[6] = '      <Pid>' + Elemente[15] + '</Pid>'
        XMLlist[18] = '          <Reference-No>' + TsTrue + '</Reference-No>'
        XMLlist[19] = '          <Date>' + DateForm + '</Date>'
        XMLlist[23] = '        <Date>' + DateForm + '</Date>'
        XMLlist[28] = '            <Reference-No>' + Rechnungsnummer + '</Reference-No>'
        XMLlist[29] = '            <Date>' + DateForm + '</Date>'
        XMLlist[34] = '            <Reference-No>' + Auftragsnummer + '</Reference-No>'
        XMLlist[35] = '            <Date>' + DateForm + '</Date>'
        XMLlist[46] = '            <Reference-No>' + TsTrue + '</Reference-No>'
        XMLlist[19] = '            <Date>' + DateForm + '</Date>'
        XMLlist[52] = '        <Tax-No>' + Elemente[12] + '</Tax-No>'
        XMLlist[55] = '          <Pid>' + Elemente[7] + '</Pid>'
        XMLlist[59] = '            <Line-35>' + Elemente[9] + '</Line-35>'
        XMLlist[60] = '            <Line-35>' + Elemente[10] + '</Line-35>'
        XMLlist[61] = '            <Line-35>' + Elemente[11] + '</Line-35>'
        XMLlist[83] = '          <Pid>' + Elemente[18] + '</Pid>'
        XMLlist[87] = '            <Line-35>' + Elemente[16] + '</Line-35>'
        XMLlist[88] = '            <Line-35>' + Elemente[17] + '</Line-35>'
        XMLlist[89] = '            <Line-35>' + Elemente[18] + '</Line-35>'
        XMLlist[108] = '        <Amount>' + TotalFormat + '</Amount>'
        XMLlist[
            133] = '            <Payment-Period Type="M" On-Or-After="1" Reference-Day="' + Referenceday + '">' + PayDays + '</Payment-Period>'
        XMLlist[134] = '            <Date>' + Enddate_30 + '</Date>'
        XMLlist[
            140] = '            <Payment-Period Type="M" On-Or-After="1" Reference-Day="' + Referenceday + '"></Payment-Period>'

        for n in XMLlist:
            print(n, file=w)
    zipObj.write(pathxml)
    zipObj.close()
else:
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="logfile.log",
                            filemode="w",
                            format=Log_Format,
                            level=logging.ERROR)
    logger = logging.getLogger()
    logger.error("Unreadable")
    if path.exists(pathxml):
        os.remove(pathxml)
    if path.exists(pathtxt):
        os.remove(pathtxt)





