from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.

def home(request):
    productos = Productos.objects.all()
    return render(request, "GestionProductos.html", {"productos":productos})

def registrarProductos(request):
     if request.method == "POST":    
        codigo = request.POST['txtCodigo']
        descripcion = request.POST['txtDescripcion']
        marca = request.POST['txtMarca']
        lote = request.POST['txtLote']
        fecha_vencimiento = request.POST['txtFechaVencimiento']
        precio_lista = request.POST['txtPrecioLista']
        stock_disponible = request.POST['txtStock']
        unidad_medida = request.POST['txtUnidadMedida']
        requiere_receta = True if request.POST.get('chkReceta') == 'on' else False
        observaciones = request.POST.get('txtObservaciones', '')

        Productos.objects.create(
            codigo=codigo,
            descripcion=descripcion,
            marca=marca,
            lote=lote,
            fecha_vencimiento=fecha_vencimiento,
            precio_lista=precio_lista,
            stock_disponible=stock_disponible,
            unidad_medida=unidad_medida,
            requiere_receta=requiere_receta,
            observaciones=observaciones
        )
        return redirect('/') 

def edicionProductos(request,codigo):
    productos = Productos.objects.get(codigo=codigo)
    return render(request, "edicionProductos.html",{"productos":productos})

def editarProductos(request):
 if request.method == "POST":
        codigo = request.POST['txtCodigo']
        descripcion = request.POST['txtDescripcion']
        marca = request.POST['txtMarca']
        lote = request.POST['txtLote']
        fecha_vencimiento = request.POST['txtFechaVencimiento']
        precio_lista = request.POST['txtPrecioLista']
        stock_disponible = request.POST['txtStock']
        unidad_medida = request.POST['txtUnidadMedida']
        requiere_receta = True if request.POST.get('chkReceta') == 'on' else False
        observaciones = request.POST.get('txtObservaciones', '')
     
        producto = Productos.objects.get(codigo=codigo)
        producto.codigo = codigo
        producto.descripcion = descripcion
        producto.marca = marca
        producto.lote = lote
        producto.fecha_vencimiento = fecha_vencimiento
        producto.precio_lista = precio_lista
        producto.stock_disponible = stock_disponible
        producto.unidad_medida = unidad_medida
        producto.requiere_receta = requiere_receta
        producto.observaciones = observaciones
        producto.save()

        return redirect('/')


def eliminarProductos(request, codigo):
    productos = Productos.objects.get(codigo=codigo)
    productos.delete()
    return redirect('/') 