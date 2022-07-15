#https://aladin.cds.unistra.fr/AladinLite/doc/tutorials/interactive-finding-chart/


keywords = ['@BS_TARGET', '@BS_FOV', '@BS_SURVEY', '@BS_WIDTH',
            '@BS_HEIGHT', '@BS_SURBTNS', '@BS_MARKERS',
            '@BS_SIMBAD', '@BS_VIZIER', '@BS_EPOIMG', '@BS_IMGSUR']

class Aladin:
    def __init__(self, target, fov=1, survey="P/DSS2/color", width=700, height=700):
        
        with open('template.txt', 'r') as f:
            self.html = f.read()

        self.target = target
        self.fov = fov
        self.survey = survey
        self.width = width
        self.height = height
        self.buttons = None
        self.markers = None
        self.__simbad = None
        self.__vizier = None
        self.__image = None
        self.__imgsurvey = None


    def create(self):
        self.html = self.html.replace('@BS_TARGET', self.target)
        self.html = self.html.replace('@BS_FOV', str(self.fov))
        self.html = self.html.replace('@BS_SURVEY', self.survey)
        self.html = self.html.replace('@BS_WIDTH', str(self.width))
        self.html = self.html.replace('@BS_HEIGHT', str(self.height))
        if self.buttons is not None:
            self.html = self.html.replace('@BS_SURBTNS', self.buttons)
            
        if self.markers is not None:
            self.html = self.html.replace('@BS_MARKERS', self.markers)
        if self.__simbad is not None:
            self.html = self.html.replace('@BS_SIMBAD', self.__simbad)
        if self.__vizier is not None:
            self.html = self.html.replace('@BS_VIZIER', self.__vizier)
        if self.__image is not None:
            self.html = self.html.replace('@BS_EPOIMG', self.__image)
        if self.__imgsurvey is not None:
            self.html = self.html.replace('@BS_IMGSUR', self.__imgsurvey)

    def __add_survey_btn(self, value, id, label):
        return f'<input id="{id}" type="radio" name="survey" value="{value}"><label for="{id}">{label}<label>\n'

    def add_survey_buttons(self, buttons):
        btn_start_char = self.html.find('@BS_SURBTNS')
        self.buttons = ''
        for i in range(len(buttons)):
            self.buttons = self.buttons + self.__add_survey_btn(buttons[i][0], 'id'+str(i+1), buttons[i][1])
        self.__btn_end_char = btn_start_char -len('@BS_SURBTNS') + len(self.buttons)
        self.create()
        

    def __add_marker(self, n, ra, dec, title, desc):
        return f"var marker{n} = A.marker({ra}, {dec}, {{popupTitle: '{title}', popupDesc: '{desc}'}});\n"

    def add_markers(self, markers):
        self.markers = ''
        for i in range(len(markers)):
            self.markers = self.markers + self.__add_marker(i+1, markers[i][0], markers[i][1], markers[i][2], markers[i][3])
        self.markers = self.markers + "var markerLayer = A.catalog({color: '#800080'});\n"
        self.markers = self.markers + "aladin.addCatalog(markerLayer);\n"
        tmp = ''
        for i in range(len(markers)):
            tmp = tmp + f'marker{i+1}, '
        self.markers = self.markers + f"markerLayer.addSources([{tmp}]);\n"
        self.create()

    def add_simbad(self, target=None, radius=None):
        if target is None:
            target = self.target
        if radius is None:
            radius = self.fov / 3
        self.__simbad = f"aladin.addCatalog(A.catalogFromSimbad('{target}', {radius}, {{shape: 'plus', color: '#5d5', onClick: 'showTable'}}));"
        self.create()
        

    def add_vizier(self, table=None, target=None , radius=None):
        if table is None:
            table = 'I/239/hip_main'
        if target is None:
            target = self.target
        if radius is None:
            radius = self.fov / 4
        self.__vizier = f"aladin.addCatalog(A.catalogFromVizieR('{table}', '{target}', {radius}, {{shape: 'square', sourceSize: 8, color: 'red', onClick: 'showPopup'}}));"
        self.create()

    def add_image(self, url):
        self.__image = f"aladin.displayJPG('{url}');"

    def add_image_survey(self, hips_id, hips_name, hips_base_url, hips_max_ord, coord_frame='equatorial', format='png'):
        tmp = 'aladin.setOverlayImageLayer(aladin.createImageSurvey('
        #tmp = 'aladin.setImageSurvey(aladin.createImageSurvey('
        self.__imgsurvey = tmp + f"'{hips_id}', '{hips_name}', '{hips_base_url}', '{coord_frame}', {hips_max_ord}, {{imgFormat: '{format}'}}));"
        radio = f'<input id="id999" type="radio" name="survey" value="{hips_id}"><label for="id999">{hips_name}<label>\n'
        self.html = self.html[:self.__btn_end_char] + radio + '\n' + self.html[self.__btn_end_char:]
        

    def save(self, filename='index.html'):
        html = self.html
        for i in keywords:
            html = html.replace(i, '')
        with open(filename, 'w') as f:
            f.write(html)

