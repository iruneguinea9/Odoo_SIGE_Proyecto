# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modulo para las empresas en las que los alumnos van a hacer practicas
# Aqui se puede asignar un alumno a la empresa
from odoo import fields, models, api

class Profesores(models.Model):
    _name = "instituto.irune.profesores"
    _description = "Objeto profesores"
    name=fields.Text(required=True,string="Nombre")
    apellidos=fields.Text(string='Apellidos',required=True)
    email=fields.Text(string='Email')
    asignaturas_ids = fields.Many2many("instituto.irune.asignaturas", string="Asginaturas")
    departamento=fields.Selection(string='Departamento',selection=[('informatica','Informatica'),('comercio','Comercio'),('marketing','Marketing'),('administracion','Administracion')],default='informatica')
