
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


document.getElementById('userInfoForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const location = document.getElementById('location').value;
    const radius = document.getElementById('radius').value;
    const interests = Array.from(document.getElementById('interests').selectedOptions).map(option => option.value);

    // Now you can use these values to make API calls, update the UI, etc.
    console.log(name, location, radius, interests);
});

function sendBackend() {
    var userInput;
    userInput = "liquor stores near me";
    
    url = "" + userInput;
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