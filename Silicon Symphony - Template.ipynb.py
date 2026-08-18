!pip install music21 midi2audio
!apt-get update -qq
!apt-get install -y fluidsynth lilypond musescore > /dev/null
!apt-get install --reinstall -y fluid-soundfont-gm

from music21 import note, chord, stream, instrument, tempo, duration, environment
from midi2audio import FluidSynth
from IPython.display import Audio, Image, display
from google.colab import files
import subprocess
import os

us = environment.UserSettings()
us['lilypondPath'] = '/usr/bin/lilypond'
us['musescoreDirectPNGPath'] = '/usr/bin/mscore'

def play_stream(s):
    midi_path = 'output.mid'
    wav_path = 'output.wav'

    # Write the midi file safely
    s.write('midi', fp=midi_path)

    # Convert using explicit soundfont location
    fs = FluidSynth(sound_font='/usr/share/sounds/sf2/FluidR3_GM.sf2')
    fs.midi_to_audio(midi_path, wav_path)

    display(Audio(wav_path))

    # files.download(midi_path) #Uncomment to save file to computer


def show_music(s):
    # Lilypond writes out files as 'output.png' or 'output-1.png'
    # Force writing explicitly to ensure the image acts predictably
s.write('lily.png', fp='output')

    # Check if lilypond output with structural page suffixes exists
    if os.path.exists('output.png'):
        display(Image('output.png'))
    elif os.path.exists('output-1.png'):
        display(Image('output-1.png'))
    else:
        print("Error: Sheet music compilation failed to write an image file.")

# --- WRITE CODE BELOW --- #
#Step 1: Define a scale in a list

import random
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
