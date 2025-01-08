from core.models import Profile
from django.shortcuts import redirect

def navbar_data(request):
    if request.user.is_authenticated:
        data = Profile.objects.filter(user=request.user).first()
        return {'data': data}
    else:
        return {'data': None}