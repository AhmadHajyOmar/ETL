
import requests
# --------------------------------------------------
#   Stage 1: Daten vom Webserver laden
#-----------------------------------------------------*/
# webserver
url = 'https://210301.de/b40/sensorcsvWS230312.php?s=66600014&D=231203'
ausgabe = "Datenquelle : " + url
print(ausgabe)
# Daten aus einer Datenquelle aus dem Internet laden (synchrones laden).
response = requests.get(url)
# --------------------------------------------------

#  Stage 2:  Rohdaten speichern.(rohdaten.txt oder rohdatengesamt.txt).
# Daten in der Variable ausgabe speichern
ausgabe = response.text
print("Daten: die erste 9 Zeilen aus der Datenquelle")
print(ausgabe[:500])
print("------------------------")
# erstelle die Datei rohdaten.txt mit dem Falg 'w' (Daten-Schreiben)
datei = open('rohdaten.txt', 'w')
# Schreibe die geladene Daten aus der Datenquelle in der text-datei "rohdaten"
datei.write(ausgabe)
# Datei schließen
datei.close()
print ("Daten in rohdaten.txt gespeichert")
# -----------------------------------------------------*/

# ----------------------------------------------

#  Stage 3:  Daten von lokal in Variablen laden.
# öffene die text-datei "rohdaten.txt"
dateiLaden = open("./rohdaten.txt")
# Variablen um die Daten aus der text-datei "rohdaten.txt" zu speichern
zeilen = " "
temp1 = ""
temp2 = ""

temp1Erste6Stunden = ""
temp1Zweite6Stunden = ""
temp1Dritte6Stunden = ""
temp1Vierte6Stunden = ""

temp2Erste6Stunden = ""
temp2Zweite6Stunden = ""
temp2Dritte6Stunden = ""
temp2Vierte6Stunden = ""
kennzahlen_content = ""

# eine boolische Variable "start", die welche Daten zu speicher sind entscheidet
start = False
for zeile in dateiLaden:
    if not zeile.__contains__("Zeit"):
        start = True
    if start:
        if zeile != '\n':
            zeilen += zeile.rstrip()
            kennzahlen_content += zeile.rstrip() + "\n"
            # die Zeit in der Format TT.MM.JJJJ SS:MM:SS von jeder Zeile speichern
            zeit = zeile.split(";")[2].split(" ")
            # die Stunde in der variable stunde speichern
            stunde = zeit[1].split(":")[0]
            # die stunde zu int (ganze Zahl) umwandeln
            stundeAlsGanzeZahl = int(stunde)
            # Temp1 in jeder Zeile speichern ( außerdem wird die Komma von , zu . umgewandelt)
            tempR1 = zeile.split(";")[4].replace(",", ".") + "|"
            # Temp2 in jeder Zeile speichern ( außerdem wird die Komma von , zu . umgewandelt)
            tempR2 = zeile.split(";")[6].replace(",", ".") + "|"
            # Temp1 für den ganzen Tag speichern
            temp1 += tempR1
            # Temp2 für den ganzen Tag speichern
            temp2 += tempR2

            # speichere Temp1 und Temp2 für die erste sechs Stunden
            if stundeAlsGanzeZahl >= 0 and stundeAlsGanzeZahl < 6:
                temp1Erste6Stunden += tempR1
                temp2Erste6Stunden += tempR2
            # speichere Temp1 und Temp2 für die zweite sechs Stunden
            if stundeAlsGanzeZahl >= 6 and stundeAlsGanzeZahl < 12:
                temp1Zweite6Stunden += tempR1
                temp2Zweite6Stunden += tempR2
            # speichere Temp1 und Temp2 für die driite sechs Stunden
            if stundeAlsGanzeZahl >= 12 and stundeAlsGanzeZahl < 18:
                temp1Dritte6Stunden += tempR1
                temp2Dritte6Stunden += tempR2
            # speichere Temp1 und Temp2 für die vierte sechs Stunden
            if stundeAlsGanzeZahl >= 18 and stundeAlsGanzeZahl < 24:
                temp1Vierte6Stunden += tempR1
                temp2Vierte6Stunden += tempR2

