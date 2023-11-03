from django.shortcuts import render
from psycopg2 import *
from report.report import report

def Home(request):
    return render(request, 'home.html')

def exportRp1(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte1();")

    productos_list= []
    for producto, ventas, proveedor in cur.fetchall():# data={nombre:tipo}
        productos_list.append({
            'producto': producto,
            'ventas': ventas,
            'proveedor': proveedor
        })

        
        if productos_list.count==0:{ #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            productos_list.append({
            'producto': 'none',
            'ventas': 0,
            'proveedor': 'none'
            
        })
        }
        
            
        data={
        'productos': productos_list
            }

    return report(request, 'rp1', data)

def exportRp2(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte2();")

    empleados_list= []
    for nombre, apellido, faltas in cur.fetchall():# data={nombre:tipo}
        empleados_list.append({
            'nombre': nombre,
            'apellido': apellido,
            'faltas': faltas
        })
        
       # for personajes in personajes_list: 
        data1={ 
      #      personajes:personajes
        'empleados': empleados_list
            }
        #    
    #for i in data.items():print(i)

    return report(request, 'rp2', data1)

def exportRp3(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte3();")

    sucursal_list= []
    for sucursal, sitio, ingresos, gastos, ganancias in cur.fetchall():# data={nombre:tipo}
        sucursal_list.append({
            'sucursal': sucursal,
            'sitio': sitio,
            'ingresos': ingresos,
            'gastos': gastos,
            'ganancias': ganancias
        })
        
       # for personajes in personajes_list: 
        data2={ 
      #      personajes:personajes
        'sucursales': sucursal_list
            }
        #    
    #for i in data.items():print(i)

    return report(request, 'rp3', data2)

def exportRp4(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte4();")

    empleados_list= []
    for nombre, apellido, sucursal, ventas in cur.fetchall():# data={nombre:tipo}
        empleados_list.append({
            'nombre': nombre,
            'apellido':apellido,
            'sucursal': sucursal,
            'ventas': ventas
        })
        
       # for personajes in personajes_list: 
        data3={ 
      #      personajes:personajes
        'empleados': empleados_list
            }
        #    
    #for i in data.items():print(i)

    return report(request, 'rp4', data3)

def exportRp5(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte5();")

    productos_list= []
    for fecha, producto, presentacion, razon in cur.fetchall():# data={nombre:tipo}
        productos_list.append({
            'fecha': fecha,
            'producto':producto,
            'presentacion': presentacion,
            'razon': razon
        })
        
       # for personajes in personajes_list: 
        data3={ 
      #      personajes:personajes
        'productos': productos_list
            }
        #    
    #for i in data.items():print(i)

    return report(request, 'rp5', data3)

def exportRp6(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte6();")

    productos_list= []
    for producto, descuento, ventas in cur.fetchall():# data={nombre:tipo}
        productos_list.append({
            'producto': producto,
            'descuento':descuento,
            'ventas': ventas
        })
        
       # for personajes in personajes_list: 
        data3={ 
      #      personajes:personajes
        'productos': productos_list
            }
        #    
    #for i in data.items():print(i)

    return report(request, 'rp6', data3)

def exportRp7(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte7();")

    productos_list= []
    for nombre, presentacion, precio, vencidmiento, unidades in cur.fetchall():# data={nombre:tipo}
        productos_list.append({
            'nombre': nombre,
            'presentacion':presentacion,
            'precio': precio,
            'vencidmiento': vencidmiento,
            'unidades': unidades
        })
        
       # for personajes in personajes_list: 
        data3={ 
      #      personajes:personajes
        'productos': productos_list
            }
        #    
    #for i in data.items():print(i)

    return report(request, 'rp7', data3)

def exportRp8(request):
    conexion= connect(host="dpg-ckmtifav7m0s738q5vd0-a.oregon-postgres.render.com",database="tedmarket",user="tedmarket_user",password="rw5XqeMYfA4lAQc93kt7CctaKiZaAwd1")
    cur=conexion.cursor()

    cur.execute("select * from reporte8();")

    productos_list= []
    for producto,acompa, ventas in cur.fetchall():# data={nombre:tipo}
        productos_list.append({
            'producto': producto,
            'acompa':acompa,
            'ventas': ventas
        })
        
       # for personajes in personajes_list: 
        data3={ 
      #      personajes:personajes
        'productos': productos_list
            }
        #    
    #for i in data.items():print(i)

    return report(request, 'rp8', data3)

