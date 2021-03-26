import configparser
import speech_recognition as sr


class STT:
    def __init__(self, config_path):
        self.recognizer = sr.Recognizer()
        self.config_path = config_path
        self.__config()

    def __config(self):
        conf = configparser.ConfigParser()
        conf.read(self.config_path)

        self.language = conf['CONFIGURATION']['LANGUAGE']
        self.nr = conf['CONFIGURATION'].getboolean('NOISE_REDUCTION')
        self.buffer = int(conf['CONFIGURATION']['BUFFER_SIZE'])
        self.service = conf['CONFIGURATION']['SERVICE']

        self.GoogleDefaultAPI = conf['GOOGLE_SPEECH_RECOGNITION'].getboolean('USE_DEFAULT_API')
        self.GOOGLE_SPEECH_RECOGNITION_API_KEY = conf['GOOGLE_SPEECH_RECOGNITION']['GOOGLE_SPEECH_RECOGNITION_API_KEY']
        self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = conf['GOOGLE_CLOUD_SPEECH']['GOOGLE_CLOUD_SPEECH_CREDENTIALS']
        self.WIT_AI_KEY = conf['WIT_AI']['WIT_AI_KEY']
        self.AZURE_SPEECH_KEY = conf['AZURE_SPEECH']['AZURE_SPEECH_KEY']
        self.BING_KEY = conf['BING']['BING_KEY']
        self.HOUNDIFY_CLIENT_ID = conf['HOUNDIFY']['HOUNDIFY_CLIENT_ID']
        self.HOUNDIFY_CLIENT_KEY = conf['HOUNDIFY']['HOUNDIFY_CLIENT_KEY']
        self.IBM_USERNAME = conf['IBM']['IBM_USERNAME']
        self.IBM_PASSWORD = conf['IBM']['IBM_PASSWORD']

    def STT_model(self):
        if self.service == "SPHINX": ret = self.SPHINX()
        elif self.service == "GOOGLE_SPEECH_RECOGNITION": ret = self.GOOGLE_SPEECH_RECOGNITION()
        elif self.service == "GOOGLE_CLOUD_SPEECH": ret = self.GOOGLE_CLOUD_SPEECH()
        elif self.service == "WIT_AI": ret = self.WIT_AI()
        elif self.service == "AZURE_SPEECH": ret = self.AZURE_SPEECH()
        elif self.service == "BING": ret = self.BING()
        elif self.service == "HOUNDIFY": ret = self.HOUNDIFY()
        elif self.service == "IBM": ret = self.IBM()
        return ret

    def STT_message(self, audio_file):
        self.audio_file = audio_file
        with sr.AudioFile(self.audio_file) as source:
            if self.nr: self.recognizer.adjust_for_ambient_noise(source)
            self.audio = self.recognizer.record(source)
            try:
                ret = self.STT_model()
            except sr.UnknownValueError:
                ret = None
            except sr.RequestError as e:
                print(f"Could not request results from service; {e}")
                ret = None
            return ret

    def SPHINX(self):
        return self.recognizer.recognize_sphinx(self.audio, language=self.language)

    def GOOGLE_SPEECH_RECOGNITION(self):
        if self.GoogleDefaultAPI:
            ret = self.recognizer.recognize_google(self.audio, language=self.language)
        else:
            ret = self.recognizer.recognize_google(self.audio, language=self.language, key=self.GOOGLE_SPEECH_RECOGNITION_API_KEY)
        return ret

    def GOOGLE_CLOUD_SPEECH(self):
        return self.recognizer.recognize_google_cloud(self.audio, language=self.language, credentials_json=self.GOOGLE_CLOUD_SPEECH_CREDENTIALS)

    def WIT_AI(self):
        return self.recognizer.recognize_wit(self.audio, key=self.WIT_AI_KEY)

    def AZURE_SPEECH(self):
        return self.recognizer.recognize_azure(self.audio, language=self.language, key=self.AZURE_SPEECH_KEY)

    def BING(self):
        return self.recognizer.recognize_bing(self.audio, language=self.language, key=self.BING_KEY)

    def HOUNDIFY(self):
        return self.recognizer.recognize_houndify(self.audio, client_id=self.HOUNDIFY_CLIENT_ID, client_key=self.HOUNDIFY_CLIENT_KEY)

    def IBM(self):
        return self.recognizer.recognize_ibm(self.audio, language=self.language, username=self.IBM_USERNAME, password=self.IBM_PASSWORD)


if __name__ == '__main__':
    a = STT('config.txt')
    text = a.STT_message('example_files/test1.wav')
    print(text)