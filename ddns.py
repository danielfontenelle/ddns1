# -*- coding: utf8 -*- 
import subprocess 


########################## NECESSÁRIO EXECUTAR O CMD COMO ADMINISTRADOR! ##########################################

return_code = subprocess.call('color c',shell=True)
print('###################################################################################################')
dns = int(input('Escolha algum servidor de DNS: [1]-Dyn [2]-Google [3]-UltraDNS [4]-OpenDNS [5]-Comodo [6]-Safe DNS: '))
print('###################################################################################################')
print('Criado por: Daniel Fontenelle  | Facebook: https://www.facebook.com/danielll.fontenelle')
print('###################################################################################################')
print('###################################################################################################')



########################## AQUI FAZ AS TROCAS DO SERVIDOR DE DNS ##################################################

if dns == 1:
	return_code = subprocess.call('netsh int ip add dns "Ethernet" addr=216.146.35.35 index=1',shell=True)
	print('ATENÇÃO: O Prompt de Comando (CMD) deve ser executado como Administrador! ')
if dns == 2:
	return_code = subprocess.call('netsh int ip add dns "Ethernet" addr=8.8.8.8 index=1',shell=True)
	print('ATENÇÃO: O Prompt de Comando (CMD) deve ser executado como Administrador! ')
if dns == 3:
	return_code = subprocess.call('netsh int ip add dns "Ethernet" addr=204.69.234.1 index=1',shell=True)
	print('ATENÇÃO: O Prompt de Comando (CMD) deve ser executado como Administrador! ')
if dns == 4:
	return_code = subprocess.call('netsh int ip add dns "Ethernet" addr=208.67.220.220 index=1',shell=True)
	print('ATENÇÃO: O Prompt de Comando (CMD) deve ser executado como Administrador! ')
if dns == 5:
	return_code = subprocess.call('netsh int ip add dns "Ethernet" addr=156.154.70.22 index=1',shell=True)
	print('ATENÇÃO: O Prompt de Comando (CMD) deve ser executado como Administrador! ')
if dns == 6:
	return_code = subprocess.call('netsh int ip add dns "Ethernet" addr=195.46.39.39 index=1',shell=True)
	print('ATENÇÃO: O Prompt de Comando (CMD) deve ser executado como Administrador! ')
	
########################## Esse foi o meu segundo programinha criado em Python ^^ ######################################


		



