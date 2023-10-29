
import PySimpleGUI as sg
from datetime import date
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
        
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']

        paigutus2 = [[sg.Text('Milker 0.1', text_color='black', font=("Helvetica", 12))],
                  [sg.Text('Mitu Liitrit?: ', size=(10,1)), sg.Slider(range=(0,31), orientation='h', size=(50,25), key='L')],
                  [sg.Text('Mis Firma?: ', size=(10,1)), sg.Listbox(values=('Tere', 'Alma', 'Pilos', 'Moloko', 'MixMax', 'Morozhno'), key='brand', size=(10, 6))],
                  [sg.Text('Mitu %?: ', size=(10,1)), sg.InputCombo(('0.2', '1', '2.5', '4.5', '5', '10'), size=(5,10), key='%')],
                  [sg.Text('_' * 80)],
                  [sg.Submit('Sisesta'), sg.Cancel('Välju')]]
   
        aken = sg.Window('2. aken: sünnipäev', paigutus2, size=(600,400))
        syndmus2, v22rtused2 = aken.read()
        
        if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Välju':
            break
        
        if syndmus2 == 'Sisesta':
            aken.close()
            
            liiter = int(v22rtused2['L'])
            firma = v22rtused2['brand']
            protsent = v22rtused2['%']
                      
            if firma == 'Tere':
                firma2 = 1
            elif firma == 'Alma':
                firma2 = 2
            elif firma == 'Pilos':
                firma2 = 3
            elif firma == 'Moloko':
                firma2 = 4
            elif firma == 'MixMax':
                firma2 = 5
            elif firma == 'Morozhno':
                firma2 = 6
            
          
            
                      
            paigutus3 = [[sg.Text('Tere, ' + eesnimi + '!')],
                       [sg.Text('Sulle on saadetud ' + str(liiter) + ' liitrit' + ', ' + str(protsent) + ' protsendist ' + str(firma) + ' piima aadressile ' + perekonnanimi)],
                       [sg.Submit('Välju')]]
            
            aken = sg.Window('Milker 0.1', paigutus3)
            syndmus3, v22rtused3 = aken.read()
            
            if syndmus3 == sg.WIN_CLOSED:
                break
            if syndmus3 == 'Välju':
                aken.close()             
                sg.Popup('Aitäh tellimuse eest!')
aken.close()