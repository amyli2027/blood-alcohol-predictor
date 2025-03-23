document.getElementById("user-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const userInput = document.getElementById("user-input").value;
    const resultDiv = document.getElementById("result");

    try {
        const response = await fetch("/process", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_input: userInput }),
        });
        const data = await response.json();
        resultDiv.textContent = data.output;
    } catch (error) {
        resultDiv.textContent = "An error occurred.";
        console.error(error);
    }
});
