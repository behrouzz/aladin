from gaiadr3 import GaiaObject
import matplotlib.pyplot as plt

s1 = '5420219732228461184'
s2 = '5420219624853996672'

g1 = GaiaObject(s1)
g1.read_ancillary(adr=f'data/{s1}')

g2 = GaiaObject(s2)
g2.read_ancillary(adr=f'data/{s2}')

fig, ax = plt.subplots(2, 1)
ax[0].plot(g1.xp_samp['wavelength'], g1.xp_samp['flux'], c='b')
ax[1].plot(g2.xp_samp['wavelength'], g2.xp_samp['flux'], c='r')
ax[0].grid()
ax[1].grid()
plt.show()

