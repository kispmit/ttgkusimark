import PySimpleGUI as sg
#theme asemel kasutame:
sg.ChangeLookAndFeel('TanBlue')
#et näha kõiki teemade variante, võid need ekraanile kuvada:
#print(sg.ListOfLookAndFeelValues())

paigutus = [[sg.Text('Näited erinevatest nuppudest ja väljadest!', size=(35, 1), justification='left', font=("Helvetica", 15))],
            [sg.Frame('Soovid Milki? ', [[sg.Column(veerud)]])],
            [sg.Text('_' * 80)],
            [sg.Checkbox('JAH!!!'),  sg.Checkbox('Ei, mul on laktoositalumatus ja ma situn kõik täis kui piima joon.')],
            [sg.Submit('Järgmine'), sg.Cancel('Välju')]]
aken = sg.Window('Palju erinevaid vidinaid!', paigutus, size=(600,700), default_element_size=(40, 1), grab_anywhere=False)

while True:
    syndmus, v22rtused = aken.read()
    #kui aken pannakse kinni, lõpetab programm töö
    if syndmus == sg.WIN_CLOSED or syndmus == 'Välju':
        break
    #kui vajutatakse nuppu 'Järgmine', pannakse põhiaken kinni ja avaneb uus aken
    if syndmus == 'Järgmine':
        aken.close()
            
            paigutus2 = [[sg.Text('Vali Linnaosa: ', size=(11,1))],
                         [sg.InputCombo(('Annelinn', 'Tammelinn', 'Ihaste', 'Jaamamõisa', 'Karlova', 'Kesklinn', 'Maarjamõisa','Raadi','Ropka','Ränilinn','Supilinn','Tähtvere','Vaksali','Variku','Veeriku','Ülejõe' ), size=(10, 1))],
                         [sg.Text('Valikute kast: ')],
                         [sg.Listbox(values=('Valik 1', 'Valik 2', 'Valik 3', 'Valik 4', 'Valik 5', 'Valik 6', 'Valik 7'), size=(20, 5))],
                         [sg.Text('Mitu liitrit?: ', size=(20,1))],
                         [sg.Slider(range=(1, 10), orientation='h', size=(20, 20), default_value=5)],
                         [sg.Submit('Sisesta'), sg.Cancel('Välju')]
        
    #lisame ka juba tuttavad nupud
    [sg.Submit('Saada!'), sg.Cancel('Sulge')]]
aken = sg.Window('Palju erinevaid vidinaid!', paigutus, size=(600,700), default_element_size=(40, 1), grab_anywhere=False)

      
    if syndmus == sg.WIN_CLOSED or syndmus == 'Sulge':
        break
    if syndmus == 'Saada!':
        aken.close()
        sg.Popup('Kuvame siin Sinu sisestatud vastused: ',
                 #Vastused kuvatakse sõnastikuna looksulgude vahel
                 'Vajutatud nupp: "{}"'.format(syndmus),
                 'Vastused: ', v22rtused)
aken.close()