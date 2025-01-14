document.getElementById("dropLabel").addEventListener("dragover", (event) => {
    event.preventDefault();
    event.target.style.backgroundColor = "#e6f2ff";
});

document.getElementById("dropLabel").addEventListener("dragleave", (event) => {
    event.target.style.backgroundColor = "#f0f8ff";
});
