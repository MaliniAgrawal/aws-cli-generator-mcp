document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.getElementById("nlpInput");
    const generateBtn = document.getElementById("generateBtn");
    const clearBtn = document.getElementById("clearBtn");
    const themeToggle = document.getElementById("themeToggle");
    const resultBox = document.getElementById("result");
    const copyBtn = document.getElementById("copyBtn");

    async function generateCommand() {
        const nlpInput = inputField.value.trim();
        if (!nlpInput) {
            resultBox.innerText = "Please enter a request.";
            return;
        }

        try {
            const response = await fetch("/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ input: nlpInput })
            });

            const data = await response.json();
            resultBox.innerText = `✅ Generated Command:\n${data.command}\n\n💡 Explanation:\n${data.explanation}`;
        } catch (err) {
            resultBox.innerText = `❌ Error: ${err}`;
        }
    }

    // Clear button
    clearBtn.addEventListener("click", () => {
        inputField.value = "";
        resultBox.innerText = "";
    });

    // Theme toggle
    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("light");
    });

    generateBtn.addEventListener("click", generateCommand);

    // Copy Command button
    copyBtn.addEventListener("click", () => {
        // Extract the command from the resultBox text
        const match = resultBox.innerText.match(/Generated Command:\n([^\n]+)/);
        if (match && match[1]) {
            navigator.clipboard.writeText(match[1]);
        }
    });

    // Handle example clicks
    document.querySelectorAll(".example").forEach(btn => {
        btn.addEventListener("click", () => {
            inputField.value = btn.innerText;
            generateCommand();
        });
    });
});
