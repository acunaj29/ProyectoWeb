from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="post":
        formulario_contacto=formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.post.get("nombre")
            email=request.post.get("email")
            contenido=request.post.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
                               "El usuario con nombre {} con direccion {} escribe: \n\n {}".format(nombre,email,contenido),
                               "",["joseacuna2010gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html",{"miformulario":formulario_contacto})