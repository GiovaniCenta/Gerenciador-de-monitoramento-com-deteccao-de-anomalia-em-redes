import PySimpleGUI as sg
from easysnmp import Session


def main():
    print("BEGIN")
    sg.theme('Material1')

    layout = [
    [sg.Text('Utilização do processador = ', font=('Helvetica', 15), text_color='black', background_color='light blue'),
     sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100), background_color='light blue',
              key='-PROCESSOR-')],
    [sg.Text('Uso da memória = ', font=('Helvetica', 15), text_color='black', background_color='light blue'),
     sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100), background_color='light blue',
              key='-MEMORY-')],
    [sg.Text('Contadores de erros de entrada = ', font=('Helvetica', 15), text_color='black', background_color='light blue'),
     sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100), background_color='light blue',
              key='-INERRORS-')],
    [sg.Text('Contadores de erros de saída = ', font=('Helvetica', 15), text_color='black', background_color='light blue'),
     sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100), background_color='light blue',
              key='-OUTERRORS-')],
    [sg.Button('Atualizar', font=('Helvetica', 12)), sg.Exit(font=('Helvetica', 12))]
]

    window = sg.Window('Análise de Métricas', layout, default_element_size=(40, 1), auto_size_text=False,button_color = 'red',margins = (10,10))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Atualizar':
            session = Session(hostname='10.0.0.1', community='public', version=2)
            hrProcessorLoad = session.get('HOST-RESOURCES-MIB::hrProcessorLoad.1').value
            window['-PROCESSOR-'].update(hrProcessorLoad)
            memTotalReal = session.get('UCD-SNMP-MIB::memTotalReal.0').value
            memAvailReal = session.get('UCD-SNMP-MIB::memAvailReal.0').value
            memory = (int(memTotalReal) - int(memAvailReal)) / int(memTotalReal) * 100
            window['-MEMORY-'].update(memory)
            ifInErrors = session.get('IF-MIB::ifInErrors.2').value
            window['-INERRORS-'].update(ifInErrors)
            ifOutErrors = session.get('IF-MIB::ifOutErrors.2').value
            window['-OUTERRORS-'].update(ifOutErrors)

    window.close()
    print("END")


if __name__ == "__main__":
    main()


