from django.http import HttpResponse


#PUTTING UP LOGIN PART AND REGISTRATION PART


#SIMPLE URL TO REDIRECT TO FORMS
def index(request):
    html = "<center><h1>ROAD ACCIDENT RECORDING FORM A1</h1></center><br>"
    html += "<a href='forms'>CONTINUE TO FILL FORM</a>"
    return HttpResponse(html)