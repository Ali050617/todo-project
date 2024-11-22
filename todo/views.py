from django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
    <h1>Yangi vazifa yaratish</h1>
    
    <br>
    
    <form>
        <label for="Vazifa nomi>
        Vazifa nomi:
        <input type="text"/>
        </label>
    
    </form>
    
    """
    return HttpResponse(task_create())