print("Daten aus der text-Datei \"rohdaten\" erfolgreich geladen.")

# Temp1 für den ganzen Tag als Liste speichern
temp1Liste = temp1.split("|")
temp1Liste.pop()
# Temp2 für den ganzen Tag als Liste speichern
temp2Liste = temp2.split("|")
temp2Liste.pop()
# Temp1 für die erste sechs Stunden als Liste speichern
temp1Erste6StundenListe = temp1Erste6Stunden.split("|")
temp1Erste6StundenListe.pop()
# Temp2 für die erste sechs Stunden als Liste speichern
temp2Erste6StundenListe = temp2Erste6Stunden.split("|")
temp2Erste6StundenListe.pop()
# Temp1 für die zweite sechs Stunden als Liste speichern
temp1Zweite6StundenListe = temp1Zweite6Stunden.split("|")
temp1Zweite6StundenListe.pop()
# Temp2 für die zweite sechs Stunden als Liste speichern
temp2Zweite6StundenListe = temp2Zweite6Stunden.split("|")
temp2Zweite6StundenListe.pop()
# Temp1 für die driite sechs Stunden als Liste speichern
temp1Dritte6StundenListe = temp1Dritte6Stunden.split("|")
temp1Dritte6StundenListe.pop()
# Temp2 für die driite sechs Stunden als Liste speichern
temp2Dritte6StundenListe = temp2Dritte6Stunden.split("|")
temp2Dritte6StundenListe.pop()
# Temp1 für die vierte sechs Stunden als Liste speichern
temp1Vierte6StundenListe = temp1Vierte6Stunden.split("|")
temp1Vierte6StundenListe.pop()
# Temp2 für die vierte sechs Stunden als Liste speichern
temp2Vierte6StundenListe = temp2Vierte6Stunden.split("|")
temp2Vierte6StundenListe.pop()
# die text-Datei "rohdaten.txt" schließen
dateiLaden.close()

# -----------------------------------------------------*/

# ----------------------------------------------

#  Stage 4: Kennzahlen berechnen

# Variablen für die Mittelwerte zu speichern
mittelwertTemp1 = 0
mittelwertTemp2 = 0

mittelwertTemp1Erste6Stunde = 0
mittelwertTemp1Zweite6Stunde = 0
mittelwertTemp1Dritte6Stunde = 0
mittelwertTemp1Vierte6Stunde = 0

mittelwertTemp2Erste6Stunde = 0
mittelwertTemp2Zweite6Stunde = 0
mittelwertTemp2Dritte6Stunde = 0
mittelwertTemp2Vierte6Stunde = 0

# eine For-Schleife für die summe von Temp1 und Temp2 für den ganzen Tag zu berechnen
for i in range(len(temp1Liste)):
    mittelwertTemp1 += float(temp1Liste[i])
    mittelwertTemp2 += float(temp2Liste[i])
# eine For-Schleife für die summe von Temp1 und Temp2 für die erste sechs stunden zu berechnen
for i in range(len(temp1Erste6StundenListe)):
    mittelwertTemp1Erste6Stunde += float(temp1Erste6StundenListe[i])
    mittelwertTemp2Erste6Stunde += float(temp2Erste6StundenListe[i])
# eine For-Schleife für die summe von Temp1 und Temp2 für die zweite sechs stunden zu berechnen
for i in range(len(temp1Zweite6StundenListe)):
    mittelwertTemp1Zweite6Stunde += float(temp1Zweite6StundenListe[i])
    mittelwertTemp2Zweite6Stunde += float(temp2Zweite6StundenListe[i])
# eine For-Schleife für die summe von Temp1 und Temp2 für die driite sechs stunden zu berechnen
for i in range(len(temp1Dritte6StundenListe)):
    mittelwertTemp1Dritte6Stunde += float(temp1Dritte6StundenListe[i])
    mittelwertTemp2Dritte6Stunde += float(temp2Dritte6StundenListe[i])
