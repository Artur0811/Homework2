var elem = document.getElementById('map');
//elem.parentNode.removeChild(elem);
function init(route) {

    elem = new ymaps.Map('map', {
        center: [55.831, 37.629],
        zoom: 15,
        controls: ['smallMapDefaultSet']
    }, {
        searchControlProvider: 'yandex#search',
        restrictMapArea: [
            [55.842, 37.604],
            [55.821, 37.651]
        ]
    }),
    multiRoute = new ymaps.multiRouter.MultiRoute({
                        referencePoints: ['55.826591, 37.638033', '55.826249, 37.637578', '55.828598, 37.633872', '55.828660, 37.631427', '55.829970, 37.633791', '55.830684, 37.633393', '55.830932, 37.632602'],
                        params: {
                            routingMode: 'pedestrian'
                        }
                    }, {
                        boundsAutoApply: true
                })
    elem.geoObjects.add(multiRoute);

}

ymaps.ready(init)
