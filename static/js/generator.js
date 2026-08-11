const passwordInput =
document.getElementById("generatedPassword");

const generateButton =
document.getElementById("generateButton");

const copyButton =
document.getElementById("copyButton");

const lengthSlider =
document.getElementById("length");

const lengthValue =
document.getElementById("lengthValue");

const strengthBar =
document.getElementById("strengthBar");

const strengthText =
document.getElementById("strengthText");

const copyMessage =
document.getElementById("copyMessage");

const uppercase =
document.getElementById("uppercase");

const lowercase =
document.getElementById("lowercase");

const numbers =
document.getElementById("numbers");

const symbols =
document.getElementById("symbols");

/* CHARACTER SETS */

const upperChars =
"ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const lowerChars =
"abcdefghijklmnopqrstuvwxyz";

const numberChars =
"0123456789";

const symbolChars =
"!@#$%^&*()_+-=[]{}|;:,.<>?";

/* RANDOM CHARACTER */

function randomCharacter(characters) {


return characters[
    Math.floor(
        Math.random() * characters.length
    )
];


}

/* SHUFFLE */

function shufflePassword(password) {


return password
    .split("")
    .sort(() => Math.random() - 0.5)
    .join("");


}

/* GENERATE PASSWORD */

function generatePassword() {


const length =
    parseInt(lengthSlider.value);


let characters = "";

let password = "";


if (uppercase.checked) {

    characters += upperChars;

    password += randomCharacter(
        upperChars
    );

}


if (lowercase.checked) {

    characters += lowerChars;

    password += randomCharacter(
        lowerChars
    );

}


if (numbers.checked) {

    characters += numberChars;

    password += randomCharacter(
        numberChars
    );

}


if (symbols.checked) {

    characters += symbolChars;

    password += randomCharacter(
        symbolChars
    );

}


if (!characters) {

    alert(
        "Please select at least one character type."
    );

    return;

}


while (password.length < length) {

    password += randomCharacter(
        characters
    );

}


password =
    shufflePassword(password);


passwordInput.value =
    password;


updateStrength(password);


}

/* STRENGTH */

function updateStrength(password) {


let score = 0;


if (password.length >= 8) {
    score++;
}

if (password.length >= 12) {
    score++;
}

if (/[A-Z]/.test(password)) {
    score++;
}

if (/[a-z]/.test(password)) {
    score++;
}

if (/[0-9]/.test(password)) {
    score++;
}

if (/[^A-Za-z0-9]/.test(password)) {
    score++;
}


let percentage =
    (score / 6) * 100;


strengthBar.style.width =
    percentage + "%";


if (score <= 2) {

    strengthText.textContent =
        "Weak";

    strengthText.className =
        "weak";

}

else if (score <= 4) {

    strengthText.textContent =
        "Good";

    strengthText.className =
        "good";

}

else {

    strengthText.textContent =
        "Excellent";

    strengthText.className =
        "excellent";

}


}

/* LENGTH */

lengthSlider.addEventListener(
"input",
function () {


    lengthValue.textContent =
        this.value;

}


);

/* GENERATE BUTTON */

generateButton.addEventListener(
"click",
generatePassword
);

/* COPY */

copyButton.addEventListener(
"click",
async function () {


    if (!passwordInput.value) {

        return;

    }


    try {

        await navigator.clipboard.writeText(
            passwordInput.value
        );

        copyMessage.textContent =
            "✓ Password copied!";

    }

    catch {

        passwordInput.select();

        document.execCommand("copy");

        copyMessage.textContent =
            "✓ Password copied!";

    }


    setTimeout(
        () => {
            copyMessage.textContent = "";
        },
        2000
    );

}


);

/* GENERATE INITIAL PASSWORD */

generatePassword();
