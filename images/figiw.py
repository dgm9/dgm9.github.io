import matplotlib.pyplot as plt
import numpy as np

filez = ['figi12fixed', 'figi13fixed']

for f in filez:

    q = plt.imread(f + '.png')
    q[:,:,0:3] = 1.  #make white, but leave alpha modulation

    plt.imsave(f + 'w', q)

    print f, ' is done!'
