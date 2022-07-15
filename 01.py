"""
NGC 3132
SIMBAD
main_id = "NGC  3132"
ra, dec = 151.75735684271, -40.43642515362001
"""

from aladin import Aladin

# NGC 3132
target = '151.75735684271, -40.43642515362001'

a = Aladin(target=target, fov=0.1)

buttons = [
    ('P/2MASS/color', '2MASS'),
    ('P/DSS2/color', 'DSS'),
    #('CDS/P/JWST/Southern-Ring-Nebula/NIRCam', 'JWST')
    ]


a.add_survey_buttons(buttons)

hips_id = 'CDS/P/JWST/Southern-Ring-Nebula/NIRCam'
hips_name = 'Southern-Ring-Nebula'
hips_base_url = 'https://alasky.cds.unistra.fr/JWST/CDS_P_JWST_Southern-Ring-Nebula_NIRCam'
hips_max_ord = 14

a.add_image_survey(hips_id, hips_name, hips_base_url, hips_max_ord)

#a.add_vizier('I/355/gaiadr3')

a.create()
a.save('index.html')

"""
https://aladin.cds.unistra.fr/AladinLite/v3-beta/?
fov=0.06&ra=151.7573568&dec=-40.4364251&
baseImageLayer=CDS%2FP%2FunWISE%2Fcolor-W2-W1W2-W1&
overlayImageLayer=https%3A%2F%2Falasky.cds.unistra.fr%2FJWST%2FCDS_P_JWST_Southern-Ring-Nebula_NIRCam&
cooFrame=ICRS
"""

# http://aladin.unistra.fr/AladinLite/doc/API/examples/overlay-image-layer/

#https://aladin.cds.unistra.fr/AladinLite/v3-beta/?fov=0.06&ra=151.7573568&dec=-40.4364251&baseImageLayer=CDS%2FP%2FunWISE%2Fcolor-W2-W1W2-W1&overlayImageLayer=https%3A%2F%2Falasky.cds.unistra.fr%2FJWST%2FCDS_P_JWST_Southern-Ring-Nebula_NIRCam&cooFrame=ICRS