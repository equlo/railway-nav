document.addEventListener('DOMContentLoaded', () => {
    // Setup the 3D Scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('map-container').appendChild(renderer.domElement);

    // Create a simple box geometry as a placeholder for the station map
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    const animate = () => {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    };

    animate();

    // Function to fetch the shortest path from backend API
    const fetchShortestPath = async () => {
        const response = await fetch('/api/shortest_path/start_id/end_id/');
        const data = await response.json();
        console.log(data);  // Display the path or update the map with the path data
    };

    // Function to fetch text-to-speech from backend API
    const fetchTextToSpeech = async () => {
        const response = await fetch('/api/text_to_speech/');
        const blob = await response.blob();
        const audioUrl = URL.createObjectURL(blob);
        const audio = new Audio(audioUrl);
        audio.play();
    };

    // Event Listeners for Buttons
    document.getElementById('find-path-btn').addEventListener('click', fetchShortestPath);
    document.getElementById('text-to-speech-btn').addEventListener('click', fetchTextToSpeech);
});
