const og_otp = 54321;

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    processLogin(username, password);
}

function processLogin(username, password1){
    console.log("username:", username);
    console.log("password:", password1);
    const data = {
        username: username,
        password1: password1,
    };
    fetch('http://127.0.0.1:5000/login', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData);
        // Handle the response from the Python backend (e.g., display a message)
        alert(responseData.message); // Example: Display a message from the backend
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
    location.href = "homeAdmin.html";
    // location.replace("verify.html?"+email);
}


function register() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;
    var category;
    
    if(document.getElementById('s').checked)
        category = document.getElementById('s').value;
    else if(document.getElementById('l').checked)
        category = document.getElementById('l').value;
    else if(document.getElementById('a').checked)
        category = document.getElementById('a').value;

    window.onload = function(){
        const email = document.getElementById("email").value;
        localStorage.setItem("email",email);
    }
    if(password1 == password2) {
        processRegister(username, email, password1, category);
    } else {
        alert("Passwords not matching");
    }
}


function processRegister(username, email, password1, category){
    console.log("username:", username);
    console.log("email:", email);
    console.log("password:", password1);
    console.log("category:", category);
    // var og_otp = 54321;
    // sendEmail();
    
    const data = {
        username: username,
        email: email,
        password1: password1,
        og_otp: og_otp,
        category: category,
    };
    fetch('http://127.0.0.1:5000/register', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData);
        // Handle the response from the Python backend (e.g., display a message)
        alert(responseData.message); // Example: Display a message from the backend
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
    // location.href = "verify.html";
    location.replace("verify.html?"+email);
}


function verify(){
    // const og_otp = 54321;
    var link = window.location.href;
    link = link.replace("verify.html?","");
    // document.write(link);
    arr = link.split("/");
    email = arr[arr.length-1];
    
    const otp = document.getElementById('otp').value;
    if (og_otp == otp) {
        alert("Verified");
        processVerify(email);
        location.href = "login.html";
    } else {
        alert("Wrong OTP");
    }
}

function processVerify(email){
    console.log("email:", email);
    const data = {
        email: email,
    };

    fetch('http://127.0.0.1:5000/verify', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData);
        // Handle the response from the Python backend (e.g., display a message)
        alert(responseData.message); // Example: Display a message from the backend
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
}
