import os
from SemanticShield.errors import APIENGINEException

class OpenAISettings(object):
    ENGINE=os.environ.get('ENGINE', 'text-davinci-003')
    CHAT_ENGINE=os.environ.get('CHAT_ENGINE', 'gpt-3.5-turbo')
    if 'AZURE_CHAT_ENGINE' not in os.environ:   
        raise APIENGINEException(f"AZURE_CHAT_ENGINE not set")
    AZURE_CHAT_ENGINE=os.environ['AZURE_CHAT_ENGINE']