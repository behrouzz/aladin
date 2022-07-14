#https://aladin.cds.unistra.fr/AladinLite/doc/tutorials/interactive-finding-chart/


keywords = ['@BS_TARGET', '@BS_FOV', '@BS_SURVEY', '@BS_WIDTH',
            '@BS_HEIGHT', '@BS_SURBTNS', '@BS_MARKERS']

class Aladin:
    def __init__(self, target, fov=1, survey="P/DSS2/color", width=700, height=400):
        
        with open('template.txt', 'r') as f:
            self.html = f.read()

        self.target = target
        self.fov = fov
        self.survey = survey
        self.width = width
        self.height = height
        self.buttons = None
        self.markers = None


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


    def __add_survey_btn(self, value, id, label):
        return f'<input id="{id}" type="radio" name="survey" value="{value}"><label for="{id}">{label}<label>\n'

    def add_survey_buttons(self, buttons):
        self.buttons = ''
        for i in range(len(buttons)):
            self.buttons = self.buttons + self.__add_survey_btn(buttons[i][0], 'id'+str(i+1), buttons[i][1])
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

    def save(self, filename='index.html'):
        html = self.html
        for i in keywords:
            html = html.replace(i, '')
        with open(filename, 'w') as f:
            f.write(html)



a = Aladin(target='270.6003707 -23.0224839')

buttons = [
    ('P/2MASS/color', 'bs 2MASS'),
    ('P/GLIMPSE360', 'bs GLIMPSE 360'),
    ]

markers = [
    (270.332621, -23.078944, 'PSR B1758-23', 'Object type: Pulsar'),
    (270.63206,  -22.905550, 'HD 164514',    'Object type: Star in cluster'),
    (270.598121, -23.030819, 'HD 164492',    'Object type: Double star'),
    ]

a.add_survey_buttons(buttons)
a.add_markers(markers)

a.create()
a.save('index.html')
