import PySimpleGUI as sg
#from easysnmp import Session
import random
from time import time

sg.theme('DarkTeal')


class App:

    def __init__(self):
        self.window = self.create_screen()
 
    def create_screen(self):
        window = sg.Window('Análise de Métricas', self.get_layout(), default_element_size=(40, 1), auto_size_text=True,
                         button_color='purple', margins=(10, 10))
        #window = sg.Window("My Window", self.get_layout(), background_image="background.jfif")

        return window

    def get_layout(self):
        return [
           
            [sg.Text('Tempo de atividade (s) = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-UPTIME-')],
            [sg.Text('Utilização do processador em % = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-PROCESSOR-')],
            
            #Numero de interfaces
            [sg.Text('Número de interfaces = ', font=('Helvetica', 15), text_color='white'),
                sg.Text(size=(40,1), key='-INTERFACES-')],
            
            
            #Memoria
            [sg.Text('Total de memória (Mb)= ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-MEMORYTOTAL-')],
            [sg.Text('Uso de memória(Mb) = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-MEMORYUSE-')],
            [sg.Text('Memoria livre(Mb) = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-MEMORYFREE-')],
            [sg.Text('Memoria livre em % =  ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-MEMORYFREEPERCENT-')],
            
            #Disco
            [sg.Text('Espaço em disco total (Mb ) = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-DISKTOTAL-')],
            [sg.Text('Espaço em disco em uso(Mb) = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-DISKUSE-')],
            [sg.Text('Espaço em disco livre (Mb)=  ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-DISKFREE-')],
            [sg.Text('Espaço em disco livre em %= ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-DISKFREEPERCENT-')],
            
            #Erros de entrada e saida
            [sg.Text('Contadores de erros de entrada = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-INERRORS-')],
            [sg.Text('Contadores de erros de saída = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-OUTERRORS-')],
            
            #Temperatura
            [sg.Text('Temperatura (Celsius) = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-TEMPERATURE-')],

            #Pacotes enviados e recebidos
            [sg.Text('Pacotes enviados = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-PACKETSSENT-')],
            [sg.Text('Pacotes recebidos = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-PACKETSRECEIVED-')],
            
            
            
            #TCP    
            [sg.Text('Contador de conexões TCP = ', font=('Helvetica', 15), text_color='white'),    
             sg.Text(size=(40,1), key='-TCP-')],
            
            #Informacoes de trafego entrada,saida e total
            [sg.Text('Tráfego de entrada = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-INTRAFFIC-')],
            [sg.Text('Tráfego de saída = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-OUTTRAFFIC-')],
            [sg.Text('Tráfego total = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-TOTALTRAFFIC-')],
            
            
            
            [sg.Text('Utilização da largura de banda = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-BANDWIDTH-')],
            [sg.Text('Taxa de transferência de rede = ', font=('Helvetica', 15), text_color='white'),
             sg.Text(size=(40,1), key='-TRAFFIC-')],
            ]

    def run(self):
        endereco_ip = 0
        ip = sg.popup_get_text('Digite o endereço IP do agente')
        while True:
            event, values = self.window.read(timeout=0)
            endereco_ip = ip
            print(f'Endereço IP digitado: {endereco_ip}')
            self.update(endereco_ip)
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            
            
                
                #while event not in (sg.WIN_CLOSED, 'Exit'):
                #    self.update(endereco_ip)
            
            #self.update(endereco_ip)

    def update(self,endereco_ip):
        
        """        session = Session(hostname=endereco_ip, community='public', version=2)

                uptime = session.get('sysUpTime.0')
                uptime_ticks = uptime.value
                uptime_secs = int(uptime_ticks) // 100"""
        
        uptime_secs = random.random()
        self.window['-UPTIME-'].update(uptime_secs)
        
        #cpu_usage = int(session.get('ssCpuRawIdle.0').value)
        #cpu_usage_percent = 100 - cpu_usage
        cpu_usage_percent = random.random()
        self.window['-PROCESSOR-'].update(cpu_usage_percent)
        
        #numero de interfaces
        oid = '1.3.6.1.2.1.2.1.0'
        #value = int(session.get(oid).value)
        value = random.random()
        self.window['-INTERFACES-'].update(value)
        
        
        #total_memory,used_memory,used_memory_percent,free_memory = self.memory(session)
        
        #####MEMORIA
        #total_memory,used_memory,used_memory_percent,free_memory = self.memory(session)
        total_memory,used_memory,used_memory_percent,free_memory = [random.random(),random.random(),random.random(),random.random()]
        self.window['-MEMORYTOTAL-'].update(total_memory)
        self.window['-MEMORYUSE-'].update(used_memory)
        self.window['-MEMORYFREE-'].update(free_memory)
        self.window['-MEMORYFREEPERCENT-'].update(used_memory_percent)
        
        
        #disk_space_total,disk_space_used,disk_space_used_percent,disk_space_free = self.disk_space(session)
        disk_space_total,disk_space_used,disk_space_used_percent,disk_space_free = [random.random(),random.random(),random.random(),random.random()]

        self.window['-DISKTOTAL-'].update(disk_space_total)
        self.window['-DISKUSE-'].update(disk_space_used)
        self.window['-DISKFREE-'].update(disk_space_free)
        self.window['-DISKFREEPERCENT-'].update(disk_space_used_percent)
        
        ####Erros de entrada e saida
        #ifInErrors = session.get('IF-MIB::ifInErrors.2').value
        ifInErrors = random.random()
        self.window['-INERRORS-'].update(ifInErrors)
        #ifOutErrors = session.get('IF-MIB::ifOutErrors.2').value
        ifOutErrors = random.random()
        self.window['-OUTERRORS-'].update(ifOutErrors)
        
        ####Temperatura
        #temperature = self.temperature(session)
        temperature = random.random()
        self.window['-TEMPERATURE-'].update(temperature)
        
        # Pacotes enviados e recebidos
        # packets_sent,packets_received = self.packets(session)
        packets_sent,packets_received = [random.random(),random.random()]
        self.window['-PACKETSSENT-'].update(packets_sent)
        self.window['-PACKETSRECEIVED-'].update(packets_received)
        
        # Contador de conexões TCP
        active_tcp_oid = 'tcpCurrEstab.0'
        #active_tcp_connections = int(session.get(active_tcp_oid).value)
        active_tcp_connections = random.random()
        self.window['-TCP-'].update(active_tcp_connections)
        
        # Informações de trafego
        #input_traffic, output_traffic,total_traffic = self.trafego(session)
        input_traffic, output_traffic,total_traffic = [random.random(),random.random(),random.random()]
        self.window['-INTRAFFIC-'].update(input_traffic)
        self.window['-OUTTRAFFIC-'].update(output_traffic)
        self.window['-TOTALTRAFFIC-'].update(total_traffic)
        
        
        
        
        #utilizacao_bps= self.utilizacao_largura_banda_e(session,intervalo = 2)
        utilizacao_bps = random.random() 
        self.window['-BANDWIDTH-'].update(utilizacao_bps)
        
        #trafego = self.transfer_rate(session,intervalo = 2)
        trafego = random.random() 
        self.window['-TRAFFIC-'].update(trafego)
        
        self.verifica_erros(variavel = 'INERRORS',valor = ifInErrors ,limite = 1)
        self.verifica_erros(variavel = 'OUTERRORS',valor = ifOutErrors ,limite = 1)
        self.verifica_erros(variavel = 'Utilização da bandwidth',valor = utilizacao_bps ,limite = 95)
        self.verifica_erros(variavel = 'Uso de memoria',valor = used_memory_percent ,limite = 95)
        
        

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
    
    def memory(self, session):
        total_memory_oid = 'memTotalReal.0'
        used_memory_oid = 'memAvailReal.0'

        total_memory = int(session.get(total_memory_oid).value)
        used_memory = int(session.get(used_memory_oid).value)
        free_memory = total_memory - used_memory
        used_memory_percent = (used_memory / total_memory) * 100

        print(f'Total memory: {total_memory} bytes')
        print(f'Used memory: {used_memory} bytes ({used_memory_percent}%)')
        print(f'Free memory: {free_memory} bytes')
        
        return total_memory,used_memory,used_memory_percent,free_memory
    
    def disk_space(self,session):
        disk_space_oid = 'hrStorageUsed.31'
        disk_space_used = int(session.get(disk_space_oid).value)

        if disk_space_used > 0:
            disk_space_total_oid = 'hrStorageSize.31'
            disk_space_total = int(session.get(disk_space_total_oid).value)
            disk_space_free = disk_space_total - disk_space_used
            disk_space_used_percent = (disk_space_used / disk_space_total) * 100
            print(f'Total disk space: {disk_space_total} bytes')
            print(f'Used disk space: {disk_space_used} bytes ({disk_space_used_percent:.2f}%)')
            print(f'Free disk space: {disk_space_free} bytes')
            return disk_space_total,disk_space_used,disk_space_used_percent,disk_space_free
        else:
            sg.popup("Não foi possível obter o espaço em disco")
    def transfer_rate(self,session,intervalo):
        import time
        initial_time = time.time()

        interface_oid = 'IF-MIB::ifInOctets.1'
        traffic_start = session.get(interface_oid).value

        time.sleep(intervalo)

       
        traffic_end = session.get(interface_oid).value

        
        traffic = float(traffic_end) - float(traffic_start)

        
        transfer_rate = traffic / (time.time() - initial_time)
        return transfer_rate
    
    
    def temperature(self,session):
        temperature_oid = 'tempSensorValue.1'
        temperature_value = int(session.get(temperature_oid).value)

        if temperature_value > 0:
            temperature_celsius = temperature_value / 10
            return temperature_celsius
        else:
            sg.popup("Não foi possível obter a temperatura")
            
            
    def packets(self,session):
        packets_sent_oid = 'ifOutUcastPkts.1'
        packets_sent = int(session.get(packets_sent_oid).value)

        packets_received_oid = 'ifInUcastPkts.1'
        packets_received = int(session.get(packets_received_oid).value)

        return packets_sent,packets_received
    
    
    def trafego(self,session):
        input_traffic_oid = 'ifInOctets.1'
        output_traffic_oid = 'ifOutOctets.1'

        input_traffic = int(session.get(input_traffic_oid).value)
        output_traffic = int(session.get(output_traffic_oid).value)
        total_traffic = input_traffic + output_traffic

        return input_traffic,output_traffic,total_traffic
            
    def verifica_erros(self,variavel,valor,limite):
        
        if valor > limite:
            message = "A variável " + variavel + " está acima do limite de " + str(limite) + " % \n\n ==== Acabar com a conexão? ==== "
            button = sg.popup(message, button_type=sg.POPUP_BUTTONS_YES_NO)

            if button == "Yes":
                self.window.close()
                exit(8)
            else:
                pass
