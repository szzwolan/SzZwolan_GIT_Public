import win32com.client as win32


def msgGenerate(report,issues):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Subject = "[US] Raport po " + report[0][0]

    probeHTML = " "
    partHTML = " "

    html = [" "]


    for i in range(0,len(issues)):
        if issues[i] == 0:
            #html.append(partHTMLGenerator(i+1, "Wymiana modułu trackball", "1hL3", "Trackball for VS8", "543234", partHTML))
            html.append(
                partHTMLGenerator(i + 1, report[i][5], report[i][7], report[i][6], report[i][8], partHTML))
        else:
           # html.append(probeHTMLGenerator(i+1, "Pęknięcie soczewki akustycznej w głowicy C1-5-RS", "C1-5-RS", "KTZ12345",probeHTML))
            html.append(
                probeHTMLGenerator(i + 1, report[i][5], report[i][6], report[i][8],
                                   probeHTML))





    # probeHTML = probeHTMLGenerator(1, "Pęknięcie soczewki akustycznej w głowicy C1-5-RS", "C1-5-RS", "KTZ12345",
    #                                probeHTML)
    # probeHTML = probeHTMLGenerator(2, "Pęknięcie okablowania strain relief w Głowicy RAB6-RS", "RAB6-RS", "KTZ54321",
    #                                probeHTML)
    # partHTML = partHTMLGenerator(3, "Wymiana modułu trackball", "1hL3", "Trackball for VS8", "543234", partHTML)

    mainHTML = "<HTML><BODY><p><u>Raport po:</u></p><table><tbody><tr><td style=text-align: left; width=120><p><strong>Dispatch: " \
               "</strong></p></td><td style=text-align: center; width=114><p>" + report[0][0] + "</p></td></tr><tr><td style=text-align: left; " \
                                                                                       "width=120><p><strong>Klient:</strong></p></td><td style=text-align: center; width=400><p>" + report[0][3] + "</p></td></tr>" \
                                                                                                                                                                                              "<tr><td style=text-align: left; width=120><p><strong>System ID:</strong></p></td><td style=text-align: center; " \
                                                                                                                                                                                              "width=114><p>" + report[0][1] + "</p></td></tr><tr><td style=text-align: left; width=120><p><strong>System:</strong></p></td>" \
                                                                                                                                                                                                                           "<td style=text-align: center; width=114><p>" + report[0][2] + "</p></td></tr><tr><td style=text-align: left; width=120>" \
                                                                                                                                                                                                                                                                                    "<p><strong>S/N:</strong></p></td><td style=text-align: center; width=114><p>" + report[0][4] + "</p></td></tr></tbody></table>" \
                                                                                                                                                                                                                                                                                                                                                                          "<p><strong>&nbsp;</strong></p>" \
                                                                                                                                                                                                                                                                                                                                                                          "<p><u>Zdiagnozowano:</u>"

    mail.HTMLBody = mainHTML

    for i in range(0,len(issues)):
        mail.HTMLBody += html[i+1]

    mail.Display(True)

def probeHTMLGenerator(index, problemDescription, probeName, probePN, probeHTML):
        probeHTMLvalue = "<table style=border-color: black; border=black><tbody><tr><td>" + str(
            index) + "." + "</td><td colspan=5>" + problemDescription + "</td></tr><tr><td>&nbsp;</td><td style=text-align: center;>CRU &nbsp;</td><td>" + probeName + "</td>" \
                                                                                                                                                                      "<td><b>P/N: " + probePN + "</b></td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>UNISYN:</td><td>Test YES Repair YES</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table><br>"
        probeHTML = probeHTML + probeHTMLvalue
        return probeHTML

def partHTMLGenerator(index, problemDescription, time, partName, partPN, partHTML):
        #partHTMLvalue = "<table border=black><tbody><tr><td>" + str(index) + "." + "</td><td colspan=5>" + problemDescription + "</td></tr><tr><td>&nbsp;</td><td style=text-align: center;>" + time + "&emsp;</td><td>" + partName + "</td>&emsp;<td><b>P/N: " + partPN + "</b></td></tr></tbody></table><br>"
        partHTMLvalue = "<table border=black><tr><td>" + str(index) + "." + "</td><td colspan=5>" + problemDescription + "</td></tr><tr><td>&nbsp;</td><td>" + time + "  &emsp;  " + partName + "  &emsp;  <b>P/N: " + partPN + "</b></td></tr></table><br>"
        partHTML = partHTML + partHTMLvalue
        return partHTML