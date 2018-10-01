from django.http import HttpResponse
from django.core import serializers
from .models import Enquire


def index(request):
    latest_question_list = Enquire.objects.order_by('-pub_date')[:5]
    data = serializers.serialize("json", Enquire.objects.all())
    return HttpResponse(data)