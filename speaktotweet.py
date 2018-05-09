from tkinter import *
import speech_recognition as sr
import time
from keys import api

class Load_Window:
    def __init__(self, master):
        self.record_tweet_button = Button(tk, text='SpeakToTweet', command=self.SpeakToTweet)
        self.tweet_text_label = Label(tk, text='User/Company Name')
        self.tweet_text_label.grid(row=0, column=0)
        self.record_tweet_button.grid(row=0, column=1)
        
    def SpeakToTweet(self):
        print('SpeakToTweet!\n')
        while True:
            rec = sr.Recognizer()
            with sr.Microphone() as source:
                tweet_audio = rec.listen(source)    

            try:
                print('recovering text\n')
                tweet_text = rec.recognize_google(tweet_audio)
                print('Tweeting: \n{}\n' .format(tweet_text))
                api.update_status(status = tweet_text)
                print('Keep Talking!')
            
            except sr.UnknownValueError:
                print('I cannot understand you')
                time.sleep(3)
                print('Come again?')
                
            except sr.RequestError as e:
                print('Request Error '.format(e))

            except:
                word = rec.recognize_google(tweet_audio)
                if (word == 'goodbye'):
                    print('Gooodbye Sir/Madam')
                    break
                else:
                    pass

tk = Tk()
load = Load_Window(tk)
tk.mainloop()
