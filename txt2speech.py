from gtts import gTTS
import os

myText = " My mama always said, life was like a box of chocolates. You never know what you're gonna get."

language = 'es'

output = gTTS(text=myText,lang=language,slow=False)

output.save("output.mp3")

os.system("open output.mp3")
