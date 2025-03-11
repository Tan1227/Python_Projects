import os
 
if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x=input("Enter what you want me to speak: ")
        if x=="q":
            os.system('powershell -c "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye bye friend\')"')
            break
        command = f'powershell -c "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"' 
        os.system(command) 