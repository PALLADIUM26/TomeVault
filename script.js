function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    processLogin(username, password);
}

function processLogin(username, password){
    console.log("username:", username);
    console.log("password:", password);
}

function register() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;

    if(password1 == password2) {
        processRegister(username, email, password1);     
    } else {
        alert("Passwords not matching");
    }
}

function processRegister(username, email, password1){
    console.log("username:", username);
    console.log("email:", email);
    console.log("password:", password1);
}
