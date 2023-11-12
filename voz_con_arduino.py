import speech_recognition as sr
from pyfirmata import Arduino, util
import pyttsx3

def encender_led():
    led_pin.write(1)

def apagar_led():
    led_pin.write(0)

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

board = Arduino('COM6')
led_pin = board.get_pin('d:13:o')

recognizer = sr.Recognizer()

def escuchar_comandos():
    with sr.Microphone() as source:
        print("Di 'Alexa, enciende el LED' o 'Alexa, apaga el LED'")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="es-ES").lower()
        print("Comando: " + command)
        return command
    except sr.UnknownValueError:
        print("No se pudo entender el comando")
        return ""
    except sr.RequestError as e:
        print("Error al realizar la solicitud al servicio de reconocimiento de voz; {0}".format(e))
        return ""

while True:
    command = escuchar_comandos()

    if "enciende el led" in command:
        encender_led()
        hablar("LED encendido")
    elif "apaga el led" in command:
        apagar_led()
        hablar("LED apagado")
    elif "salir" in command:
        hablar("Saliendo del programa")
        break