!pip install music21 midi2audio
!apt-get install -y fluidsynth

from music21 import note, stream, volume
from midi2audio import FluidSynth
from IPython.display import Audio
import random

def play_stream(s):
    s.write('midi', fp='output.mid')
    FluidSynth().midi_to_audio('output.mid', 'output.wav')
    return Audio('output.wav')

#Step 1: Define a scale in a list
C_scale = [60, 62, 64, 65, 67, 69, 71, 72]
s = stream.Stream()

melody_length = 13
curr_volume = 20

#Step 1: Initialize Counter
count = 0

#Step 2: Create Loop that Increments count variable
while count < melody_length:
    chance = random.randint(60, 72)
    if chance in C_scale:
        pass
    else:
        chance -= 1
        new_note = note.Note(chance)

    new_note = note.Note(chance)
    new_note.volume.velocity = curr_volume

    #Step 3: Check if count is a multiple of 4
    if count % 2 == 0:
        #Step 4: adjust velocity
        curr_volume += 20

    s.append(new_note)
    count += 1

#Step 5: Add a finishing note
final_note = note.Note(72)
s.append(final_note)

play_stream(s)
