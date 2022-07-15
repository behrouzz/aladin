from gaiadr3 import DataLink
import matplotlib.pyplot as plt

sources = [5420219732228461184, 5420219624853996672]
dl = DataLink(source_id=sources, retrieval_type='ALL')
dl.download()

obs = dl.get_objects()

df0 = obs[0].xp_samp
df1 = obs[1].xp_samp

fig, ax = plt.subplots(2, 1)
ax[0].plot(df0['wavelength'], df0['flux'], c='b')
ax[1].plot(df1['wavelength'], df1['flux'], c='r')
ax[0].grid()
ax[1].grid()
plt.show()
