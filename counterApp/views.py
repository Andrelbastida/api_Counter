from django.http import JsonResponse

def get_sensor_data(request):
    data = {
        "Sensor": SensorData.objects.first().sensor,
        "Botao": SensorData.objects.first().botao,
        "LigaRobo": SensorData.objects.first().liga_robo,
        "ResetContador": SensorData.objects.first().reset_contador,
        "Valor Contagem": SensorData.objects.first().valor_contagem,
    }
    return JsonResponse(data)

