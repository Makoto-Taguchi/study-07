import eel
from googletrans import Translator

def translation(sentence):
  tr = Translator()
  translated = tr.translate(sentence, dest='ja').text
  # print(translated)
  eel.view_translated_js(translated)
