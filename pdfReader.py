import pdfplumber
import re
import pdfBrowser
import mainGUI
import os

import win32com.client as win32

def pdfReader():
    filepath = pdfBrowser.search_for_file_path()
    filename = os.path.basename(filepath)
    print("AAAAAAAAAAAAAA: " + filepath)
    pdf = pdfplumber.open(filepath)
    page = pdf.pages[0]
    text = page.extract_text()


    Index_Klient_start = text.find('Klient')
    Index_Klient_stop = text.find('Nr systemu')

    Klient = text[Index_Klient_start+9:Index_Klient_stop].replace('\n','')


    table = page.extract_tables()

    a = []

    for row in table:
        a.append(row)

    row1 = a[0][1][0]
    row2 = a[1][0][0]

    PARow = a[1][7][0].replace('\n','')
    PerformedAction = PARow[PARow.find('Wykonane czynności')+22:len(PARow)]
    VRow = a[1][8][0].replace('\n','')
    Verification = VRow[VRow.find('Weryfikacja / Wykonane testy')+32:len(VRow)]

    Index_System_start = row2.find('System')
    Index_System_stop = row2.find('Nr Seryjny')

    System = row2[Index_System_start+9:Index_System_stop]


    row1_splited = re.split(" ",row1)
    row2_splited = re.split(" ",row2)

    RFS = row1_splited[7].replace('\n','')
    SystemID = row2_splited[3]
    SN = row2_splited[12]

    print("Klient: " + Klient)
    print("RFS: " + RFS)
    print("System: " + System)
    print("SystemID: " + SystemID)
    print("S/N: " + SN)
    print(PerformedAction)
    print(Verification)

    report = []
    report.append(filename)
    report.append(RFS)
    report.append(SystemID)
    report.append(System)
    report.append(SN)
    report.append(Klient)
    report.append(PerformedAction)
    report.append(Verification)

    return report
    #mainGUI.fillFields(mainGUI,report)

