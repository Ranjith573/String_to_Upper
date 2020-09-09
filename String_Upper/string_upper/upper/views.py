from django.shortcuts import render

# Create your views here.
def home(request):
    #nam = request.GET['name']
    return render(request,"home.html")

def upcase(request):
    
    st = request.POST['text1']
    st = st.upper()
    return render(request, "home.html",{'res':st})
    