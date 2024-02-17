
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


function sendBackend() {
    var userInput;
    userInput = "liquor stores near me";
    //what should this url be??
    //"http://127.0.0.1:5500/getMain?=" + input
    url = "http://127.0.0.1:5500/Front%20End/thirdPlaces.html?input=" + userInput;
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
