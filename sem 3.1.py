fileObj = open("1kHz_44100Hz_16bit_05sec.wav", mode="rb")

data = fileObj.read()

print(data)