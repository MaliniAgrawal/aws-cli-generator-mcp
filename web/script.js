document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.getElementById("nlpInput");
    const generateBtn = document.getElementById("generateBtn");
    const resultBox = document.getElementById("result");
    const darkModeToggle = document.getElementById("darkModeToggle");

    const API_URL = "/mcp/generate-cli";

    function displayResult(command, explanation, isError = false) {
        resultBox.innerHTML = `
            <p><strong>CLI Command:</strong> <code>${command}</code></p>
            <p><strong>Explanation:</strong> ${explanation}</p>
        `;
        resultBox.className = `result-box ${isError ? "error" : "success"}`;
    }

    async function generateCommand() {
        const task = inputField.value.trim();
        if (!task) {
            displayResult("N/A", "Please enter a valid AWS task.", true);
            return;
        }

        try {
            const res = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ input: task })
            });

            const data = await res.json();
            if (!res.ok) {
                console.error("Error from API:", data.error || "Unknown error");
                displayResult("N/A", data.error || "Unknown error", true);
                return;
            }

            displayResult(data.command, data.explanation);
            inputField.value = ""; // Clear after success
        } catch (err) {
            console.error("Network error:", err);
            displayResult("N/A", "Network error occurred. Check console.", true);
        }
    }

    generateBtn.addEventListener("click", generateCommand);
    inputField.addEventListener("keypress", (e) => {
        if (e.key === "Enter") generateCommand();
    });

    // Dark mode toggle
    darkModeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
    });
});