# eine For-Schleife für die summe von Temp1 und Temp2 für die virtte sechs stunden zu berechnen
for i in range(len(temp1Vierte6StundenListe)):
    mittelwertTemp1Vierte6Stunde += float(temp1Vierte6StundenListe[i])
    mittelwertTemp2Vierte6Stunde += float(temp2Vierte6StundenListe[i])

# Kennzahlen ausgeben und in variablen speichern
print("Kennzahlen: ")
mittelwertTemp1AlsString = "Tagesmittelwert Vorlauftemperatur (Temp1) am 03.12.2023 " + str(mittelwertTemp1/len(temp1Liste))
print(mittelwertTemp1AlsString)
mittelwertTemp2AlsString = "Tagesmittelwert Vorlauftemperatur (Temp2) am 03.12.2023 " + str(mittelwertTemp2/len(temp2Liste))
print(mittelwertTemp2AlsString)

mittelwertTemp1Erste6StundeAlsString ="Tagesmittelwert Vorlauftemperatur (Temp1) am 03.12.2023 von 00:00:00 bis 05:59:59 : " + str(mittelwertTemp1Erste6Stunde/len(temp1Erste6StundenListe))
print(mittelwertTemp1Erste6StundeAlsString)
mittelwertTemp2Erste6StundeAlsString ="Tagesmittelwert Vorlauftemperatur (Temp2) am 03.12.2023 von 00:00:00 bis 05:59:59 : " + str(mittelwertTemp2Erste6Stunde/len(temp2Erste6StundenListe))
print(mittelwertTemp2Erste6StundeAlsString)

mittelwertTemp1Zweite6StundeAlsString = "Tagesmittelwert Vorlauftemperatur (Temp1) am 03.12.2023 von 06:00:00 bis 11:59:59 : " + str(mittelwertTemp1Zweite6Stunde/len(temp1Zweite6StundenListe))
print(mittelwertTemp1Zweite6StundeAlsString)
mittelwertTemp2Zweite6StundeAlsString = "Tagesmittelwert Vorlauftemperatur (Temp2) am 03.12.2023 von 06:00:00 bis 11:59:59 : " + str(mittelwertTemp2Zweite6Stunde/len(temp2Zweite6StundenListe))
print(mittelwertTemp2Zweite6StundeAlsString)

mittelwertTemp1Dritte6StundeAlsString = "Tagesmittelwert Vorlauftemperatur (Temp1) am 03.12.2023 von 12:00:00 bis 17:59:59 : " + str(mittelwertTemp1Dritte6Stunde/len(temp1Dritte6StundenListe))
print(mittelwertTemp1Dritte6StundeAlsString)
mittelwertTemp2Dritte6StundeAlsString = "Tagesmittelwert Vorlauftemperatur (Temp2) am 03.12.2023 von 12:00:00 bis 17:59:59 : " + str(mittelwertTemp2Dritte6Stunde/len(temp2Dritte6StundenListe))
print(mittelwertTemp2Dritte6StundeAlsString)

mittelwertTemp1Vierte6StundeAlsString = "Tagesmittelwert Vorlauftemperatur (Temp1) am 03.12.2023 von 18:00:00 bis 23:59 : " + str(mittelwertTemp1Vierte6Stunde/len(temp1Vierte6StundenListe))
print(mittelwertTemp1Vierte6StundeAlsString)
mittelwertTemp2Vierte6StundeAlsString = "Tagesmittelwert Vorlauftemperatur (Temp2) am 03.12.2023 von 18:00:00 bis 23:59 : " + str(mittelwertTemp2Vierte6Stunde/len(temp2Vierte6StundenListe))
print(mittelwertTemp2Vierte6StundeAlsString)


# -----------------------------------------------------*/

# ----------------------------------------------

