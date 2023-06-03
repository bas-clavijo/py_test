# Importacion de modelos 
from src.models.language_model import LanguageModel

def test_get_languages_not_none():
    languages = LanguageModel.get_language()
    assert languages != None
    
def test_get_languages_has_elemets():
    languages = LanguageModel.get_language()
    assert len(languages)>0

def test_get_languages_check_elemets_length():
    languages = LanguageModel.get_language()
    for language in languages:
        assert len(language)>0
