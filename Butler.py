import pyautogui as pag
import time
import sys

slp = 10
if (len(sys.argv) > 1 ):
    slp = int(sys.argv[1])

print(f"waiting for {slp} seconds")
time.sleep(slp) # Allow time to make discord the active text entry box
print("queing music")


# could open and cast to a list right away, for randomization 
TIME_BETWEEN_ENTRIS = 0.5
prefix = "m!"
command = "play"

with open("songsAndArtistList.txt", 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    if len(line) > 5:
        while line != '':  # The EOF char is an empty string, instead of something sensible
            
            pag.write(prefix + command + " " + line , interval=0.025) #interval is time between each key press
            pag.press("enter")
            
            time.sleep(TIME_BETWEEN_ENTRIS)
            
            line = reader.readline()
