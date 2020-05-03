from Phrase import Phrase
from NounPhrase import NounPhrase
phrase = Phrase("mit einem Satz".split()) #Erstellen einer neuen Instanz der Klasse Phrase
if "Satz" in phrase:
    print("Found it!")
print(phrase, phrase.head())

noun_phrase = NounPhrase("der Satz".split()) #Erstellen einer neuen Instanz der Klasse NounPhrase
print(noun_phrase, noun_phrase.head())
