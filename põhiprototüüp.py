
import PySimpleGUI as sg
from datetime import date
#funktsioon hetkevanuse arvutamiseks
def arvuta_vanus(sünnipäev):
    täna = date.today()
    vanus = täna.year - sünnipäev.year - ((täna.month, täna.day) < (sünnipäev.month, sünnipäev.day))
    return vanus
sg.theme('BrownBlue')
paigutus = [[sg.Text('Milker 0.1', text_color='black', font=("Helvetica", 12))],
          [sg.Text('Sisestage nimi: ')],
          [sg.InputText(key="eesnimi")],
          [sg.Text('Sisestage aadress: ')],
          [sg.InputText(key="perekonnanimi")],
          [sg.Text('_' * 80)],
          [sg.Submit('Järgmine'), sg.Cancel('Välju')]]
aken = sg.Window('1. aken: nimi', paigutus, size=(600,400))
while True:
    syndmus, v22rtused = aken.read()

    if syndmus == sg.WIN_CLOSED or syndmus == 'Välju':
        break

    if syndmus == 'Järgmine':
        aken.close()
        
        #salvestame ees- ja perekonnanime muutujatesse
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
        #salvestame tervituse muutujasse
        
        #loome uue paigutuse uue akna jaoks
        #kasutame erinevaid elemente
        paigutus2 = [[sg.Text('Milker 0.1', text_color='black', font=("Helvetica", 12))],
                  [sg.Text('Mitu Liitrit?: ', size=(10,1)), sg.Slider(range=(0,31), orientation='h', size=(50,25), key='L')],
                  [sg.Text('Mis Firma?: ', size=(10,1)), sg.Listbox(values=('Tere', 'Alma', 'Pilos', 'Moloko', 'MixMax', 'Morozhno'), key='brand', size=(10, 6))],
                  [sg.Text('Mitu %?: ', size=(10,1)), sg.InputCombo(('0', '1', '2', '3', '4', '5'), size=(5,10), key='%')],
                  [sg.Text('_' * 80)],
                  [sg.Submit('Sisesta'), sg.Cancel('Välju')]]
   
        aken = sg.Window('2. aken: sünnipäev', paigutus2, size=(600,400))
        syndmus2, v22rtused2 = aken.read()
        
        #akna sulgemisel lõpetab programm töö
        if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Välju':
            break
        
        #kui vajutatakse nuppu 'Sisesta', pannakse põhiaken kinni ja avaneb uus aken
        if syndmus2 == 'Sisesta':
            aken.close()
            
            liiter = int(v22rtused2['L'])
            firma = v22rtused2['brand']
            protsent = int(v22rtused2['%'])
            
            #vastavalt kuule leiame selle kuu "järjekorranumbri", mida kasutame funktsioonis            
            if firma == 'Tere':
                firma2 = 1
            if firma == 'Alma':
                firma2 = 2
            if firma == 'Pilos':
                firma2 = 3
            if firma == 'Moloko':
                firma2 = 4
            if firma == 'MixMax':
                firma2 = 5
            if firma == 'Morozhno':
                firma2 = 6
            
          
            
            
            #loome uue paigutuse viimase akna jaoks, kus kuvame kogu informatsiooni            
            paigutus3 = [[sg.Text('Tere, ' + eesnimi + '!')],
                       [sg.Text('Sulle on saadetud ' + str(liiter) + ' liitrit' + ', ' + str(protsent) + ' protsendist ' + str(firma) + ' piima aadressile ' + perekonnanimi)],
                       [sg.Submit('Välju')]]
            
            aken = sg.Window('Milker 0.1', paigutus3)
            syndmus3, v22rtused3 = aken.read()
            
            #sulgemisel lõpetab programm töö
            if syndmus3 == sg.WIN_CLOSED:
                break
            #nuppu vajutades sulgub põhiaken ning avaneb hüpikaken
            if syndmus3 == 'Välju':
                aken.close()             
                sg.Popup('Aitäh tellimuse eest!')
aken.close()