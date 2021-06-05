import eel
from googletrans import Translator

def translation(before_lang, after_lang, sentence):
  tr = Translator()
  translated = tr.translate(sentence, src=before_lang, dest=after_lang).text
  # print(translated)
  eel.view_translated_js(translated)
