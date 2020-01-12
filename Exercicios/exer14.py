# °C * 1.8 + 32 = °F
celsius = float(input('Informe a temperatura em °C: '))

fahrenheit = (celsius * 1.8) + 32 # ((9*c) / 5) + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(celsius, fahrenheit))
