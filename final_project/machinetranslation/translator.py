"""
docstring
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-12-25',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translate English text to French
    """
    return language_translator.translate(
    text= english_text,
    model_id = 'en-fr').get_result()['translations'][0]['translation']

def french_to_english(french_text):
    """
    Translate French text to English
    """
    return language_translator.translate(
    text= french_text,
    model_id = 'fr-en').get_result()['translations'][0]['translation']

