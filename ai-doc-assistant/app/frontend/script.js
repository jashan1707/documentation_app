document.getElementById("start-recording").addEventListener("click", async () => {
    alert("Recording user activity...");
});

document.getElementById("stop-recording").addEventListener("click", async () => {
    alert("Processing AI-generated documentation...");

    const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST"
    });
    const data = await response.json();
    document.getElementById("documentation").value = data.documentation;
});

document.getElementById("upload-doc").addEventListener("click", async () => {
    const title = document.getElementById("doc-title").value;
    const content = document.getElementById("documentation").value;

    if (!title || !content) {
        alert("Please enter a title and generate documentation first.");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content })
    });

    const result = await response.json();
    alert(result.message);
});