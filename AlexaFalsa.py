import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit


audio = sr.Recognizer()
maquina = pyttsx3.init()

maquina.say('Olá, eu me chamo Caio') # abertura
maquina.say('No que posso ajudar?') #inicio
maquina.runAndWait()


def executa_comando():
 try:
     with sr.Microphone() as source:
        print('Ouvindo..')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR') #linguagem da fala
        comando = comando.lower()
        
        if 'caio' in comando: 
            comando = comando.replace('caio', '') 
            maquina.say(comando)
            maquina.runAndWait()
    
 except:
    print('Não foi possivel entender seu comando')
    
    return comando

def comando_voz_usuario():
    comando = executa_comando() 
    
    if 'horas' in comando: #informa a hora
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say ('Agora são' + hora)
        maquina.runAndWait()
    
    elif 'procure por' in comando: #procura no wikipedia
        procurar = comando.replace('procurar por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        maquina.say(resultado)
        maquina.runAndWait()
        
    elif 'toque' in comando: #reproduz musica no youtube
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()
               
        
comando_voz_usuario()