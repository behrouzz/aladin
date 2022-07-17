from gaiadr3 import DataLink, GaiaObject, sql2df
import pandas as pd
import matplotlib.pyplot as plt



def step1_download(sources):
    dl = DataLink(source_id=sources, retrieval_type='ALL')
    dl.download()
    objects = dl.get_objects()
    return objects


def step2_plot(objects):
    N = len(objects)
    fig, ax = plt.subplots(N, 1)

    for i, s in enumerate(objects):
        g = GaiaObject(s)
        g.read_ancillary(adr=f'data/{s}')
        if g.has['XP_SAMPLED']:
            ax[i].plot(g.xp_samp['wavelength'], g.xp_samp['flux'])
            ax[i].grid()
    plt.show()


def step3_download_sql(sources):
    df,_ = sql2df(f'SELECT @COLS FROM @MT WHERE source_id IN {str(tuple(sources))}')
    df.set_index('source_id').to_csv('data/gaia.csv')

    
def step4_read_csv():
    df = pd.read_csv('data/gaia.csv')
    df.loc[df['source_id']==5420219732228461184, 'name'] = 's1'
    df.loc[df['source_id']==5420219732233481472, 'name'] = 's1b'
    df.loc[df['source_id']==5420219624853996672, 'name'] = 's2'

    df = df[['name', 'parallax', 'distance_gspphot', 'pmra', 'pmdec',
           'radial_velocity', 'teff_gspphot', 'logg_gspphot', 'phot_g_mean_mag',
           'phot_bp_mean_mag', 'phot_rp_mean_mag']]

    df.columns = ['name', 'plx', 'dist', 'pmra', 'pmdec',
           'rv', 'teff', 'logg', 'g', 'b', 'r']
    df = df.sort_values('name')
    return df


s1 = '5420219732228461184'
s1b = '5420219732233481472'
s2 = '5420219624853996672'

sources = [s1, s1b, s2]


##objects = step1_download(sources)
##step2_plot(objects)
##step3_download_sql(sources)
##step4_read_csv()
