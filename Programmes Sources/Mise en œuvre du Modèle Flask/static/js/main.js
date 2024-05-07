document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get input values
    const formData = {
        child_mort: parseFloat(document.getElementById('child_mort').value),
        exports: parseFloat(document.getElementById('exports').value),
        health: parseFloat(document.getElementById('health').value),
        imports: parseFloat(document.getElementById('imports').value),
        income: parseFloat(document.getElementById('income').value),
        inflation: parseFloat(document.getElementById('inflation').value),
        life_expec: parseFloat(document.getElementById('life_expec').value),
        total_fer: parseFloat(document.getElementById('total_fer').value),
        gdpp: parseFloat(document.getElementById('gdpp').value)
    };

    // Send data to backend for prediction
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: formData })
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        document.getElementById('prediction-result').innerText = 'Prediction: ' + data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('prediction-result').innerText = 'Error: Failed to get prediction';
    });
});