#  Stage 5: Kennzahlen speichern. (kennzahlen.txt)
# öffene die text-Datei "kennzahlen.txt"
datei = open('kennzahlen.txt', 'w')
# Liste um die kennzahlen zu speichern
kennzahlen = []
kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp1) 03.12.2023 = " + str((int) ((mittelwertTemp1/len(temp1Liste))*100)/100.0) +" C"
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp2) 03.12.2023 = " + str((int) ((mittelwertTemp2/len(temp2Liste))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp1) 03.12.2023 von 00:00:00 bis 05:59:59 = " + str((int) ((mittelwertTemp1Erste6Stunde/len(temp1Erste6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp2) 03.12.2023 von 00:00:00 bis 05:59:59 = " + str((int) ((mittelwertTemp2Erste6Stunde/len(temp2Erste6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp1) 03.12.2023 von 06:00:00 bis 11:59:59 = " + str((int) ((mittelwertTemp1Zweite6Stunde/len(temp1Zweite6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp2) 03.12.2023 von 06:00:00 bis 11:59:59 = " + str((int) ((mittelwertTemp2Zweite6Stunde/len(temp2Zweite6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp1) 03.12.2023 von 12:00:00 bis 17:59:59 = " + str((int) ((mittelwertTemp1Dritte6Stunde/len(temp1Dritte6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp2) 03.12.2023 von 12:00:00 bis 17:59:59 = " + str((int) ((mittelwertTemp2Dritte6Stunde/len(temp2Dritte6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp1) 03.12.2023 von 18:00:00 bis 23:59:59 = " + str((int) ((mittelwertTemp1Vierte6Stunde/len(temp1Vierte6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)
# neue Zeile in der text-Datei "kennzahlen.txt"
datei.write("\n")

kennzahlenMsg = "Tagesmittelwert Vorlauftemperatur (Temp2) 03.12.2023 von 18:00:00 bis 23:59:59 = " + str((int) ((mittelwertTemp2Vierte6Stunde/len(temp2Vierte6StundenListe))*100)/100.0) +" C"
# Kennzahlen in der text-Datei "kennzahlen.txt" speichern
datei.write(kennzahlenMsg)
# kennzahlen in Liste speichern
kennzahlen.append(kennzahlenMsg)

# Informiere der Anwender, dass die Kennzahken in der datei erfolgreich gespeichert wurden
print("Die Kennzahlen wurden erfolgreich schon in der Datei kennzahlen.txt gespeichert")
# schließe die text-Datei kennzahlen.txt
datei.close()
#
# -----------------------------------------------------*/

# ----------------------------------------------

#  Stage 6: Visualisierung - und speichern

# SVG-Frame
svg_frame = """<?xml version="1.0" standalone="no" ?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="720" height="360" viewBox="0 0 720 360"
 xmlns="http://www.w3.org/2000/svg"
 xmlns:xlink="http://www.w3.org/1999/xlink">
<desc>Temperature Mittelwert Diagramm</desc>
<!-- Hintergrund weiss -->
<rect x="0" y="0" width="720" height="360" rx="15" fill="white"></rect>
<!-- Achsen und Beschriftungen -->
<text x="90" y="350" fill="black">00-06</text>
<text x="270" y="350" fill="black">06-12</text>
<text x="450" y="350" fill="black">12-18</text>
<text x="630" y="350" fill="black">18-24</text>
<!-- y-Achse Beschriftung -->
<text x="10" y="10" fill="black">Temp ( C)</text>
<!-- Polyline fuer die Mittelwerte -->
<polyline points="#*1*#" fill="none" stroke="blue" stroke-width="2"/>
<polyline points="#*2*#" fill="none" stroke="green" stroke-width="2"/>
<!-- Linienbeschriftungen -->
<text x="650" y="50" fill="blue">Temp1</text>
<text x="650" y="70" fill="green">Temp2</text>
"#*3*#"
</svg>
"""


# Datenverarbeitung: Mittelwerte für Temp1 und Temp2 in verschiedenen Zeitintervallen
mittelwerte = {'00-06': {'Temp1': '', 'Temp2': ''},
               '06-12': {'Temp1': '', 'Temp2': ''},
               '12-18': {'Temp1': '', 'Temp2': ''},
               '18-24': {'Temp1': '', 'Temp2': ''}}


for line in kennzahlen:
    parts = line.split('=')
    time_part = parts[0].strip()
    temp_part = float(parts[1].split('C')[0].strip())
    # Bestimme, ob es sich um 'Temp1' oder 'Temp2' handelt
    temp_type = 'Temp1' if 'Temp1' in time_part else 'Temp2'
    # Überprüfe den Zeitbereich und speichere die Temperaturwerte im 'mittelwerte'-Dictionary
    if '00:00:00 bis 05:59:59' in time_part:
        mittelwerte['00-06'][temp_type] = float(temp_part)
    elif '06:00:00 bis 11:59:59' in time_part:
        mittelwerte['06-12'][temp_type] = float(temp_part)
    elif '12:00:00 bis 17:59:59' in time_part:
        mittelwerte['12-18'][temp_type] = float(temp_part)
    elif '18:00:00 bis 23:59:59' in time_part:
        mittelwerte['18-24'][temp_type] = float(temp_part)

# Polyline-Punkte für Temp1 und Temp2 erstellen
# Erzeuge Polyline-Punkte für Temp1 und Temp2
svgPointsMarker = ""
print("PolyLine (SVG): ")
polyline_points_temp1 = ""
polyline_points_temp2 = ""
for i, interval in enumerate(['00-06', '06-12', '12-18', '18-24']):
    # Skalierung auf der x-Achse
    x = i * 180 + 90
    # Skalierung auf der y-Achse für Temp1
    y_temp1 = 360 - mittelwerte[interval]['Temp1'] * 10
    # Skalierung auf der y-Achse für Temp2
    y_temp2 = 360 - mittelwerte[interval]['Temp2'] * 10
    # füge Punkt für Temp1 für SVG Fram hinzu
    polyline_points_temp1 += f"{x},{y_temp1} "
    # füge Punkt für Temp2 für SVG Fram hinzu
    polyline_points_temp2 += f"{x},{y_temp2} "
    # Ausgabe von jedem Punk auf de rKonsole
    print(f"{i+1}-te Punkt:")
    print(f"Temp1 : (X: {x}, Y: {y_temp1})")
    print(f"Temp2 : (X: {x}, Y: {y_temp2})")
    # erstellen Punkte und Beschriftung in der SVG Frame
    svgPointsMarker += f"<circle cx=\"{x}\" cy=\"{y_temp1}\" r=\"4\" fill=\"blue\" />"
    svgPointsMarker += f"<text x=\"{x+3}\" y=\"{y_temp1+5}\" fill=\"blue\">{mittelwerte[interval]['Temp1']}</text>"
    svgPointsMarker += f"<circle cx=\"{x}\" cy=\"{y_temp2}\" r=\"4\" fill=\"green\" />"
    svgPointsMarker += f"<text x=\"{x+3}\" y=\"{y_temp2+5}\" fill=\"green\">{mittelwerte[interval]['Temp2']}</text>"


# SVG Elemente in SVG Frame ersetzen
svg = svg_frame.replace("#*1*#", polyline_points_temp1.strip())
svg = svg.replace("#*2*#", polyline_points_temp2.strip())
svg = svg.replace("#*3*#", svgPointsMarker.strip())

# SVG-Datei speichern
svgFile = open('kennzahlen.svg', 'w')
# schreibe Daten (SVG Fram) in der Datei kennzahlen.svg
svgFile.write(svg)
# schließe die Datei
svgFile.close()
# Nutzer mitteilung, dass die SVG Frame in der Datei gespeichert wurde
print ("Daten in kennzahlen.svg gespeichert")
print ("----- fertig -----")

# -----------------------------------------------------*/
