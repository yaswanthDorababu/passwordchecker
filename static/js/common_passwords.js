const passwordInput =
    document.getElementById("commonPassword");

const togglePassword =
    document.getElementById("togglePassword");


togglePassword.addEventListener("click", function () {

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

        togglePassword.textContent = "🙈";

    } else {

        passwordInput.type = "password";

        togglePassword.textContent = "👁️";

    }

});