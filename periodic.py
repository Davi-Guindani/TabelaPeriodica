import periodictable
from googletrans import Translator

def periodic(numAtomico: int):
    def translate_text(text):
        translator = Translator()
        translated = translator.translate(text, src='en', dest='pt')
        return translated.text
    
    elemento = periodictable.elements[numAtomico]

    lista = []
    lista.append(elemento.number)
    lista.append(elemento.symbol)
    lista.append(translate_text(elemento.name).title())
    lista.append(elemento.mass)
    lista.append(elemento.density)
    return lista