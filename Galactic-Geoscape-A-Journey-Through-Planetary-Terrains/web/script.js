// JavaScript code to handle interactive elements on the Galactic Geoscape webpage

// Data representing the planetary information (mirrors data from the CSV file)
const planetaryData = {
    Mars: {
        composition: "Iron Oxide and Basalt",
        averageTemperature: "-63°C",
        gravity: "3.71 m/s²",
        atmosphere: "Thin CO2"
    },
    Europa: {
        composition: "Water Ice and Rock",
        averageTemperature: "-160°C",
        gravity: "1.31 m/s²",
        atmosphere: "Oxygen Presence"
    },
    Moon: {
        composition: "Sodium and Potassium",
        averageTemperature: "-53 to 127°C",
        gravity: "1.62 m/s²",
        atmosphere: "None"
    }
};

// Function to display the selected planet's data on the page
function displayPlanetInfo(planet) {
    const planetInfo = planetaryData[planet];

    if (planetInfo) {
        document.getElementById('planet-composition').innerText = `Composition: ${planetInfo.composition}`;
        document.getElementById('planet-temperature').innerText = `Average Temperature: ${planetInfo.averageTemperature}`;
        document.getElementById('planet-gravity').innerText = `Gravity: ${planetInfo.gravity}`;
        document.getElementById('planet-atmosphere').innerText = `Atmosphere: ${planetInfo.atmosphere}`;
    }
}

// Event listener for planet selection dropdown menu
document.getElementById('planet-select').addEventListener('change', function () {
    const selectedPlanet = this.value;
    displayPlanetInfo(selectedPlanet);
});

// Initialize page with the default planet's data
window.onload = function () {
    displayPlanetInfo('Mars');  // Default to displaying Mars info on page load
};
