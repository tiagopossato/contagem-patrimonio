from django.shortcuts import render
from app.tables import InventarioTable

def inventario(request):
    invent = InventarioTable()
    return render(request, "index.html", {'Inventario': invent})