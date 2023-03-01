import PySimpleGUI as sg
from easysnmp import Session
import random
from time import time

sg.theme('Reddit')


class App:

    def __init__(self):
        self.window = self.create_screen()

    def create_screen(self):
        window = sg.Window('Análise de Métricas', self.get_layout(), default_element_size=(40, 1), auto_size_text=False,
                         button_color='purple', margins=(10, 10))
        #window = sg.Window("My Window", self.get_layout(), background_image="background.jfif")

        return window

    def get_layout(self):
        return [
            [sg.Text('Tempo de atividade = ', font=('Helvetica', 15), text_color='black'),
             sg.Text(size=(40,1), key='-UPTIME-')],
            [sg.Text('Utilização do processador = ', font=('Helvetica', 15), text_color='black'),
             sg.Text(size=(40,1), key='-PROCESSOR-')],
            [sg.Text('Uso da memória = ', font=('Helvetica', 15), text_color='black'),
             sg.Text(size=(40,1), key='-MEMORY-')],
            [sg.Text('Contadores de erros de entrada = ', font=('Helvetica', 15), text_color='black'),
             sg.Text(size=(40,1), key='-INERRORS-')],
            [sg.Text('Contadores de erros de saída = ', font=('Helvetica', 15), text_color='black'),
             sg.Text(size=(40,1), key='-OUTERRORS-')],
            [sg.Text('Utilização da largura de banda = ', font=('Helvetica', 15), text_color='black'),
             sg.Text(size=(40,1), key='-BANDWIDTH-')],
            [sg.Text('Taxa de transferência de rede = ', font=('Helvetica', 15), text_color='black'),
             sg.Text(size=(40,1), key='-TRAFFIC-')],
            [sg.Button('Atualizar', font=('Helvetica', 12)), sg.Exit(font=('Helvetica', 12))]]

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Atualizar':
                self.update()
            self.update()

    def update(self):
       
        session = Session(hostname='10.0.0.1', community='public', version=2)

        uptime = session.get('sysUpTime.0')
        uptime_ticks = uptime.value
        uptime_secs = int(uptime_ticks) // 100
        #uptime = random.random()
        self.window['-UPTIME-'].update(uptime_secs)
        
        hrProcessorLoad = session.get('HOST-RESOURCES-MIB::hrProcessorLoad.1').value
        #hrProcessorLoad = random.random()
        self.window['-PROCESSOR-'].update(hrProcessorLoad)
        
        memTotalReal = session.get('UCD-SNMP-MIB::memTotalReal.0').value
        memAvailReal = session.get('UCD-SNMP-MIB::memAvailReal.0').value
        memory = (int(memTotalReal) - int(memAvailReal)) / int(memTotalReal) * 100
        #memory = random.random()
        
        #self.window['-MEMORY-'].update(memory)
        ifInErrors = session.get('IF-MIB::ifInErrors.2').value
        ifInErrors = random.random()
        self.window['-INERRORS-'].update(ifInErrors)
        #ifOutErrors = session.get('IF-MIB::ifOutErrors.2').value
        ifOutErrors = random.random()
        self.window['-OUTERRORS-'].update(ifOutErrors)
        
        utilizacao_bps= self.utilizacao_largura_banda_e(session,intervalo = 2)
        #utilizacao_bps = random.random() 
        self.window['-BANDWIDTH-'].update(utilizacao_bps)
        
        trafego = self.transfer_rate(session,intervalo = 2)
        #trafego = random.random() 
        self.window['-TRAFFIC-'].update(trafego)
        
        self.verifica_erros(variavel = 'INERRORS',valor = ifInErrors ,limite = 1)
        self.verifica_erros(variavel = 'OUTERRORS',valor = ifOutErrors ,limite = 1)
        self.verifica_erros(variavel = 'Utilização da bandwidth',valor = utilizacao_bps ,limite = 95)
        self.verifica_erros(variavel = 'memoria',valor = memory ,limite = 95)
        
        

    def close(self):
        self.window.close()
        
    def utilizacao_largura_banda(self,session,intervalo = 5):
        interface_index = 1
        in_octets = int(session.get(f'IF-MIB::ifInOctets.{interface_index}').value)
        out_octets = int(session.get(f'IF-MIB::ifOutOctets.{interface_index}').value)
        if_speed = int(session.get(f'IF-MIB::ifSpeed.{interface_index}').value)

        # Aguardar por um intervalo de tempo
        import time
        time.sleep(intervalo)

        # Obter os novos valores de entrada e saída do contador de largura de banda
        in_octets_new = int(session.get(f'IF-MIB::ifInOctets.{interface_index}').value)
        out_octets_new = int(session.get(f'IF-MIB::ifOutOctets.{interface_index}').value)

        # Calcular a diferença entre os valores de entrada e saída em dois intervalos de tempo diferentes
        delta_in_octets = in_octets_new - in_octets
        delta_out_octets = out_octets_new - out_octets

        # Calcular a utilização da largura de banda em bits por segundo (bps)
        intervalo_de_tempo = 5  # segundos
        taxa_de_transferencia_bps = (delta_in_octets + delta_out_octets) * 8 / intervalo_de_tempo
        
        utilizacao_da_largura_de_banda = taxa_de_transferencia_bps / if_speed * 100

        return utilizacao_da_largura_de_banda
    def transfer_rate(self,session,intervalo):
        initial_time = time.time()

        interface_oid = 'IF-MIB::ifInOctets.1'
        traffic_start = session.get(interface_oid).value

        time.sleep(intervalo)

       
        traffic_end = session.get(interface_oid).value

        
        traffic = traffic_end - traffic_start

        
        transfer_rate = traffic / (time.time() - initial_time)
        return transfer_rate
    
    def verifica_erros(self,variavel,valor,limite):
        
        if valor > limite:
            message = "A variável " + variavel + " está acima do limite de " + str(limite) + " % \n\n ==== Acabar com a conexão? ==== "
            button = sg.popup(message, button_type=sg.POPUP_BUTTONS_YES_NO)

            if button == "Yes":
                self.window.close()
                exit(8)
            else:
                pass
