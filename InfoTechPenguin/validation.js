function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;
    var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

    if (name === "" || email === "" || message === "") {
        alert("All fields are required");
        return false;
    }

    if (!emailRegex.test(email)) {
        alert("Invalid email address");
        return false;
    }

    return true;
}
