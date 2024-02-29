const burgerNav = document.querySelector(".burger")
const links = document.querySelector(".links")


burgerNav.addEventListener("click", () => {
    links.classList.toggle("hidden")
});
