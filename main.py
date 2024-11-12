import pyttsx3

# object creation
engine = pyttsx3.init()

# Welcome text
print("Welcome to text to speech conversion agent.")

# Voice Settings : 
x = int(input("Enter '0' for male voice agent or '1' for female voice agent : "))
voices = engine.getProperty('voices')  

if(x == 0):
    # changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)
    engine.say("Welcome to the Text-to-Speech Conversion Service. I’m Bob, here to assist you with all your text-to-speech needs. Please feel free to enter any text you’d like converted.")
    engine.runAndWait()
elif(x == 1):
    #changing index, changes voices. 1 for female
    engine.setProperty('voice', voices[1].id)
    engine.say("Welcome to the Text-to-Speech Conversion Service. I’m Alice, here to assist you with all your text-to-speech needs. Please feel free to enter any text you’d like converted.")
    engine.runAndWait()

# Main Logic :
while(True): # To keep the input running
    # To accept the input :
    text = input("Me : ")

    # To break the input :
    if(text == "q"):
        engine.say("Exiting the terminal")
        engine.runAndWait()
        break

    # Passing the input to the "say" method :
    # engine.say(text)
    if(x == 0):
        print("Bob : .....")
        engine.say(text)
    elif(x == 1):
        print("Alice : .....")
        engine.say(text)

    engine.runAndWait()