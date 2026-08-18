!pip install music21 midi2audio
!apt-get install -y fluidsynth

from music21 import note, chord, stream, instrument, tempo, duration
from midi2audio import FluidSynth
from IPython.display import Audio

def play_stream(s):
    s.write('midi', fp='output.mid')
    FluidSynth().midi_to_audio('output.mid', 'output.wav')
    return Audio('output.wav')

helloooo= [62, 62, 66, 66, 61,0, 72,72, 62, 62, 66, 66,61,72,72]
hhahaahah=[1, 1, 1, 1, 1,1, 1, 1, 1, 1,1,1,1,1,1]
s= stream.Stream()

for i in range(len(helloooo)):
    if helloooo [i] == 0:
      new_note = note.Rest()
    else:
      new_note = note.Note(helloooo[i])
    new_note.duration.quarterLength = hhahaahah[i]
    s.append(new_note)

play_stream(s)
