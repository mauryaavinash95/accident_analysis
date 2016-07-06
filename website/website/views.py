from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

#PUTTING UP LOGIN PART AND REGISTRATION PART


#SIMPLE URL TO REDIRECT TO FORMS
def index(request):
    html = "<center><h1>ROAD ACCIDENT RECORDING FORM A1</h1></center><br>"
    html += "<a href='forms'>CONTINUE TO FILL FORM</a>"
    return HttpResponse(html)

@staff_member_required
def my_admin_view(request):
    if request.method == "POST":
        form = DataInput(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            context = {"form": form, "success": success}
            return render_to_response("imported.html", context,
            context_instance=RequestContext(request))
    else:
        form = DataInput()        
        context = {"form": form}
        return render_to_response("imported.html", context,
        context_instance=RequestContext(request)) 
