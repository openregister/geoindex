var getPosition = function(event) {
    event.preventDefault();
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(function(position) {
        console.log('lat:' + position.coords.latitude + '/long:'+ position.coords.longitude);
        getBoundary(position);
      });
    } else {
      alert('geolocation not available');
      return {};
    }
  };

var getBoundary = function(position) {
  $.ajax({
    type: 'GET',
    url: '/location/'+ position.coords.latitude+'/'+ position.coords.longitude+'.geojson',
    success: function(data) {
      console.log(data);
      var template = $.templates("#location-template"),
          html = template.render({
            'latitude': position.coords.latitude,
            'longitude': position.coords.longitude,
            'boundaryName': data.properties.name

        });
        $('#registration-district').append(html);
        renderMap(position.coords.latitude, position.coords.longitude, data);
    },
    error: function() {
      console.log("error");
    }
   });
}

var renderMap = function(latitude, longitude, geojson) {

  L.mapbox.accessToken = 'pk.eyJ1IjoiYXNoaW1hbGkiLCJhIjoiZGRkYmJiZDVjY2IwOTY4ODczZWE2OGFhM2Q0MjA3M2YifQ.C9NNJLCY_BQjtdfdDswlBg';

  var map = L.mapbox.map('map', 'ashimali.ec6806c6');
  var featureLayer = L.mapbox.featureLayer()
    .setGeoJSON(geojson).addTo(map);

  map.fitBounds(featureLayer.getBounds());
  L.marker([latitude, longitude]).addTo(map);

}

$(document).ready(function() {
  $("#current-location").click(getPosition);
});
