# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from carro.carro import Carro
# #from flask import redirect
# from django.contrib import messages
# from pedidos.models import LineaPedido, Pedido
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags


# @login_required(login_url="/autenticacion/logear")
# def procesar_pedido(request):
#     pedido=Pedido.objects.create(user=request.user)
#     carro=Carro(request)
#     lineas_pedido=list()

#     for key,value in carro.carro.items():
#         lineas_pedido.append(LineaPedido(
#             producto_id=key,
#             cantidad=value["cantidad"],
#             user=request.user,
#             pedido=pedido
#         ))

#     LineaPedido.objects.bulk_create(lineas_pedido)

#     enviar.mail(
#         pedido=pedido,
#         lineas_pedido=lineas_pedido,
#         nombreusuario=request.username,
#         emailusuario=request.usermail
#     )

#     messages.success(request, "El pedido se ha creado.")

#     return redirect("../tienda")

# # def enviar_mail(**kwargs):
#     asunto = "Gracias por el pedido"
#     mensaje = render_to_string("emails/pedido.html",{
#         "pedido": kwargs.get("pedido"),
#         "lineas_pedido": kwargs.get("lineas_pedido"),
#         "nombreusuario":kwargs.get("nombreusuario")
#     })

    # mensaje_texto=strip_tags(mensaje)
    # from_email="joseacuna2010@gmail.com"
    # to=kwargs.get("emailusuario")

    # send.mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)

    # Cuna de madera 3 en 1 con cambiador y cajonera, colo cafe. precio $350