class Phrase:

    def __init__(self, phrase):
        self._phrase = phrase

    def __contains__(self, token):
        for wort in self._phrase:
            if wort == token:
                return True


    #Methode, die die Darstellung dieser Klasse in lesbarer Form zurückgibt
    def __str__(self):
        return " ".join(self._phrase)

    #Methode die die Darstellung dieser Klasse auf eindeutige Weise zurückgibt
    def __repr__(self):
        pass

    def head(self):
        return("head unknown")
