#de gpiozero importa LED
from gpiozero import LED
# De la biblioteca time import sleep que esta definida por segundo
from time import sleep
led_rojo=LED(14)
led_azul=LED(15)
led_verde=LED(18)
 
#declaramos para hacer que el rojo se prenda y apague cada segundo 
while(True):
 led_rojo.on()
 led_azul.on()
 led_verde.off()
 sleep(1)
 led_rojo.on()
 led_azul.off()
 led_verde.on()
 sleep(1)
 led_rojo.off()
 led_azul.on()
 led_verde.on()
 sleep(1)



  
 
