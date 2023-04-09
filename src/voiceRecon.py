from gtts import gTTS
import speech_recognition as speech
import pyttsx3

class ReconnaissanceVocale:
    """
    Cette classe permet de faire de la reconnaissance vocale en français et de répondre en utilisant une voix française.

    Attributes:
        rate (int): La vitesse de la voix.
        volume (float): Le volume de la voix.
        voice_id (str): L'ID de la voix française à utiliser.

    Methods:
        __init__(self): Le constructeur de la classe.
        reconnaissance_vocale(self): La méthode pour effectuer la reconnaissance vocale et produire une réponse.
    """

    def __init__(self, rate=150, volume=0.9, voice_id=None):
        """
        Constructeur de la classe ReconnaissanceVocale.

        Args:
            rate (int): La vitesse de la voix. Default: 150.
            volume (float): Le volume de la voix. Default: 0.9.
            voice_id (str): L'ID de la voix française à utiliser. Si None, la première voix française trouvée sera utilisée. Default: None.
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        voices = self.engine.getProperty('voices')

        if voice_id is None:
            for voice in voices:
                if 'french' in voice.name.lower():
                    voice_id = voice.id
                    break

        self.engine.setProperty('voice', voice_id)
        self.recognize = speech.Recognizer()


    def reconnaissance_vocale(self):
        """
        Effectue la reconnaissance vocale et répond en utilisant la voix configurée.

        Returns:
            str: La réponse à produire en fonction de la reconnaissance vocale effectuée.
        """
        with speech.Microphone() as source:
            print("Parlez maintenant:")
            self.recognize.adjust_for_ambient_noise(source, duration=0.2)
            audio_text = self.recognize.listen(source)
            print("Enregistrement terminé, merci.")

        try:
            texte_audio = self.recognize.recognize_google(audio_text, language='fr-FR')
            print("Texte: " + texte_audio)
        except:
            print("Désolé, je n'ai pas compris.")
            self.engine.say("Désolé, je n'ai pas compris ce que vous essayez de dire")
            self.engine.runAndWait()

        verify = ""
        result = ""
        sorry = "Désolé, vous n'avez pas dit 'Jacques a dit'."

        result = str(texte_audio)

        # if "jacques a dit" in verify:
        #     eliminer = verify.find("jacques a dit") + len("Jacques a dit") + 1
        #     result = verify[eliminer:]
        # else:
        #     result = sorry

        print(result)
        # self.engine.say(result)
        # self.engine.runAndWait()
        return result
