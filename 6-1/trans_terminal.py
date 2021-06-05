from googletrans import Translator

tr = Translator()
sentence = input("英語を入力してください：")
translated = tr.translate(sentence, dest='ja')
print(translated.text)