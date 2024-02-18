
// Declare map and marker variables in the global scope
var map;
var marker;
var locationName;
var locationAddress;
var locationOpenStatus;
var locationRating;
var locationData;


// Get the element with id="defaultOpen" and click on it
//document.getElementById("defaultOpen").click();
// Get the form element

document.addEventListener('DOMContentLoaded', function () {
  // Get the form element
  var form = document.getElementById('userInfo');

  // Check if the form element exists before adding an event listener
  if (form != null) {
    form.addEventListener('submit', function(event) {
      // Prevent the form from being submitted normally
      event.preventDefault();

      // Get the input values
      var location = document.getElementById('location').value;
      var activity = document.getElementById('activity').value;
      var category = document.getElementById('category').value;

      // Pass the input values to the sendBackend function
      sendBackend(location, activity, category);
    });
  } else {
    console.error("Form element with ID 'form' not found");
  }
});


function sendBackend(location, activity, category) {
    //console.log("sendBackend Called");
    var userInput = location + " " + activity + " " + category;

    url = "http://127.0.0.1:3000/getThirdPlace?string=" + userInput;
    fetch(url, {
        method: 'GET',
    }).then(response => {
        //see if response is OK
        if(!response.ok) {
            throw new Error('HTTP error! Status: ${response.status}');
        }
        return response.json();
    })
    .then(data =>{
        if (data.candidates && data.candidates.length > 0) {
    
            // //do stuff to data

            var address = data.candidates[0].formatted_address;
            geocode(address, function(latitude, longitude) {
                console.log(latitude, longitude);
                updateLocation(latitude, longitude);
            });
            console.log(data);
            updatedSearchResults(data);
        } else {
            console.error('Candidates array is empty or not found in data:', data);
        }
    })
    .catch(error => {
        //deal with errors
        console.error('Error:', error);
    });
}

function geocode(address, callback) {
    var geocodingUrl = "https://maps.googleapis.com/maps/api/geocode/json";
    fetch(`${geocodingUrl}?address=${encodeURIComponent(address)}&key=AIzaSyA5L1utCSQOnj7d-MKRU8kLUopQ3DUVE38`)
        .then(response => response.json())
        .then(data => {
            if (data.results && data.results.length > 0) {
                var latlng = data.results[0].geometry.location;
                callback(latlng.lat, latlng.lng);
            }
        })
        .catch(error => console.error(error));
}

function initMap() {
    var location = {lat: 37.35, lng: -121.95};

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: location
    });

    marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

// Function to update the map and marker
function updateLocation(latitude, longitude) {
    var newLocation = {lat: latitude, lng: longitude};
    map.setCenter(newLocation);
    marker.setPosition(newLocation);
}

document.getElementById('userInfo').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from being submitted normally

    // Display the window
    document.getElementById('searchResult').style.display = 'block';

    // You can also update the content of the window here, if needed
});

function updatedSearchResults(data) {
    if (data.candidates && data.candidates.length > 0) {
        locationName = data.candidates[0].name || "";
        locationRating = data.candidates[0].rating || "";
        locationOpen = data.candidates[0].opening_hours ? data.candidates[0].opening_hours.open_now : null;
        locationOpenStatus = (locationOpen !== null) ? (locationOpen ? "Open" : "Closed") : "";

        locationAddress = data.candidates[0].formatted_address || "";

        console.log(locationOpen);
        console.log(locationOpenStatus);
        console.log(locationAddress);
        console.log(locationRating);
        console.log(locationName);

        // Update the HTML elements only if the corresponding data exists
        if (locationName !== "") {
            document.getElementById('LocationName').textContent = locationName;
        }

        if (locationRating !== "") {
            document.getElementById('LocationRating').textContent = locationRating + " stars";
        }

        if (locationOpenStatus !== "") {
            document.getElementById('LocationOpenStatus').textContent = locationOpenStatus;
        }

        if (locationAddress !== "") {
            document.getElementById('LocationAddress').textContent = locationAddress;
        }
    } else {
        console.error('Candidates array is empty or not found in data:', data);
    }
}