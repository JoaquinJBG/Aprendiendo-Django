from django.shortcuts import render



def simple (request):
    return render(request, 'simple.html') # renderizamos la plantilla simple.html y la devolvemos como respuesta a la solicitud HTTP

def dinamico (request, name):
    
    categorias = ['Python', 'Django', 'JavaScript', 'HTML', 'CSS'] # creamos una lista de categorías para pasar a la plantilla
    
    context = {'name': name, 'categories': categorias} # creamos un diccionario con el valor de name y la lista de categorías para pasarlo a la plantilla
    return render(request, 'dinamico.html', context) # renderizamos la plantilla dinamico.html y le pasamos el diccionario context para que pueda ser utilizado en la plantilla
