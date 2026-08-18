mport numpy as np
from IPython.display import Audio, display
naruto=input("ENTER A NOTE OR YOU WILL BE BEHEADED FROM THE MEDIEVAL TIME")
note=input("TELL ME HOW LONG YOU WANT TO HOLD THE NOTE OR ELSE!!!")
note=int(note)
aerospace=[("A",880),("A flat",831),("G",784),("F sharp",740),("F",698),("E",659),("D sharp",622),("D",587),("C sharp",554),("C",523),("B",494),("B flat",466),("A",440)]
for nota in aerospace:
  print(nota)
  if naruto==nota[0]:
    print(nota[1])
    frequency=nota[1]
# Parameters
sampling_rate = 44100  # Hz
duration =note #CHANGE DURATION(SECONDS) #        # seconds
    # Hz (B note) #KEEP CHANGING THIS#

# Generate time array
t = np.linspace(0, duration, int(sampling_rate * duration), False)

# Generate sine wave
wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Play the audio
display(Audio(wave, rate=sampling_rate))
