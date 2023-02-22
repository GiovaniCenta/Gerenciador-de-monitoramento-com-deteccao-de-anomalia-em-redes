import PySimpleGUI as sg
from easysnmp import Session

sg.theme('Material1')


class App:

    def __init__(self):
        self.window = self.create_screen()

    def create_screen(self):
        return sg.Window('Análise de Métricas', self.get_layout(), default_element_size=(40, 1), auto_size_text=False,
                         button_color='red', margins=(10, 10))

    def get_layout(self):
        return [
            [sg.Text('Utilização do processador = ', font=('Helvetica', 15), text_color='black',
                     background_color='light blue'),
             sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100),
                      background_color='light blue',
                      key='-PROCESSOR-')],
            [sg.Text('Uso da memória = ', font=('Helvetica', 15), text_color='black', background_color='light blue'),
             sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100),
                      background_color='light blue',
                      key='-MEMORY-')],
            [sg.Text('Contadores de erros de entrada = ', font=('Helvetica', 15), text_color='black',
                     background_color='light blue'),
             sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100),
                      background_color='light blue',
                      key='-INERRORS-')],
            [sg.Text('Contadores de erros de saída = ', font=('Helvetica', 15), text_color='black',
                     background_color='light blue'),
             sg.Graph(canvas_size=(250, 150), graph_bottom_left=(0, 0), graph_top_right=(100, 100),
                      background_color='light blue',
                      key='-OUTERRORS-')],
            [sg.Button('Atualizar', font=('Helvetica', 12)), sg.Exit(font=('Helvetica', 12))]]

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Atualizar':
                self.update()

    def update(self):
        session = Session(hostname='10.0.0.1', community='public', version=2)
        hrProcessorLoad = session.get('HOST-RESOURCES-MIB::hrProcessorLoad.1').value
        self.window['-PROCESSOR-'].update(hrProcessorLoad)
        memTotalReal = session.get('UCD-SNMP-MIB::memTotalReal.0').value
        memAvailReal = session.get('UCD-SNMP-MIB::memAvailReal.0').value
        memory = (int(memTotalReal) - int(memAvailReal)) / int(memTotalReal) * 100
        self.window['-MEMORY-'].update(memory)
        ifInErrors = session.get('IF-MIB::ifInErrors.2').value
        self.window['-INERRORS-'].update(ifInErrors)
        ifOutErrors = session.get('IF-MIB::ifOutErrors.2').value
        self.window['-OUTERRORS-'].update(ifOutErrors)

    def close(self):
        self.window.close()
