from datetime import datetime
import contextlib
from datetime import datetime,timedelta

path = 'testpython - Copy.txt'
XMLPath = 'XML.txt'
f = open('Inputdata.data')
f = f.read()
b = f.replace('\n', ';')
Elemente = b.split(';')
d = open(XMLPath)
d = d.read()

with open('filebeks.txt', 'w') as l:
    for y in Elemente:
        x = print(y, file=l)
XMLlist = d.split('\n')
date = (Elemente[3] + ' '+ Elemente[4])
date_time = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
ts = datetime.timestamp(date_time)
TsTrue = (str(ts)).split('.')[0]
dateNoForm = Elemente[3]
dateNoFormsplit = Elemente[3].split('.')
DateForm = dateNoFormsplit[2]+ dateNoFormsplit[1]+ dateNoFormsplit[0]
Rechnungsnummer = Elemente[0].split('_')[1]
Auftragsnummer = Elemente[1].split('_')[1]

loop_anzahl = int((len(Elemente) - 20) / 7)
Total = 0
i = 19
for zja in range(loop_anzahl):
    Betrag2 = Elemente[i + 5]
    Total += float(Betrag2)
    i = i + 7
TotalFormat = ("{:.2f}".format(Total).split('.')[0] + "{:.2f}".format(Total).split('.')[1]).rjust(10,'0')
PayDays = Elemente[5].split('_')[1]
Date_30 = date_time + timedelta(days=int(PayDays))
Enddate_30 = (str(Date_30).split(' ')[0].split('-')[0] + str(Date_30).split(' ')[0].split('-')[1] +
              str(Date_30).split(' ')[0].split('-')[2])
Referenceday = str(int(PayDays) + 1)


with open(path, 'w') as w:
    XMLlist[3] = '      <Pid>' + Elemente[7]+'</Pid>'
    XMLlist[6] = '      <Pid>' + Elemente[15]+'</Pid>'
    XMLlist[18] = '          <Reference-No>'+TsTrue+'</Reference-No>'
    XMLlist[19] = '          <Date>'+DateForm+'</Date>'
    XMLlist[23] = '        <Date>'+DateForm+'</Date>'
    XMLlist[28] = '            <Reference-No>'+Rechnungsnummer+'</Reference-No>'
    XMLlist[29] = '            <Date>'+DateForm+'</Date>'
    XMLlist[34] = '            <Reference-No>'+Auftragsnummer+'</Reference-No>'
    XMLlist[35] = '            <Date>'+DateForm+'</Date>'
    XMLlist[46] = '            <Reference-No>' + TsTrue + '</Reference-No>'
    XMLlist[19] = '            <Date>' + DateForm + '</Date>'
    XMLlist[52] = '        <Tax-No>'+Elemente[12]+'</Tax-No>'
    XMLlist[55] = '          <Pid>'+Elemente[7]+'</Pid>'
    XMLlist[59] = '            <Line-35>'+Elemente[9]+'</Line-35>'
    XMLlist[60] = '            <Line-35>' + Elemente[10] + '</Line-35>'
    XMLlist[61] = '            <Line-35>' + Elemente[11] + '</Line-35>'
    XMLlist[83] = '          <Pid>'+Elemente[18]+'</Pid>'
    XMLlist[87] = '            <Line-35>'+Elemente[16]+'</Line-35>'
    XMLlist[88] = '            <Line-35>' + Elemente[17] + '</Line-35>'
    XMLlist[89] = '            <Line-35>' + Elemente[18] + '</Line-35>'
    XMLlist[108] = '        <Amount>'+TotalFormat+'</Amount>'
    XMLlist[133] = '            <Payment-Period Type="M" On-Or-After="1" Reference-Day="'+Referenceday+'">' + PayDays + '</Payment-Period>'
    XMLlist[134] = '            <Date>'+Enddate_30+'</Date>'
    XMLlist[140] = '            <Payment-Period Type="M" On-Or-After="1" Reference-Day="'+Referenceday+'"></Payment-Period>'

    for n in XMLlist:
        print(n,file=w)
