from aladin import Aladin

a = Aladin(target='151.75735684271, -40.43642515362001', fov=0.1)

buttons = [
    ('P/2MASS/color', '2MASS'),
    ('P/DSS2/color', 'DSS'),
    ]

a.add_survey_buttons(buttons)

hips_id = 'CDS/P/JWST/Southern-Ring-Nebula/NIRCam'
hips_name = 'Southern-Ring-Nebula'
hips_base_url = 'https://alasky.cds.unistra.fr/JWST/CDS_P_JWST_Southern-Ring-Nebula_NIRCam'
hips_max_ord = 14

a.add_image_overlayer(hips_id, hips_name, hips_base_url, hips_max_ord, slider=True)

a.create()
a.save('index.html')
