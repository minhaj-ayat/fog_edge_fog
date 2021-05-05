from django.shortcuts import render
from UE.ue import authenticated


# Create your views here.
def oidc_login(request):
    print("Auth :: " + str(authenticated))
    args = {'auth': authenticated}
    return render(request, 'rp.html', args)


def foreignfog_home_view(request):
    return render(request, 'foreignfog_home.html')
