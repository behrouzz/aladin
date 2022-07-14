**Author:** [Behrouz Safari](https://behrouzz.github.io/)<br/>
**Website:** [AstroDataScience.Net](http://astrodatascience.net/)<br/>

# Pythonic tool to work with Aladin Lite

Ref: [Build an interactive sky map with Aladin Lite](https://behrouzz.github.io/](https://aladin.cds.unistra.fr/AladinLite/doc/tutorials/interactive-finding-chart/)<br/>

## Example

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


See more at [astrodatascience.net](https://astrodatascience.net/)
