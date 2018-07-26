import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.interpolate import interp1d

def main():
    #samplerate
    Fs = 44100
    #file path
    pathDrySample = "sample/sample.wav";
    pathIR = "sample/convolutions/";
    pathConvolutionOutput = "sample/";
    nConvol = 2

    fs, dataDry = wavfile.read(pathDrySample)
    fs, dataIR = wavfile.read(pathIR+"conv_"+str(nConvol-1)+".wav")

    print("---------------------------") 
    print('START  Convolution 0 : original')
    factor = interp1d([dataDry.min(),dataDry.max()],[-0.7,0.7])
    noCov = dataDry
    wavfile.write(pathConvolutionOutput+"sample_0.wav", fs, factor(noCov))
    print('FINISH Convolution 0')
    print("---------------------------") 
    print("START  Convolution "+str(nConvol))
    convolution = np.convolve(dataDry, dataIR)*fs
    factor = interp1d([convolution.min(),convolution.max()],[-0.7,0.7])
    wavfile.write(pathConvolutionOutput+"sample_"+str(nConvol-1)+".wav", fs, factor(convolution))
    print("FINISH Convolution "+str(nConvol))
    print("---------------------------")

        
if __name__ == "__main__":
    main()
