const password = document.getElementById("password");

const lower = document.getElementById("lower");
const upper = document.getElementById("upper");
const numbers = document.getElementById("numbers");
const special = document.getElementById("special");
const passlength = document.getElementById("passlength");

if (password) {

password.addEventListener("keyup", function () {

    const value = password.value;


    // Lowercase

    if (/[a-z]/.test(value)) {

        lower.classList.add("valid");
        lower.classList.remove("invalid");

    } else {

        lower.classList.add("invalid");
        lower.classList.remove("valid");

    }


    // Uppercase

    if (/[A-Z]/.test(value)) {

        upper.classList.add("valid");
        upper.classList.remove("invalid");

    } else {

        upper.classList.add("invalid");
        upper.classList.remove("valid");

    }


    // Number

    if (/[0-9]/.test(value)) {

        numbers.classList.add("valid");
        numbers.classList.remove("invalid");

    } else {

        numbers.classList.add("invalid");
        numbers.classList.remove("valid");

    }


    // Special character

    if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>/?]/.test(value)) {

        special.classList.add("valid");
        special.classList.remove("invalid");

    } else {

        special.classList.add("invalid");
        special.classList.remove("valid");

    }


    // Length

    if (value.length >= 8) {

        passlength.classList.add("valid");
        passlength.classList.remove("invalid");

    } else {

        passlength.classList.add("invalid");
        passlength.classList.remove("valid");

    }

});


}

const passwordInput = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");

if (passwordInput && togglePassword) {

    togglePassword.addEventListener("click", function () {

        // Change password visibility
        if (passwordInput.type === "password") {

            passwordInput.type = "text";

            this.setAttribute(
                "aria-label",
                "Hide password"
            );

        } else {

            passwordInput.type = "password";

            this.setAttribute(
                "aria-label",
                "Show password"
            );
        }

        // Restart animation
        this.classList.remove("animate");

        void this.offsetWidth;

        this.classList.add("animate");
    });
}
