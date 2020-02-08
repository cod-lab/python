import gtts
import os

mytext = "Hello Ankit Tayal, oh sorry, Unemployed Ankit Tayal. khali bethe story check karne wale tayal"
txt2 = "ohhhhhh ravi ravi ravi, u r my ravi teja...."
myvoice = gtts.gTTS(text=txt2,lang='en')
myvoice.save("speech1.mp3")
os.system("speech1.mp3")