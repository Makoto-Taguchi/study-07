import eel
import desktop
import trans

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def translation(before_lang, after_lang, src_sentence):
    trans.translation(before_lang, after_lang, src_sentence)

desktop.start(app_name,end_point,size)