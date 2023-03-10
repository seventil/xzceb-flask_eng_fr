''' The module translator provides functionality
to translate from english to french 
and from french to english
using IGM Watson API
'''


import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    ''' Function translates english text to french
    '''
    if englishText is None:
        return None
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation.get('translations')[0]\
        .get('translation')
    return frenchText

def frenchToEnglish(frenchText):
    ''' Function translates french text to english
    '''
    if frenchText is None:
        return None
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translation.get('translations')[0]\
        .get('translation')
    return englishText
