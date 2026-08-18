!pip install music21
!apt-get install -y fluidsynth
!pip install midi2audio

from music21 import note, instrument, stream
from midi2audio import FluidSynth
from IPython.display import Audio
doorbell_stream = stream.Stream()
yaya= [1,0.5,0.5,1,1,0.5,0.5,0.5,0.5,0.5]
YAHOO= [67, 64, 60, 62, 55, 55, 59, 62, 65, 64, 60]
for cactus in YAHOO:
  nhello =note.Note(cactus)
  nhello.quarterLength = 0.2
  doorbell_stream.append(nhello)

doorbell_stream.insert(0, instrument.Marimba())
doorbell_stream.write('midi', 'my_note.mid')
fs = FluidSynth()
fs.midi_to_audio('my_note.mid', 'output.wav')
Audio('output.wav')

