
function sendToBack(category){
    url = "http://127.0.0.1:5500/getMain?=" + category;
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
        communities();
        
    })
    .catch(error => {
        //deal with errors
        console.error('Error:', error);
    });
}

function communities(){
    
    function showVolunteerGroup() {
      document.getElementById("volunteerGroup").style.display = "block";
      document.getElementById("sportsGroup").style.display = "none";
      document.getElementById("localClubActivities").style.display = "none";
    }

    function redirectToSportsPage() {
      // Redirect to the sports page
      window.location.href = "sports.html";
    }

    function showLocalClubActivities() {
      document.getElementById("volunteerGroup").style.display = "none";
      document.getElementById("sportsGroup").style.display = "none";
      document.getElementById("localClubActivities").style.display = "block";
    }
  
    

}