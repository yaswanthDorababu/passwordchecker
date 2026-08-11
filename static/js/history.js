const searchInput =
document.getElementById("historySearch");

const strengthFilter =
document.getElementById("strengthFilter");

const clearButton =
document.getElementById("clearHistory");

const historyCard =
document.querySelector(".history-card");

const emptyState =
document.getElementById("emptyState");

function filterHistory() {


const searchValue =
    searchInput.value.toLowerCase();

const selectedStrength =
    strengthFilter.value;

const rows =
    document.querySelectorAll(".history-row");

let visibleRows = 0;


rows.forEach(function (row) {

    const text =
        row.textContent.toLowerCase();


    const badge =
        row.querySelector(".badge");


    const strength =
        badge
            ? badge.textContent.toLowerCase()
            : "";


    const matchesSearch =
        text.includes(searchValue);


    const matchesStrength =
        selectedStrength === "all" ||
        strength === selectedStrength;


    if (matchesSearch && matchesStrength) {

        row.style.display = "grid";

        visibleRows++;

    } else {

        row.style.display = "none";

    }

});


if (visibleRows === 0) {

    historyCard.style.display = "none";

    emptyState.style.display = "block";

} else {

    historyCard.style.display = "block";

    emptyState.style.display = "none";

}


}

if (searchInput) {


searchInput.addEventListener(
    "input",
    filterHistory
);


}

if (strengthFilter) {


strengthFilter.addEventListener(
    "change",
    filterHistory
);


}

if (clearButton) {


clearButton.addEventListener(
    "click",
    function () {

        const confirmed =
            confirm(
                "Are you sure you want to clear your password history?"
            );


        if (!confirmed) {
            return;
        }


        const rows =
            document.querySelectorAll(".history-row");


        rows.forEach(function (row) {

            row.style.display = "none";

        });


        historyCard.style.display = "none";

        emptyState.style.display = "block";

    }
);


}
