import keyboard
import speech_recognition as sr
import pyautogui as pg
import time
import datetime
from gtts import gTTS
from gtts import gTTS
import sounddevice as sd
import soundfile as sf


#modficável
tasks = ''
data_hora_atual = datetime.datetime.now()
hora_atual = datetime.datetime.now().strftime("%H")
email = 'pedrohenriquedeaquinogodoydeso@gmail.com'
#não modficável
def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source: #AS VEZES PEGA O AUDIO DO EASE US
        print("Diga o comando (ex: 'clicar' , 'parar' ou 'pausa')...")
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print("Você disse:", comando)
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Erro no serviço de reconhecimento.")
    return ""

#
def task():
    b = gTTS(tasks, lang='pt')
    b.save('voz.mp3')
    filename = 'voz.mp3'
    data, fs = sf.read(filename, dtype='int16')
    sd.play(data, fs)


print("Esperando comando de voz...")

def falar(x):
    b = gTTS(x, lang='pt')
    b.save('voz.mp3')
    filename = 'voz.mp3'
    data, fs = sf.read(filename, dtype='int16')
    sd.play(data, fs)
    
def escreva():
    keyboard.write(ouvir_comando())

def abrir():
    keyboard.press_and_release('win')
    keyboard.write(ouvir_comando())
    for i in range(3):
        time.sleep(1)
        keyboard.press_and_release('enter')
    
def exibir_lista_comandos():

    print('----C O M A N D O S----\n'
    'Clica-(clicar,clica,pausa,despausa) ;\n'
    'Autoclick[pausa com h]-(auto,automático)\n'  
    'Abre o que disser-(abrir[algo no pc]) ;\n' 
    'Escreva-(fale escreva, depois o que deseja escrever)\n' 
    'Missões(fala seus objetivos)\n'
    'Fim do código-(sair, parar)\n'
    '----- M E M E------\n'
    'destruição (simula uma autodestruição)\n')
def click():
    pg.click()
def farm_automatica():
    pg.click()

def rap():
    #https://www.youtube.com/watch?v=Hn6D3K8rWfI&list=RDQQLIn91wE3o&index=2 - KUNIGAMI
    #https://youtube.com/playlist?list=PLSDHHB0zAFUZBxCSpmvqsb2219zDVp57P&si=6WVWqAWOLfokCcdu - Tuilist
    keyboard.press_and_release('win')
    keyboard.write('Opera GX')
    for i in range(3):
        time.sleep(1)
        keyboard.press_and_release('enter')
    keyboard.write('https://www.youtube.com/watch?v=Hn6D3K8rWfI&list=RDQQLIn91wE3o&index=2')
    keyboard.press_and_release('enter')

def volume():

    t = ouvir_comando()
    if "diminuir" in t or "abaixar" in t:
        for i in range(5):
            keyboard.press_and_release('volume down')
    elif "aumentar" in t or "subir" in t:
        for i in range(5):
            keyboard.press_and_release('volume up')
    elif "mutar" in t or "mudo" in t:
        keyboard.press_and_release('volume mute')


def pesquisar():
    keyboard.press_and_release('win')
    time.sleep(0.2)
    keyboard.write('Opera GX')
    for i in range(3):
        time.sleep(1)
        keyboard.press_and_release('enter')
    keyboard.write(ouvir_comando())
    keyboard.press_and_release('enter')
#colocar mais funções (Opcional)
# HORÁRIO E FALA OS TEMAS
#palavras-chave que iniciam as funções
while True:
    comando = ouvir_comando()

    if "clicar" in comando or "clica" in comando or "pausa" in comando or "despausa" in comando:
        click()
    elif "volume" in comando:
        volume()
    elif "comandos" in comando or "comando" in comando:
        exibir_lista_comandos()
    elif "automático" in comando or "auto" in comando or keyboard.is_pressed('g'):
        while not keyboard.is_pressed('h') :
            farm_automatica()
    elif "abrir" in comando or "Abrir" in comando:
        abrir()
    elif 'destruição' in comando:
        falar('Iniciando auto destruição, 3, 2 , 1, trollei')
    elif "escreva" in comando:
        escreva() 
    elif 'missões' in comando or 'missão' in comando:
        task()
    elif 'Rap' in comando or 'rap' in comando:
        rap()
    elif "parar" in comando or "sair" in comando:
        print("Encerrando script.")
        break
    elif "pesquisar" in comando:
        pesquisar()
    
    #ADICIONAR Matemática, Probabilidade e Estatística, modo narrador (windows + ctrl + enter)
