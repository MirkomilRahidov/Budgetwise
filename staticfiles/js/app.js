document.addEventListener("DOMContentLoaded", function () {
    const h1 = document.createElement("h1");
    h1.innerText = gettext("Welcome to BudgetWise");
    document.querySelector(".container").prepend(h1);
});
