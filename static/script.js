document.getElementById("survey-form").addEventListener("submit", async (event) => {
    event.preventDefault();  // Prevents page reload

    const formData = {};
    for (let i = 1; i <= 10; i++) {
        formData[`question${i}`] = document.getElementById(`question${i}`).value;
    }

    const resultDiv = document.getElementById("result");

    try {
        const response = await fetch("/process", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        });

        const data = await response.json();
        resultDiv.innerHTML = Object.entries(data)
            .map(([question, answer]) => `<p>${question}: ${answer}</p>`)
            .join("");
    } catch (error) {
        resultDiv.textContent = "An error occurred.";
        console.error(error);
    }
});
