# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modulo para ponerle caracteristicas al alumno
from odoo import fields, models

class InstitutoTag(models.Model):
    _name = "instituto.irune.tag"
    _description = "Modulo irune tag"
    name = fields.Char(required=True)