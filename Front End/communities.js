
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
    if(data.Community1.category == "volunteer"){
        document.getElementById('resultText0').textContent = "Volunteering Based Communities:";
    }
    if(data.Community1.category == "social"){
        document.getElementById('resultText0').textContent = "Social Based Communities:";
    }
    if(data.Community1.category == "fitness"){
        document.getElementById('resultText0').textContent = "Fitness Based Communities:";
    }

    document.getElementById('resultText1').textContent = data.Community1.name + ": "+  data.Community1.description + " " + data.Community1.meeting_times;
    document.getElementById('resultText2').textContent = data.Community2.name + ": "+  data.Community2.description + " " + data.Community2.meeting_times;
    document.getElementById('resultText3').textContent = data.Community3.name + ": "+  data.Community3.description + " " + data.Community3.meeting_times;
    document.getElementById('resultText4').textContent = data.Community4.name + ": "+  data.Community4.description + " " + data.Community4.meeting_times;
    document.getElementById('resultText5').textContent = data.Community5.name + ": "+  data.Community5.description + " " + data.Community5.meeting_times;
}