import xlrd
loc = ("Excel.xlsx")

def excelReader(probe):

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(6)
    sheet.cell_value(0, 0)
    probeCapa = []
    probeCapa.append(None)


    for i in range(sheet.nrows):
        probeName = sheet.cell_value(i,2)
        if probeName == probe:
            probeCapa.clear()
            probeCapa.append("")
            print("mam cię!: " +str(i+1))
            b = sheet.row_values(i,0,74)
            print(sheet.row_values(1,0,74))
            c = sheet.row_values(1,0,74)
            print(sheet.row_values(i,0,74))

            unisynStatus = b[0]
            console = b[4]
            indexList = []

            for i in range(0,74):
                d = b[i]
                if d == "YES":
                    indexList.append(i)
                    probeCapa.append(c[i])

            #print(indexList)
            print(probeCapa)
            break
        else:
            #probeCapa[0] = "None"
            unisynStatus = "                    "
            console = "Probe missing in UNISYN excel file"

    return probeCapa,unisynStatus,console
        #print(sheet.cell_value(i, 2))