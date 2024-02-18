function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      center: { lat: 39.8282, lng: -100 },
      zoom: 4
    });

    var marker;

    // Add a click event listener to the map
    google.maps.event.addListener(map, 'click', function(event) {
      // Remove existing marker if present
      if (marker) {
        marker.setMap(null);
      }

      // Create a new marker at the clicked location
      marker = new google.maps.Marker({
        position: event.latLng,
        map: map,
        draggable: true,
        title: 'Drag me!'
      });

      // Add an event listener for the marker drag event
      marker.addListener('dragend', function() {
        // Get the updated coordinates after dragging the marker
        var updatedLatLng = marker.getPosition();
        console.log('Marker dragged to:', updatedLatLng.lat(), updatedLatLng.lng());
      });
    });

    /* Add a button to remove the marker
    var removeMarkerButton = document.createElement('button');
    removeMarkerButton.textContent = 'Remove Marker';
    document.body.appendChild(removeMarkerButton);*/

    removeMarkerButton.addEventListener('click', function() {
      // Remove the marker from the map
      if (marker) {
        marker.setMap(null);
        console.log('Marker removed.');
      }
    });
}