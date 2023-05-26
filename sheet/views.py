from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Sheet
from json import loads

def index(request):
	sheets = Sheet.objects.all()
	return JsonResponse([sheet.to_dict() for sheet in sheets], safe=False, status=200)

@csrf_exempt
def crud(request):
	if request.method == 'GET':
		return read(request)
	elif request.method == 'POST':
		return create(request)
	elif request.method == 'PUT':
		return update(request)
	elif request.method == 'DELETE':
		return delete(request)
	else:
		return JsonResponse({'error': 'method not supported'})

def read(request):
	params = request.GET
	if 'id' in params:
		sheet = Sheet.objects.get(id=params['id'])
		return JsonResponse(sheet.to_dict(), safe=False, status=200)
	else:
		return JsonResponse({'error': 'id not found'}, status=400)

def create(request):
	body = loads(request.body)
	sheet = Sheet()
	sheet.make(body)
	sheet.save()
	return JsonResponse(sheet.to_dict(), safe=False, status=201)

def update(request):
	body = loads(request.body)
	sheet = Sheet.objects.get(id=body['id'])
	sheet.make(body)
	sheet.save()
	return JsonResponse(sheet.to_dict(), safe=False, status=200)

def delete(request):
	body = loads(request.body)
	sheet = Sheet.objects.get(id=body['id'])
	sheet.delete()
	return JsonResponse(sheet.to_dict(), safe=False, status=200)