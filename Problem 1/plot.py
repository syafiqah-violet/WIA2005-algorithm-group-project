import gmplot

apikey = 'AIzaSyBkj8reS92qZ7sEAGzl_Z0fbVL0Zr0k5M4'

lat, lng = zip(*[
    (3.0319924887507144, 101.37344116244806),
    (3.112924170027219, 101.63982650389863),
    (3.265154613796736, 101.68024844550233),
    (2.9441205329488325, 101.7901521759029),
    (3.2127230893650065, 101.57467295692778)
])

courier = ['City-Link Express', 'Poslaju', 'GDEX', 'J&T', 'DHL']
courierAlpha = ['C', 'P', 'G', 'J', 'D']

gmap = gmplot.GoogleMapPlotter(3.209247, 101.524803, 10, apikey=apikey)
gmap.scatter(lat, lng, color='red', size=50, title=courier, label=courierAlpha)
gmap.draw("map.html")