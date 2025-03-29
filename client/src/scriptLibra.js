function searchBooks(){
    location.href = "pageLibra1.html";
}

function issueBooks(){
    location.href = "pageLibra3.html"
}

function addMember(){
    location.href = "pageLibra2.html"
}

function processSearchBooks(data) {
    let tableHTML = '<table border="1"><tr>';
    len = data.length;
    
    tableHTML += '<th>ISBN</th><th>Book name</th><th>Author</th><th>Quantity</th><th>Cost</th></tr>';
    for (let i=0; i<len; i++){
        tableHTML += '<tr>';
        for (let j=0; j<5; j++){
            tableHTML += '<td>'+data[i][j]+'</td>';
        }
        tableHTML += '</tr>';
    }
    tableHTML += '</table>';

    document.body.innerHTML += tableHTML;
}

function searchBooks2(){
    const bookKey = document.getElementById('bookKey').value;
    const data = {
        bookKey: bookKey,
    };

    fetch('http://127.0.0.1:5000/searchBooks', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData.message);
        alert(responseData.message); // Example: Display a message from the backend
        prcesssSearchBooks(responseData.message);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
}


function issueBooks2(){
    const sid = document.getElementById('sid').value;
    const isbn = document.getElementById('isbn').value;
    const data = {
        sid: sid,
        isbn: isbn,
    };

    fetch('http://127.0.0.1:5000/issueBooks', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData.message);
        alert(responseData.message); // Example: Display a message from the backend
        if (responseData.message == -1)
        alert("cannot add more books");
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
}


function addMember2(){
    const sid = document.getElementById('sid').value;
    const data = {
        sid: sid,
    };

    fetch('http://127.0.0.1:5000/addMember', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData.message);
        alert(responseData.message); // Example: Display a message from the backend
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
}