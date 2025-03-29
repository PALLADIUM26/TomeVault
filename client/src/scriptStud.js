// function becomeMember(){
//     var link = window.location.href;
//     link = link.replace("homeStud.html?","");
//     arr = link.split("/");
//     username = arr[arr.length-1];
//     location.replace("pageStud1.html?"+username);
// }

function showBorrows(){
    var link = window.location.href;
    link = link.replace("homeStud.html?","");
    arr = link.split("/");
    username = arr[arr.length-1];
    // alert(username);
    console.log(username);
    location.replace("pageStud1.html?"+username);
}

function showBorrows2(){
    var link = window.location.href;
    link = link.replace("pageStud1.html?","");
    arr = link.split("/");
    username = arr[arr.length-1];

    const data = {username: username,}
    fetch('http://127.0.0.1:5000/showBorrows', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData);
        alert(responseData.message); // Example: Display a message from the backend
        processShowBorrows(responseData.message);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
}


function processShowBorrows(data) {
    let tableHTML = '<table border="1"><tr>';
    const len = data.length;
    
    tableHTML += '<th>Username</th><th>ISBN 1</th><th>ISBN 2</th><th>ISBN 3</th><th>ISBN 4</th><th>ISBN 5</th><th>Penalty</th></tr>';
    for (let i=0; i<len; i++){
        tableHTML += '<tr>';
        for(let j=0; j<7; j++){
            tableHTML += '<td>'+data[i][j]+'</td>';
        }
        tableHTML += '</tr>';
    }
    tableHTML += '</table>';

    document.body.innerHTML += tableHTML;
}


function becomeMember(){
    var link = window.location.href;
    link = link.replace("homeStud.html?","");
    arr = link.split("/");
    username = arr[arr.length-1];

    const data = {username: username,}
    fetch('http://127.0.0.1:5000/becomeMember', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData);
        alert(responseData.message); // Example: Display a message from the backend
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
}