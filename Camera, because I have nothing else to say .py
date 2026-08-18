!pip install music21
!apt-get install -y fluidsynth
!pip install midi2audio


from music21 import note, instrument, stream
from midi2audio import FluidSynth
from IPython.display import Audio
note_length= 10.0
n1 =note.Note(72)
n1.quarterLength = note_length
#n1.show("midi")#
my_note = stream.Stream()
my_note.insert(0, instrument.Accordion())
my_note.insert(0, n1)
my_note.write('midi', 'my_note.mid')
fs = FluidSynth()
fs.midi_to_audio('my_note.mid', 'output.wav')
Audio('output.wav')
