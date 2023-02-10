# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modulo para las empresas en las que los alumnos van a hacer practicas
# Aqui se puede asignar un alumno a la empresa
from odoo import fields, models, api

class Asignaturas(models.Model):
    _name = "instituto.irune.asignaturas"
    _description = "Objeto asignaturas"
    name=fields.Text(required=True,string="Nombre")
    