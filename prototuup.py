import PySimpleGUI as sg
sg.theme('Dark Blue 3')
paigutus = [[sg.Text('Janune? Me aitame sind', text_color='white', font=('Helvetica', 15))],
      [sg.Text('Kui palju piima', size=(17, 1)), sg.Input()],
      [sg.Submit('Jah!'), sg.Cancel('Ei!')]]
aken = sg.Window('Arvutustehted', paigutus, size=(300,200))
while True:
    syndmus, v22rtused = aken.read()
    if syndmus == sg.WIN_CLOSED or syndmus == 'Sulge aken':
            break
    if syndmus == 'Jah!':
            aken.close()
        
            #teisendame sisendid täisarvudeks, et nendega saaks liitmistehet sooritada
            sisend1 = int(v22rtused[0])
        
            summa = sisend1
        
            #loome uue järjendi uute elementidega
            paigutus2 = [[sg.Text('Sisesta enda linnaosa nr: ', text_color='white', font=('Helvetica', 15))],
                  [sg.Text('Siia: ', size=(17, 1)), sg.InputText()],
                  [sg.Submit('LAHUTA!'), sg.Cancel('Sulge aken')]]
        
            #loome akna uue järjendiga
            aken = sg.Window('Andmed 2', paigutus2, size=(300,200))
        
            syndmus2, v22rtused2 = aken.read()
        
            #kui aken pandi kinni, lõpetab programm töö
            if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Sulge aken':
                break
        
            #kui vajutatakse nuppu 'LAHUTA!', pannakse aken kinni ja avatakse uus
            if syndmus2 == 'LAHUTA!':
            
              aken.close()
            
              #teisendame teisest aknast saadud sisendid arvudeks, et nendega saaks lahutustehet sooritada
              sisend3 = int(v22rtused2[0])
              sisend4 = int(v22rtused2[1])
            
              vahe = sisend3-sisend4
            
              #kuvame ekraanile sisendid ja arvutustehete vastused     mugaval kujul
              sg.Popup('Tehete vastused: ',
                 str(sisend1) + ' + ' + str(sisend2) + ' = ' + str(summa),
                 str(sisend3) + ' - ' + str(sisend4) + ' = ' + str(vahe))
        
aken.close()