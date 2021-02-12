import speech_recognition as sr

re=sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
#print(dir(sr))
def voiceinput():
    print("Speak Country name...")
    with sr.Microphone() as source:
        audio = re.listen(source)
    txt=re.recognize_google(audio)
    return txt
data = voiceinput()
print(data)


if data == India:
    print("balle")
