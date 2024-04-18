import wave

infiles = []
while True:
    inp = input()
    if inp == "":
        break
    inp_formatted = f"voice_announcement/{inp}.wav"
    infiles.append(inp_formatted)

outfile = "sounds.wav"

data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
    
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()