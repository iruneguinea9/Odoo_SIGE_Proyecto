# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# PROYECTO SIGE IRUNE MODULO INSTITUTO
# 08/02/2023
# instituto_irune muestra los alumnos y sus caracteristicas
from odoo import api,fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

class InstitutoIrune(models.Model):
    _name = "instituto.irune"
    _description = "Proyecto irune"
    name =fields.Text(required=True,string='Nombre')
    apellidos=fields.Text(required=True,string='Apellidos')
    fecha_nac=fields.Date(required=True,string='Fecha de nacimiento',default = date.today() + relativedelta(years=-16))
    direccion=fields.Text(string='Direccion')
    codigo_postal=fields.Text(string='Codigo postal')
    email=fields.Text(string='Email')
    github=fields.Text(string='Enlace a github',required=True,default="https://github.com/iruneguinea9")
    ciclo = fields.Selection(string='Ciclo formativo',selection=[('asir','ASIR'),('dam','DAM'),('daw','DAW')],required=True,help="Ciclo")
    coche=fields.Boolean(string='Coche')
    otros=fields.Text(string='Otros')

    actitud=fields.Float(string='Actitud y asistencia (%5)',default="5.0")
    ejercicios=fields.Float(string='Ejercicios de clase (%20)',default="5.0")
    proyecto=fields.Float(string='Proyecto (%55)',default="5.0")
    examen=fields.Float(string='Examen sobre el propio proyecto (%20)',default="5.0")

    nota_media=fields.Float(compute="_compute_notaMedia",readonly=True,string='Nota media',default="5.0")
    nota_media_texto= fields.Text(default="aprobado",string='Nota',compute="_compute_nota",readonly=True) # es un compute
    empresa_id=fields.Many2one("instituto.irune.empresas",string='Empresa')
    alumnos2_id=fields.Many2one("instituto.irune.alumnos.lista",string='Alumnos')
    tag_ids = fields.Many2many("instituto.irune.tag", string="Tag")
    # Para calcular la nota en texto con la nota media
    @api.depends("nota_media")
    def _compute_nota(self):
        for record in self:
            if(record.nota_media<5):
                record.nota_media_texto="suspenso"
            else:
                if(record.nota_media>=5 and record.nota_media<7):
                    record.nota_media_texto="aprobado"
                else:
                    if(record.nota_media>=7 and record.nota_media<9):
                        record.nota_media_texto="notable"
                    else:
                        record.nota_media_texto="sobresaliente"
    # Para ponerle un boton con el enlace a github del alumno, accion de URL
    @api.depends("github")
    def irune_url(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': self.github,
                'target': 'new',
            }

    # Para calcular la nota media
    @api.depends("actitud","proyecto","ejercicios","examen")
    def _compute_notaMedia(self):
        for record in self:
            # actitud
            porActitud = ( self.actitud * 5 )/100
            #ejercicios
            porEjercicios  =( self.ejercicios * 20 )/100
            #proyecto
            porProyecto=( self.proyecto * 55 )/100
            #examen
            porExamen =( self.examen * 20 )/100
            record.nota_media = porActitud+porEjercicios+porProyecto+porExamen