from gpiozero import LED 
from time import sleep
from gpiozero import Button 
led_rojo= LED(14)
led_azul= LED(15)
led_verde= LED(18)
button_1 = Button(17)
button_2 = Button(27) 
button_3 = Button(22)
while True:
    
 if button_1.is_pressed or button_2.is_pressed:

  led_rojo.on()
  led_verde.on()
  led_azul.on() 

 else: 
    led_rojo.off()
    led_verde.on()
    led_azul.off() 
    sleep(.5)
    
 if button_1.is_pressed or button_3.is_pressed:

  led_rojo.on()
  led_verde.on()
  led_azul.on() 
 else:
    led_rojo.off()
    led_verde.off()
    led_azul.on() 
    sleep(.5)
 
 if button_2.is_pressed or button_3.is_pressed:
     led_rojo.on()
     led_verde.on()
     led_azul.on() 
 else:
    led_rojo.off()
    led_verde.off()
    led_azul.off() 
    sleep(.5)

    
 
