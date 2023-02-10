var myMap;
var routes;
function init(route) {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    const postData = async (url = '', data = {}) => {
  // Формируем запрос

        const response = await fetch(url, {
        // Метод, если не указывать, будет использоваться GET
        method: 'POST',
       // Заголовок запроса
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        // Данные
        body: JSON.stringify(data)
      });
      return response.json();
    }

    myMap = new ymaps.Map('map', {
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
    menu = $('<ul class="menu"/>');

    for (var i = 0, l = groups.length; i < l; i++) {
        createMenuGroup(groups[i]);
    }

    function createMenuGroup (group) {
        var menuItem = $('<li><a href="#">' + group.name + '</a></li>'),
            collection = new ymaps.GeoObjectCollection(null, { preset: group.style }),
            submenu = $('<ul class="submenu"/>');

        myMap.geoObjects.add(collection);
        menuItem
            .append(submenu)
            .appendTo(menu)
            .find('a')
            .bind('click', function () {
                if (collection.getParent()) {
                    myMap.geoObjects.remove(collection);
                    submenu.hide();
                } else {
                    myMap.geoObjects.add(collection);
                    submenu.show();
                }
            });
        for (var j = 0, m = group.items.length; j < m; j++) {
            createSubMenu(group.items[j], collection, submenu);
        }
    }
    function createSubMenu (item, collection, submenu) {
        if (item.center == '55.826591,37.638033'){
        var submenuItem = $('<li><a href="#">' + item.name +'</a>' + "</li>")
        }
        if (item.center != '55.826591,37.638033'){
        var submenuItem = $('<li><a href="#">' + item.name +'</a>' + '<input class="messageCheckbox" type="checkbox" name=' + item.center+'><span class="checkmark" ></span>' + "</li>")
        }
        // делаю строку (ссылка, чекбокс) его имя - координаты точки
        var placemark = new ymaps.Placemark(item.center, { balloonContent: item.name });

        collection.add(placemark);
        submenuItem
            .appendTo(submenu)
            .find('a')
            .bind('click', function () {
                if (!placemark.balloon.isOpen()) {
                    placemark.balloon.open();
                } else {
                    placemark.balloon.close();
                }
                return false;
            });
    }

    menu.appendTo($('body'));

//    multiRoute = new ymaps.multiRouter.MultiRoute({
//                        referencePoints: ['55.826591, 37.638033', '55.828794, 37.629733'],
//                        params: {
//                            routingMode: 'pedestrian'
//                        }
//                    }, {
//                        boundsAutoApply: true
//                })
//    myMap.geoObjects.add(multiRoute);

    var slider = document.getElementById("myRange");
    var output = document.getElementById("time");
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
    }

    document.getElementById('desel').onclick = function () {
        var inputElements = document.getElementsByClassName('messageCheckbox')//все чекбоксы
        for(var i = 0, l = inputElements.length; i < l; i++){//рохожусь по чекбоксам
            if(inputElements[i].checked){//есть галочка то ее не будет
                inputElements[i].checked = false
            }
        }
    }
    var new_routes = []
    document.getElementById('gobtn').onclick = function () {
        //console.log(new_routes)//ранее добавленные маршруты
        for(var i = 0, l = new_routes.length; i < l; i++){
            myMap.geoObjects.remove(new_routes[i])
        }

        async function f(){
        var timeee = document.getElementById("time").innerHTML//лимит по времени
        var inputElements = document.getElementsByClassName('messageCheckbox');//получаю все чекбоксы
        var ob_poi = []//обязательные точки
        for(var i = 0, l = inputElements.length; i < l; i++){//рохожусь по чекбоксам
            if(inputElements[i].checked){//есть галочка - добавляю имя(координаты)
                ob_poi.push(inputElements[i].name)
            }
        }
        //console.log(ob_poi)//точки
        //console.log(timeee)//лимит
        // в итоге в ob_poi хранятся обязательные точки. может быть пустым

        var rez = await postData("def/", {"point" : ob_poi,"time": timeee,   // < here
            state:"inactive" })
        //console.log(rez)//результат запроса

        var fillroute = [["#000088", "#E63E92"], ["#ff9baa", "#E63E92"],["#6a38ff", "#E63E92"],["#0f93ff", "#E63E92"],["#00856f", "#E63E92"]]
        let k = 0
        if(Object.keys(rez).length === 0){
             var popup = document.getElementById('popup')
             popup.classList.toggle('active')
             window.onclick = function(event) {
                popup.className = ""
             }
        }
        for (var i in rez) {
          multiRoute = new ymaps.multiRouter.MultiRoute({
                            referencePoints: rez[i],
                            params: {
                                routingMode: 'pedestrian'
                            }
                        }, {
                            // Внешний вид путевых точек.
                            wayPointStartIconColor: "#333",
                            wayPointStartIconFillColor: "#B3B3B3",
                            // Позволяет скрыть иконки путевых точек маршрута.

                            // Внешний вид транзитных точек.
                            viaPointIconRadius: 7,
                            viaPointIconFillColor: "#000088",
                            viaPointActiveIconFillColor: "#E63E92",
                            // Внешний вид линии маршрута.
                            routeStrokeWidth: 2,
                            routeStrokeColor: fillroute[k],
                            routeActiveStrokeWidth: 6,
                            routeActiveStrokeColor: fillroute[k],

                            // Внешний вид линии пешеходного маршрута.
                            routeActivePedestrianSegmentStrokeStyle: fillroute[k],
                            routeActivePedestrianSegmentStrokeColor: fillroute[k],
                            boundsAutoApply: true
                        })
          new_routes.push(multiRoute)
          k = k+1
          myMap.geoObjects.add(multiRoute)
        }
        }
        f()
    };
}


ymaps.ready(init)