
var name;
var description;
var locations;
var meeting_times;





function sendToBack(category){
    url = "http://127.0.0.1:3000/getCommunity?name=" + category;
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
        //call a function that does what we want
        //console.log(data.Community1.name);
        updatedSearchResults(data);
        
    })
    .catch(error => {
        //deal with errors
        console.error('Error:', error);
    });
}
function openGroup(event, category) {
    sendToBack(category);
}

function updatedSearchResults(data) {

    document.getElementById('resultText1').textContent = data.Community1.name + ": "+  data.Community1.description;
    document.getElementById('resultText2').textContent = data.Community2.name + ": "+  data.Community2.description;
    document.getElementById('resultText3').textContent = data.Community3.name + ": "+  data.Community3.description;
    document.getElementById('resultText4').textContent = data.Community4.name + ": "+  data.Community4.description;
    document.getElementById('resultText5').textContent = data.Community5.name + ": "+  data.Community5.description;
}