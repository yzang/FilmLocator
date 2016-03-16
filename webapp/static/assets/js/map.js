/**
 * Created by Yiming on 3/15/2016.
 */
function animateElement(parentElement){
    $(parentElement).addClass('idle');
    setTimeout(function() {
        $(parentElement).find('.animate').each(function(i){
            if( $(parentElement).hasClass('idle') ){
                $(this).addClass('idle');
                $(this).css('transition-delay',(i*transitionDelay)+'s');
                $(this).css('-webkit-transition-delay',(i*transitionDelay)+'s');
            }
        });
    }, transitionDelay);
}

function removeAnimation(parentElement){
    $(parentElement).find('.animate').each(function(){
        $(this).removeClass('idle');
    });
}

function addMarkers(map,json){
        var newMarkers = [];
        var markerClicked = 0;
        var activeMarker = false;
        var lastClicked = false;

        for (var i = 0; i < json.length; i++) {
            // Google map marker content

            var markerContent = document.createElement('DIV');
            markerContent.innerHTML =
                '<div class="map-marker">' +
                    '<div class="icon">' +
                    '<img src="/static/assets/img/marker.png">' +
                    '</div>' +
                '</div>';
            // Create marker on the map
            var marker = new RichMarker({
                position: new google.maps.LatLng( json[i].latitude, json[i].longitude ),
                map: map,
                draggable: false,
                content: markerContent,
                flat: true
            });
            newMarkers.push(marker);

            // Create infobox for marker
            var infoboxContent = document.createElement("div");
            infoboxContent.innerHTML = drawInfobox(json, i);

            var infoboxOptions = {
                content: infoboxContent,
                disableAutoPan: false,
                pixelOffset: new google.maps.Size(-150, -20),
                zIndex: null,
                alignBottom: true,
                boxClass: "infobox",
                enableEventPropagation: false,
                closeBoxMargin: "10px 10px -30px 0px",
                closeBoxURL: "/static/assets/img/close-infobox.png",
                infoBoxClearance: new google.maps.Size(1, 1)
            };

            // Create new markers
            newMarkers[i].infobox = new InfoBox(infoboxOptions);

            // Show infobox after click

            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                    google.maps.event.addListener(map, 'click', function(event) {
                        lastClicked = newMarkers[i];
                    });
                    activeMarker = newMarkers[i];
                    if( activeMarker != lastClicked ){
                        for (var h = 0; h < newMarkers.length; h++) {
                            newMarkers[h].content.className = 'marker-loaded';
                            removeAnimation('.infobox');
                            newMarkers[h].infobox.close();
                        }
                        newMarkers[i].infobox.open(map, this);
                        newMarkers[i].infobox.setOptions({ boxClass:'fade-in-marker'});
                        newMarkers[i].content.className = 'marker-active marker-loaded';
                        markerClicked = 1;
                    }
                    google.maps.event.addListener(newMarkers[i].infobox, 'domready', function(){
                            animateElement('.infobox');
                        });
                }
            })(marker, i));


            // Fade infobox after close is clicked

            google.maps.event.addListener(newMarkers[i].infobox, 'closeclick', (function(marker, i) {
                return function() {
                    activeMarker = 0;
                    newMarkers[i].content.className = 'marker-loaded';
                    newMarkers[i].infobox.setOptions({ boxClass:'fade-out-marker' });
                    removeAnimation('.infobox');
                }
            })(marker, i));
        }

        // Close infobox after click on map

        google.maps.event.addListener(map, 'click', function(event) {
            if( activeMarker != false && lastClicked != false ){
                if( markerClicked == 1 ){
                    activeMarker.infobox.open(map);
                    activeMarker.infobox.setOptions({ boxClass:'fade-in-marker'});
                    activeMarker.content.className = 'marker-active marker-loaded';
                }
                else {
                    markerClicked = 0;
                    activeMarker.infobox.setOptions({ boxClass:'fade-out-marker' });
                    activeMarker.content.className = 'marker-loaded';
                    removeAnimation('.infobox');
                    setTimeout(function() {
                        activeMarker.infobox.close();
                    }, 350);
                }
                markerClicked = 0;
            }
            if( activeMarker != false ){
                google.maps.event.addListener(activeMarker, 'click', function(event) {
                    markerClicked = 1;
                    removeAnimation('.infobox');
                });
            }
            markerClicked = 0;
        });

        // Create marker clusterer

        var clusterStyles = [
            {
                url: '/static/assets/img/cluster.png',
                height: 42,
                width: 42
            }
        ];

        var markerCluster = new MarkerClusterer(map, newMarkers, { styles: clusterStyles, maxZoom: 19 });

        // Dynamic loading markers and data from JSON
        google.maps.event.addListener(map, 'idle', function() {
            var visibleArray = [];
            for (var i = 0; i < json.data.length; i++) {
                if (map.getBounds().contains(newMarkers[i].getPosition())) {
                    visibleArray.push(newMarkers[i]);
                    $.each(visibleArray, function (i) {
                        setTimeout(function () {
                            if (map.getBounds().contains(visibleArray[i].getPosition())) {
                                if (!visibleArray[i].content.className) {
                                    visibleArray[i].setMap(map);
                                    visibleArray[i].content.className += 'bounce-animation marker-loaded';
                                    markerCluster.repaint();
                                }
                            }
                        }, i * 50);
                    });
                } else {
                    newMarkers[i].content.className = '';
                    newMarkers[i].setMap(null);
                }
            }
        });


        // Autocomplete address ----------------------------------------------------------------------------------------

        var input = document.getElementById('location') ;
        var autocomplete = new google.maps.places.Autocomplete(input, {
            types: ["geocode"]
        });
        autocomplete.bindTo('bounds', map);
        google.maps.event.addListener(autocomplete, 'place_changed', function() {
            var place = autocomplete.getPlace();
            if (!place.geometry) {
                return;
            }
            if (place.geometry.viewport) {
                map.fitBounds(place.geometry.viewport);
                map.setZoom(14);
            } else {
                map.setCenter(place.geometry.location);
                map.setZoom(14);
            }

            //marker.setPosition(place.geometry.location);
            //marker.setVisible(true);

            var address = '';
            if (place.address_components) {
                address = [
                    (place.address_components[0] && place.address_components[0].short_name || ''),
                    (place.address_components[1] && place.address_components[1].short_name || ''),
                    (place.address_components[2] && place.address_components[2].short_name || '')
                ].join(' ');
            }
        });
    }

