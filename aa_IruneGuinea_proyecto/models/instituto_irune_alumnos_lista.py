# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Tabla intermedia donde estan las practicas que ha realizado el alumno
# Tambien se muestar el año de realizacion y cuanto dinero le han pagado
from odoo import api,fields, models

class InstitutoIruneAlumnos(models.Model):
    _name = "instituto.irune.alumnos.lista"
    _description = "Proyecto irune"
    alumno_id = fields.Many2one("instituto.irune",string="Alumno")
    anio_realiz=fields.Char(required=True,string='Año de realizacion', default="2023")
    aprobadas=fields.Boolean(required=True,string='Aprobadas',default=True)
    empresa2_id=fields.Many2one("instituto.irune.empresas",string='Empresa')
    alumnos2_ids=fields.One2many("instituto.irune","alumnos2_id")
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    dineros = fields.Monetary(string="Salario")
   