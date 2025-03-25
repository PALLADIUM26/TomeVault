function showBooks(){
    fetch('http://127.0.0.1:5000/showBooks', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(),
        // body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        // console.log('Success:', responseData);
        console.log('Success:', responseData);
        // Handle the response from the Python backend (e.g., display a message)
        alert(responseData.message); // Example: Display a message from the backend
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
}


function prcesssViewUsers(data) {
    let tableHTML = '<table border="1"><tr>';
    
    tableHTML += '<th>Username</th><th>Email</th><th>Password</th><th>Category</th></tr>';
    for (let i=0; i<len; i++){
        tableHTML += '<tr>';

        tableHTML += '<td>'+data[i][0]+'</td><td>'+data[i][1]+'</td><td>'+data[i][2]+'</td><td>'+data[i][3]+'</td>';
        tableHTML += '</tr>';
    }
    tableHTML += '</table>';

    document.body.innerHTML += tableHTML;
}

function viewUsers(){
    fetch('http://127.0.0.1:5000/viewUsers', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {        
        // len = responseData.message.length;
        // for (let i=0; i<len; i++){
        //     console.log(responseData.message[i])
        // }
        prcesssViewUsers(responseData.message);
        alert(responseData.message); // Example: Display a message from the backend
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });    
}