# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modulo para las empresas en las que los alumnos van a hacer practicas
# Aqui se puede asignar un alumno a la empresa
from odoo import fields, models, api
from odoo.exceptions import UserError
class Empresa(models.Model):
    _name = "instituto.irune.empresas"
    _description = "Objeto empresa"
    name=fields.Text(required=True,string="Nombre")
    direccion=fields.Text(string='Direccion')
    telefono=fields.Text(string='Telefono')
    departamento=fields.Selection(string='Departamento',selection=[('informatica','Informatica'),('comercio','Comercio'),('marketing','Marketing'),('administracion','Administracion')],default='informatica')
    alumnos_ids=fields.One2many("instituto.irune","empresa_id")
    alumnos_lista_ids=fields.One2many("instituto.irune.alumnos.lista","empresa2_id")
    disponibilidad=fields.Selection(readonly=True,string="Disponibilidad 2023",selection=[('disponible','Disponible'),('nodisponible','No disponible')],default='disponible')
    
    def cambiar_disponibilidad(self):
                for record in self:
                        if record.disponibilidad == "disponible":
                                record.disponibilidad = "nodisponible"
                        else:
                             raise UserError("No puedes poner no disponible una empresa que ya lo esta!")   
                return True