
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
        //communities();
        
    })
    .catch(error => {
        //deal with errors
        console.error('Error:', error);
    });
}

function openGroup(event, category) {
    sendToBack(category);
}

