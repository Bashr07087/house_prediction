async function predictPrice() {
    const data = {
        area: document.getElementById("area").value,
        bedrooms: document.getElementById("bedrooms").value,
        bathrooms: document.getElementById("bathrooms").value,
        stories: document.getElementById("stories").value,
        mainroad: document.getElementById("mainroad").value,
        guestroom: document.getElementById("guestroom").value,
        basement: document.getElementById("basement").value,
        hotwaterheating: document.getElementById("hotwaterheating").value,
        airconditioning: document.getElementById("airconditioning").value,
        parking: document.getElementById("parking").value,
        prefarea: document.getElementById("prefarea").value,
        furnishingstatus: document.getElementById("furnishingstatus").value
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText = `Predicted Price: $${result.predicted_price}`;

}