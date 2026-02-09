from deep_translator import GoogleTranslator # type: ignore
from random import choice
from langdetect import detect, LangDetectException #type: ignore
#05/08/25


class MYTranslator:
    """
    DESCRIPTION:
        This is just a simple class that translate a text into another one

    RETURN: 
        An MYTranslator objet
    
    """
    Avaliable_languages:dict[str,str]={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar',
    'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az',
    'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn',
    'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
    'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN',
    'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr',
    'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl',
    'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl',
    'finnish': 'fi', 'french': 'fr', 'frisian': 'fyhaitian', 'creole': 'ht', 'hausa': 'ha',
    'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
    'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga',
    'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk',
    'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri',
    'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo',
    'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg',
    'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg',
    'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr',
    'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my',
    'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps',
    'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu',
    'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 
    'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 
    'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
    'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
    'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts',
    'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur',
    'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
    'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
    

    @staticmethod
    def translate_text(
                       text_:str,
                    language_:str='english')->str:
        """
        DESCRIPTION:
            This method only translate the given text into the desired language, wit the 
            help of the google tranlator module for python,
            it will be english as a defualt
        RETURN: 
            The tranlate text

        EXAMPLE:
            >>> translate_text("Hello world!","spanish")
            return Hola mundo 
        """
        return GoogleTranslator(source='auto',target=language_).translate(text=text_)
    

    @staticmethod
    def detect_language(text_:str)->str:
        """
        DESCRIPTION:
            This method only translate will give us in wich language is the currecntly 
            text

        RETURN: 
            The language of the text

        EXAMPLE:
            >>> detect_language("Hello world!")
            return  en
        """
        try:
            return detect(text_)
        except LangDetectException:
            return 'en'

    def get_translation(self,
                        text_to_translate: str, 
                        listener_languages: list[str])->str:
        """
        DESCRIPTION:
            This method translates a given text into one of the listener's known languages.
            It first checks if the text is already in a language the listener can speak.
            If not, it translates the text into a random language from the listener's list.

        RETURN: 
            The translated text, or the original text if no translation is needed.

        EXAMPLE:
            >>> get_translation("Hola mundo", ['english', 'german'])
            output: "Hello world"
        """
      
        detecting_currently_language: str =self.detect_language(text_to_translate)
        known_languagues:list[str|None]=[self.Avaliable_languages.get(lan) for lan in listener_languages]
        
        if detecting_currently_language in known_languagues:
            return text_to_translate



        target=choice(listener_languages)
        translate_=self.translate_text(text_to_translate,language_=target)
        return translate_


if __name__ == '__main__':
    hersy: list[str] = ['spanish', 'english']
    craice: list[str] = ['japanese', 'german', 'french','english']

    text_from_hersy: str = "Dude, you not gonna belive this. Today I was visit my granny y'know, like always, and then..."
    text_from_craice: str = "Was geht ab? Hast du Lust, Videospiele zu spielen?" 

    translator = MYTranslator()

    # 1. Hersy speaks to Craice
    translated_to_craice = translator.get_translation(text_from_hersy, craice)
    print(f"Hersy said: {text_from_hersy}")
    if translated_to_craice == text_from_hersy:
        print("Craice said: Ok")
    else:
        print("\nBut Craice couldn't undertand it, that's why she used a tranlator...")
        print(f"\nTranslation for Craice: {translated_to_craice}")
        print(f"Craice said: ... ")
    print("-" * 30)

    # 2. Craice speaks to Hersy
    translated_to_hersy = translator.get_translation(text_from_craice, hersy)
    print(f"Craice said: {text_from_craice}")
    if translated_to_hersy == text_from_craice:
        print("Hersy said: Ok")
    else:
        print("\nBut Hersy couldn't undertand it, that's why he used a tranlator...")
        print(f"\nTranslation for Hersy: {translated_to_hersy}")
        print(f"Hersy said: ... ")
    print("-" * 30)

    print(translator.get_translation(text_from_craice,['english']))
    print(translator.get_translation('how can you do that?',['english']))



    """
    print()
    print(translator.detect_language(text))
    print(translator.detect_language("こんにちは世界！"))
    print(translator.detect_language("Bonjour Craice, Whatcha fait, pour moi j'ai joué aux jeux vidéo le week-end"))


    """
    #print(translate_text("Hello hersy what's up","spanish"))

