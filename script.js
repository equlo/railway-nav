// Initialize the map
const map = L.map('map').setView([22.5726, 88.3639], 15); // Centering on Howrah Station

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Real-time data - replace with actual coordinates
const markers = {
    'Ticket Counter': L.marker([22.5729, 88.3637]).bindPopup('Ticket Counter'),
    'Platform 1': L.marker([22.5732, 88.3640]).bindPopup('Platform 1'),
    'Platform 2': L.marker([22.5735, 88.3643]).bindPopup('Platform 2'),
    'Restroom': L.marker([22.5730, 88.3646]).bindPopup('Restroom'),
    'Food Court': L.marker([22.5727, 88.3642]).bindPopup('Food Court')
};

// Add markers to the map
for (const key in markers) {
    markers[key].addTo(map);
}

function findPath() {
    const start = document.getElementById('start').value;
    const end = document.getElementById('end').value;

    fetch('http://127.0.0.1:5001/shortest-path', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ start: start, end: end })
    })
    .then(response => response.json())
    .then(data => {
        const path = data.path;
        const distance = data.distance;
        displayPath(path);
        document.getElementById('path').innerText = `Distance: ${distance} meters`;
    })
    .catch(error => console.error('Error:', error));
}

function displayPath(path) {
    // Clear previous path
    map.eachLayer(layer => {
        if (layer instanceof L.Polyline) {
            map.removeLayer(layer);
        }
    });

    const latlngs = path.map(location => {
        return markers[location] ? markers[location].getLatLng() : null;
    }).filter(latlng => latlng !== null);

    if (latlngs.length > 1) {
        const polyline = L.polyline(latlngs, { color: 'blue' }).addTo(map);
        map.fitBounds(polyline.getBounds());
    }
}