$(document).ready(function ($) {
    // Resize the map dynamically -----------------------------------------------------------------------------
    if ($(window).width() < 768) {
        $('#search-collapse').removeClass('in');
        $('#search-collapse').height(0)
    }
    $('.map-wrapper').height($(window).height() - $('#header').height() - 1 - $('#search-collapse').height());

    $('.fullscreen-map #search-collapse').on('hidden.bs.collapse shown.bs.collapse', function () {
        $('.map-wrapper').height($(window).height() - $('#header').height() - 1 - $('#search-collapse').height())
        google.maps.event.trigger(map, "resize");
    });
    $(window).resize(function () {
        $('.map-wrapper').height($(window).height() - $('#header').height() - 1 - $('#search-collapse').height())
        google.maps.event.trigger(map, "resize");
    });

    // build the map -------------------------------------------------------------
    var _latitude = 37.77493;
    var _longitude = -122.419416;
    var jsonPath = '/static/assets/json/films.json';
    var center = new google.maps.LatLng(_latitude, _longitude);
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: center,
        disableDefaultUI: false,
        panControl: true,
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.LARGE,
            position: google.maps.ControlPosition.RIGHT_TOP
        }
    });
    // Load JSON data and create Google Maps
    $.getJSON(jsonPath)
            .done(function (json) {
                addMarkers(map, json);
            })
            .fail(function (jqxhr, textStatus, error) {
                console.log(error);
            })

});

