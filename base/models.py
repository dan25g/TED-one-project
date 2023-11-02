from django.db import models


class Lugar(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_nombre = models.CharField(max_length=50)
    l_tipo = models.CharField(max_length=50)
    l_cod_postal = models.IntegerField(blank=True, null=True)
    fk_lugar = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugar'

class Sucursal(models.Model):
    sucid = models.AutoField(primary_key=True)
    horaapertura = models.TimeField()
    horacierre = models.TimeField(blank=True, null=True)
    extension = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ubicacion = models.ForeignKey(Lugar, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Caja(models.Model):
    cajid = models.AutoField(primary_key=True)
    cajanumero = models.IntegerField()
    sucur = models.ForeignKey(Sucursal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'caja'

class Empleado(models.Model):
    empid = models.AutoField(primary_key=True)
    empci = models.BigIntegerField(unique=True)
    empnom = models.CharField()
    empape = models.CharField()
    fechaingreso = models.DateField()
    fechanacimiento = models.DateField()
    sueldo = models.DecimalField(max_digits=12, decimal_places=2)
    puesto = models.CharField()
    empsexo = models.CharField()
    fechasalida = models.DateField(blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    bono = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'empleado'

class Cliente(models.Model):
    clid = models.AutoField(primary_key=True)
    clci = models.BigIntegerField(unique=True)
    clpnom = models.CharField()
    clape = models.CharField()
    clfechanacimiento = models.DateField()
    clsexo = models.CharField()
    cltelefono = models.BigIntegerField()
    afiliado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Proveedor(models.Model):
    prid = models.AutoField(primary_key=True)
    prrif = models.BigIntegerField(unique=True)
    nombre = models.CharField()
    sede = models.ForeignKey(Lugar, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'

class Producto(models.Model):
    idprod = models.AutoField(primary_key=True)
    nombre = models.CharField()
    marca = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)
    presentacion = models.CharField()
    seccion = models.CharField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    precioventa = models.DecimalField(max_digits=10, decimal_places=2)
    costoind = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'producto'

class Oferta(models.Model):
    ofid = models.AutoField(primary_key=True)
    prof = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oferta'

class Compra(models.Model):
    comid = models.AutoField(primary_key=True)
    fechacom = models.DateTimeField(blank=True, null=True)
    cli = models.ForeignKey(Cliente, models.DO_NOTHING)
    cajero = models.ForeignKey(Empleado, models.DO_NOTHING)
    caja = models.ForeignKey(Caja, models.DO_NOTHING)
    ofer = models.ForeignKey(Oferta, models.DO_NOTHING)
    igtf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra'

class Prodcompra(models.Model):
    pcid = models.AutoField(primary_key=True)
    cantcom = models.IntegerField()
    prod = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)
    comp = models.ForeignKey(Compra, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prodcompra'

class Devolucion(models.Model):
    devid = models.AutoField(primary_key=True)
    razondev = models.CharField(blank=True, null=True)
    fecdev = models.DateField()
    prcmp = models.ForeignKey(Prodcompra, models.DO_NOTHING, db_column='prcmp', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devolucion'

class Falta(models.Model):
    faltaid = models.AutoField(primary_key=True)
    fechafalta = models.DateField()
    causa = models.CharField()
    emp = models.ForeignKey(Empleado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'falta'

class Pago(models.Model):
    pago_id = models.AutoField(primary_key=True)
    formapago = models.CharField(blank=True, null=True)
    pago_monto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fk_compra = models.ForeignKey(Compra, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pago'


class Stockalmacen(models.Model):
    stalid = models.AutoField(primary_key=True)
    prod = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)
    fechavencido = models.DateField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stockalmacen'


class Stocktienda(models.Model):
    sttid = models.AutoField(primary_key=True)
    prod = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)
    fechavencido = models.DateField()
    cantidad = models.IntegerField()
    sucur = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stocktienda'


class Gastos(models.Model):
    gasid = models.AutoField(primary_key=True)
    suc = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    alquiler = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    servicioagua = models.DecimalField(max_digits=10, decimal_places=2)
    servicioluz = models.DecimalField(max_digits=10, decimal_places=2)
    suministrolim = models.DecimalField(max_digits=10, decimal_places=2)
    mantenimientoelec = models.DecimalField(max_digits=10, decimal_places=2)
    gastomulta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gastos'

class Pedidoprooveedor(models.Model):
    pedid = models.AutoField(primary_key=True)
    prov = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)
    prd = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)
    costobr = models.DecimalField(max_digits=10, decimal_places=2)
    flete = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    igtf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidoprooveedor'