import matplotlib.pyplot as plt
import numpy as np

#filez = ['figi01', 'figi01alt', 'figi02', 'figi03']
#filez = ['figi10', 'figi11', 'figi12', 'figi13', 'figi14']
filez = ['figi12']

for f in filez:

    q = plt.imread(f + '.png')
    q[:,:,0:3] = 1.  #make white, but leave alpha modulation

    plt.imsave(f + 'w', q)

    print f, ' is done!'
