import matplotlib.pyplot as plt
import numpy as np

filez = ['figi01', 'figi01alt', 'figi02', 'figi03']

for f in filez:

    q = plt.imread(f + '.png')
    q[:,:,0:3] = 1.  #make white, but leave alpha modulation

    plt.imsave(f + 'w', q)

    print f, ' is done!'
