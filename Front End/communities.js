
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
        
        
    })
    .then (function(data){
        let placeholder = document.querySelector("#data-output");
        let out= " ";
        for(i = 0; i < 15; ++i ){
            out+= `
            <tr>
                <td>${data.Community1.name} </td>
                <td>${data.Community1.description} </td>
                <td>${data.Community1.locations} </td>
                <td>${data.Community1.meeting_times} </td>

            </tr>
            `;
        }
        placeholder.innerHTML= out;
    })
    .catch(error => {
        //deal with errors
        console.error('Error:', error);
    });
}
function openGroup(event, category) {
    sendToBack(category);
}