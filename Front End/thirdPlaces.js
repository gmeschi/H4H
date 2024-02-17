
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

// Get the form element
var form = document.getElementById('searchForm');

// Add an event listener for the submit event
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

function sendBackend(location, activity, category) {
    var userInput = location + " " + activity + " " + category;
    userInput = "liquor stores near me";
    //what should this url be??
    //"http://127.0.0.1:5500/Front%20End/thirdPlaces.html?input=" + userInput;
    //"http://127.0.0.1:5500/getMain?=" + input
    url = "http://127.0.0.1:5500/getMain?=" + userInput;
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
        //do stuff to data
        console.log(data);
    })
    .catch(error => {
        //deal with errors
        console.error('Error:', error);
    });


}
