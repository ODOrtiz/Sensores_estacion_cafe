import time
# =========================================
# Configuracion de libreria
# =========================================
import sensorsStation
estacion = sensorsStation.SensorsStation()

while True:
	# Lectura de variables, todos los calculos se hacen de forma interna
	print("Radiacion: " + str(estacion.getRadiation()) + " W/m^2")
	print("Temperatura: " + str(estacion.getTemperature()) + " ºC")
	print("Humedad: " + str(estacion.getHumidity()) + " %")
	print("Direccion: " + str(estacion.getDirection()) + " º")
	print("Velocidad: " + str(estacion.getVelocity()) + " Km/h")
	print("Precipitacion del dia: " + str(estacion.getPrecipitation()) + " ml\n")
	time.sleep(5)
