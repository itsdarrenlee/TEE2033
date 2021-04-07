# After LTSPICE simulation, the data is stored using .wave spice directive to ensure constant sampling time
# To convert wave file into grc file, the following python script is used.

import numpy as np
from scipy.io import wavfile

fs, data=wavfile.read("out.wav")

data1=data/max(data)*0.25

newFile=open("testspice.dat","wb")
data1.astype(np.float32).tofile(newFile)
newFile.close()
