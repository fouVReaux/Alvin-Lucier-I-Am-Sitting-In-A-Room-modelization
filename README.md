# Alvin Lucier - I Am Sitting In A Room - modelization
## Description
This project has been made to reproduce the Alvin Lucier's performance by convolving again and again and again.. an audio file with an impulse response of a room.
[Performance on Youtube](https://www.youtube.com/watch?v=fAxHlLK3Oyk)

Two programs are disponibles
1. The "brute force program" manage the convolution in one pass. By convolving each times the n-th output again with the impulse response Like so: Output_n = S(v) ∗ H(v) ∗ H(v) ∗ ... ∗ H(v)
2. The "You get what you want program" manage the convolution in two passes. The first pass convolv the impulse response with itself n times and store the results in a repertory. The second pass gets the user wanted responses and convolute it with the sample. Like so:
First pass : H_n(v) = H(v)^(n), Second pass : Output_n = S(v) * H_v^(n)

## Installation
This code need theses python modules :
- numpy
- matplotlib.pyplot
- scipy (scipy.io, scipy.interpolate)

Run this command in order to install modules (linux :wink:)
```
sudo apt-get install python-numpy python-matplotlib python-scipy
```
## Usage
1. "Get th'n all" program
-- Change the input file `sample/sample.wav`
-- Change the impulse responce file `sample/ir.wav`
-- Run the python program `python get_th_n_all.py` in a terminal (this may take a while)
-- Open the folder `sample/convolutions/`
-- This is it! You get all your rooms in rooms!
2. "Get what you want" program
-- Change the input file `sample/sample.wav`
-- Change the impulse responce file `sample/ir.wav`
-- Set the `nConvol` variable in order to set the number of "room in room"
-- Run the python program `python convol_generator.py` in a terminal (this may take a while)
-- Run the python program `python getNSampleConvol.py` in a terminal (this may take a while)
-- In the folder `sample/` you get two files : `sample_0.wav` and `sample_N.wav`
--- `sample_0.wav` is the original one (compressed on all the dynamic)
--- `sample_N.wav` is the N-th pass in a room 
## Note
The `sample.wav` used in demo is from [learnopengl.com](https://learnopengl.com/)
And is downlodable in full version [there](https://learnopengl.com/audio/in-practice/breakout/breakout.mp3)
## Licence
this project is under a ***GNU GPLv3*** licence
