import speech_recognition as srec
from gtts import gTTS
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Unduh stopwords dan punkt (untuk tokenisasi)
nltk.download('punkt_tab')
nltk.download('stopwords')

def mendengarkan_perintah():
    recognizer = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan....')
        audio = recognizer.listen(source, phrase_time_limit=5)
        try: 
            print('Diterima...')
            hasil_dengar = recognizer.recognize_google(audio, language='id-ID')
            print("Teks yang diterima:", hasil_dengar)
        except: 
            hasil_dengar = ""
            print("Tidak ada suara yang dikenali.")
        return hasil_dengar

def proses_nlp(teks):
    # Tokenisasi
    kata_kata = word_tokenize(teks)
    print("Setelah tokenisasi:", kata_kata)
    
    # Hapus stop words
    stop_words = set(stopwords.words("indonesian"))
    kata_filtered = [word for word in kata_kata if word.lower() not in stop_words]
    print("Setelah menghapus stop words:", kata_filtered)
    
    return " ".join(kata_filtered)

def suara_AI(teks):
    bahasa = 'id'
    namafile = 'SuaraAI.mp3'
    def putar_suara():
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        os.system(f'start {namafile}')
    putar_suara()

def jalankan():
    perintah_suara = mendengarkan_perintah()
    if perintah_suara:
        teks_proses = proses_nlp(perintah_suara)
        suara_AI(teks_proses)
    else:
        suara_AI("Maaf, saya tidak mendengar perintah apapun.")

jalankan()
