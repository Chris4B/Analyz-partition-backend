from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedFile

# Create your views here.
@csrf_exempt
def upload_file(request):
    """
    API endpoint to upload a file.

    Accepts:
        - POST request with a file in the "file" field.

    Returns:
        - JSON response with the file URL or an error message.
    """
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = UploadedFile(file=request.FILES['file'])
        uploaded_file.save()
        return JsonResponse({'message': 'File uploaded successfully!', 'file_url': uploaded_file.file.url})

    return JsonResponse({'error': 'No file provided'}, status=400)