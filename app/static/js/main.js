const searchBox = document.getElementById("search-box");
const searchResults = document.getElementById("search-results");

searchBox.addEventListener("click", () => {     searchResults.classList.toggle("hidden");
});

document.addEventListener("click", (event) => {
     if (
          !searchBox.contains(event.target) &&
          !searchResults.contains(event.target)
     ) {
          searchResults.classList.add("hidden");
     }
});

const button = document.getElementById("sort-button");
const dropdown = document.getElementById("sort-option");

button.addEventListener("click", () => {
     dropdown.classList.toggle("hidden");
});

document.addEventListener("click", (event) => {
     const isClickInside =
          button.contains(event.target) || dropdown.contains(event.target);
     if (!isClickInside) {
          dropdown.classList.add("hidden");
     }
});
