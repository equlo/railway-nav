from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Location, Path
from .utils import dijkstra
from gtts import gTTS
import os

def index(request):
    return render(request, 'index.html')

def get_shortest_path(request, start_id, end_id):
    try:
        start_location = Location.objects.get(id=start_id)
        end_location = Location.objects.get(id=end_id)
    except Location.DoesNotExist:
        return JsonResponse({'error': 'Location not found'}, status=404)

    # Create a graph representation from locations and paths
    graph = {}
    for location in Location.objects.all():
        graph[location.id] = []
        paths = Path.objects.filter(start_location=location)
        for path in paths:
            graph[location.id].append((path.end_location.id, path.distance))

    path, distance = dijkstra(graph, start_location.id, end_location.id)

    # Convert path ids to location names
    path_locations = [Location.objects.get(id=loc_id).name for loc_id in path]

    response_data = {
        'path': path_locations,
        'distance': distance,
    }

    return JsonResponse(response_data)

def text_to_speech(request):
    text = request.GET.get('text', "This is a default text for text-to-speech.")
    tts = gTTS(text=text, lang='en')
    audio_path = os.path.join("media", "audio.mp3")
    tts.save(audio_path)

    # Return the audio file
    with open(audio_path, "rb") as f:
        response = HttpResponse(f.read(), content_type="audio/mpeg")
        response['Content-Disposition'] = 'inline; filename=audio.mp3'
        return response
