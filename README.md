**Author:** [Behrouz Safari](https://behrouzz.github.io/)<br/>
**Website:** [AstroDataScience.Net](http://astrodatascience.net/)<br/>

# Pythonic tool to work with Aladin Lite

*Check these links:*<br/>
* [Build an interactive sky map with Aladin Lite](https://aladin.cds.unistra.fr/AladinLite/doc/tutorials/interactive-finding-chart/)<br/>
* [Image surveys](http://aladin.unistra.fr/hips/list)<br/>


## Example 1 : add surveys and markers

```python
from aladin import Aladin

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
```


## Example 2 : add SIMBAD and VizieR layers

```python
from aladin import Aladin

a = Aladin(target='270.6003707 -23.0224839')

a.add_simbad()

a.add_vizier('I/239/hip_main')

a.create()
a.save('index.html')
```

You can pass optional arguments *target* and *radius* to both *add_simbad* and *add_vizier* methods.

See more at [astrodatascience.net](https://astrodatascience.net/)
