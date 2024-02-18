
function sendToBack(category){
    url = "http://127.0.0.1:3000/getMain?=" + category;
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
    function searchResults(activityGroup) {
        // Perform search based on the selected activity group
        var results = getSearchResults(activityGroup); // Assuming getSearchResults function is defined in your script
      
        // Display search results
        displayResults(results);
      }
      
      function getSearchResults(activityGroup) {
        // Placeholder function to simulate search results
        // You would replace this with actual logic to fetch search results
        var results = [];
      
        // Sample search results
        if (activityGroup === 'volunteer') {
          results = [
            { title: 'Volunteer Opportunity 1', description: 'Description of volunteer opportunity 1' },
            { title: 'Volunteer Opportunity 2', description: 'Description of volunteer opportunity 2' },
            // Add more results as needed
          ];
        } else if (activityGroup === 'sports') {
          results = [
            { title: 'Sports Event 1', description: 'Description of sports event 1' },
            { title: 'Sports Event 2', description: 'Description of sports event 2' },
            // Add more results as needed
          ];
        } else if (activityGroup === 'localClub') {
          results = [
            { title: 'Local Club Activity 1', description: 'Description of local club activity 1' },
            { title: 'Local Club Activity 2', description: 'Description of local club activity 2' },
            // Add more results as needed
          ];
        }
      
        return results;
      }
      
      function displayResults(results) {
        var container = document.getElementById('searchResults');
        container.innerHTML = ''; // Clear previous results
      
        // Create HTML elements for each search result and append to the container
        results.forEach(function(result) {
          var resultElement = document.createElement('div');
          resultElement.innerHTML = '<h3>' + result.title + '</h3>' + '<p>' + result.description + '</p>';
          container.appendChild(resultElement);
        });
      }
      
  
    

}