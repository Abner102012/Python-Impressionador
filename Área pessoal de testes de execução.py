import time
import locale

locale.setlocale(locale.LC_TIME, "pt-BR")

data_atual = time.localtime()

data_texto  = time.strftime("%A, %d de %B de %Y, %H:%M", data_atual)

print(data_texto.title())