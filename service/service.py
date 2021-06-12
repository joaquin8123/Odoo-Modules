# -*- coding: utf-8 -*- 
from odoo import models, fields 
# Modelo de los servicios
class Service(models.Model): 
    _name = 'service.service' 
    _description = 'Service'

    # Funcion que calcula el total del servicio.
    def btn_calcular_totales(self):
        self.total = 0
        for obj in self.services_ids:
            self.total += (obj.precio * obj.cantidad)
        return self

    #campos
    name = fields.Char('Nombre', required=True)
    patente = fields.Char('Patente', required=True)
    services_ids = fields.Many2many('service.type','service_service_tipo_rel' ,'service_id','type_id', 'Servicios')
    total = fields.Float(string='Total', size=16, digits=(16, 0))
    # state = fields.Selection([ ('draft', 'Borrador'),('progress','En Curso'),('done','Finalizado'),('cancel','Cancelado')],'Estado', default='draft')
    

# Modelo de los tipos de servicio
class ServiceType(models.Model): 
    _name = 'service.type' 
    _description = 'Types Service'

    #campos
    name = fields.Char('Nombre del Servicio', required=True)
    tipo = fields.Selection([ ('service', 'Service'),('garantia', 'Garantia'),('lavado', 'Lavado')],'Type', default='service')
    active = fields.Boolean('Activo', default=True)
    cantidad = fields.Integer('Cantidad')
    precio = fields.Float(string='Precio', size=16, digits=(16, 0))