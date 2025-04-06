function showScreen(screenNumber) {
    let screens = document.querySelectorAll('.screen');
    screens.forEach(screen => screen.classList.remove('active'));

    const targetScreen = document.getElementById(`screen${screenNumber}`);
    targetScreen.classList.add('active');

    // Initialize slider value display if entering screen 3
    if (screenNumber === 3) {
        initSlider();
    }
}

async function submitForm() {
    const formData = {
        sex: document.querySelector('input[name="sex"]:checked')?.value,
        age: document.getElementById("age").value,
        height: document.getElementById("height").value,
        weight: document.getElementById("weight").value,
        strength_training: document.getElementById("strength_training").value,
        desired_drunkenness: document.getElementById("desired_drunkenness").value,
        wine_percentage: document.getElementById("wine_percentage").value,
        beer_percentage: document.getElementById("beer_percentage").value,
        other_percentage: document.getElementById("other_percentage").value
    };

    const resultDiv = document.getElementById("result");

    try {
        const response = await fetch("/process", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        });

        const data = await response.json();
        resultDiv.innerHTML = `<p>${data.message}</p>`;
    } catch (error) {
        resultDiv.textContent = "An error occurred.";
        console.error(error);
    }
}

function initSlider() {
    const slider = document.getElementById("myRange");
    const output = document.getElementById("demo");

    if (slider && output) {
        output.textContent = slider.value;
        slider.oninput = function () {
            output.textContent = this.value;
        };
    }
}