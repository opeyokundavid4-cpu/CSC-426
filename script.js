const form = document.getElementById("loginForm");

form.addEventListener("submit", function(e){

    e.preventDefault();

    const username =
    document.getElementById("username").value.trim();

    const password =
    document.getElementById("password").value.trim();

    const message =
    document.getElementById("message");

    if(username === "" || password === ""){
        message.textContent =
        "Please fill in all fields.";
        message.style.color = "red";
        return;
    }

    if(password.length < 6){
        message.textContent =
        "Password must be at least 6 characters.";
        message.style.color = "red";
        return;
    }

    if(username === "admin" &&
       password === "admin123"){
        message.textContent =
        "Login Successful!";
        message.style.color = "green";
    }
    else{
        message.textContent =
        "Invalid Username or Password.";
        message.style.color = "red";
    }

});