Import jogovelha
import sys

erroInicializar = false
jogo = jogovelha.inicializar()

if len(jogo) != 3:
	erroInicializar= True
else:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemneto != '.':
					erroInicializar = True
if erroInicializar:
	sys.exit(1)
else:
	sys.exit(0)
