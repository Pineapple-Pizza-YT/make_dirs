import os

print('Ordnerstruktur wird erstellt.')

for i in range(31):
    ordner='D:\\Videobearbeitung\\drone\\30daychallange\\Tag_%s' %(i)
    os.makedirs(ordner)
    os.mkdir('D:\\Videobearbeitung\\drone\\30daychallange\\Tag_%s\\01_Projekt' %(i))
    os.mkdir('D:\\Videobearbeitung\\drone\\30daychallange\\Tag_%s\\02_Filmmaterial' %(i))
    os.mkdir('D:\\Videobearbeitung\\drone\\30daychallange\\Tag_%s\\03_Tonspuren' %(i))
    os.mkdir('D:\\Videobearbeitung\\drone\\30daychallange\\Tag_%s\\04_Musik' %(i))
    os.mkdir('D:\\Videobearbeitung\\drone\\30daychallange\\Tag_%s\\05_Bilder' %(i))
    os.mkdir('D:\\Videobearbeitung\\drone\\30daychallange\\Tag_%s\\06_Film' %(i))
    i+=1


