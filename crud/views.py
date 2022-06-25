from django.shortcuts import render
from django.views import View
from django.contrib import auth
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView , DetailView , ListView , DeleteView , UpdateView
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseForbidden
from .models import todo
from django.urls import reverse_lazy


#this view is use for submiting signup 
def submit(request):
    if request.method == 'POST':
        
        if request.POST['password1'] == request.POST['password2']: 
            try: 

                user = User.objects.get(username=request.POST['username']) 


                return render(request, 'crud/signup.html', {'error':'Username has already been taken!'})
            except User.DoesNotExist: 

                user = User.objects.create_user(request.POST['username'], request.POST['email'] ,    request.POST['password1'])
                auth.login(request,user)
                return render(request,'crud/dist/index.html', )
                
                
 
        else: # if password 1 and  password2 don't be same :
        	alerts = 'samba' 
        	contex = {'alert' : alerts }
        	return render(request,'templates/crud/signup.html', contex)
    else:
        return redirect('http://127.0.0.1:8000/accounts/login')




#this view is use for create our checklist
def createtodo(request):
	checklistes = request.POST.getlist("checklist")[0]
	sprintes =  request.POST.getlist("sprint")[0]
	apps = todo()
	apps.checklist = checklistes
	apps.sprint = sprintes
	apps.user = request.user
	apps.save()
	return redirect('http://127.0.0.1:8000/home')
		

#in this view client can see lists of his/her checklists
class useri(ListView):
	template_name = 'crud/dist/index.html'
	context_object_name = "todo"
	def get_queryset( self,**kwargs):
		if not self.request.user.is_authenticated:
			return HttpResponseForbidden()
		hold = todo()
		pl = self.request.user
		send = todo.objects.filter(user=pl )
		return send

	#def get_context_data(request,self,**kwargs):
		#context = super().get_context_data(**kwargs)
		#context["todo"] = todo.objects.all()
		#return context
			

#delete check list
class deletetodo(DeleteView):
	model = todo
	success_url = reverse_lazy('crud:home')
	template_name = "crud/delete.html"


#update checklist	
class updatetodo(UpdateView):
	model = todo
	success_url = reverse_lazy('crud:home')
	template_name = "crud/update.html"
	fields = ['checklist','sprint']
	
	




#login
class login(View):
	def dispatch(self , request , *args , **kwargs):
		if request.method == "GET":
			return self.login(request ,  *args , **kwargs )
	def login(self , request):
		follow = True		
		return redirect('http://127.0.0.1:8000/accounts/login/')




#log out
def logout(request):
    return redirect('http://127.0.0.1:8000/accounts/logout/')


# signup
def signup(request):
    return render(request, 'crud/signup.html')
    






# Create your views here.
