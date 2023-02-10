# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Feb22Irune',
    'version': '1.0',
    'category': 'Technical',
    'description': 'Módulo de proyecto irune',
    'summary': 'Irune',
    'depends': [
        'base',
    ],
    'data': [

        'security/ir.model.access.csv',
        'views/instituto_irune_empresas_view.xml',
        'views/instituto_irune_view.xml',
        'views/instituto_irune_asignaturas_view.xml',
        'views/instituto_irune_profesores_view.xml',
        'views/instituto_irune_alumnos_lista_view.xml',
        'views/instituto_irune_tag_view.xml',
        'views/instituto_irune_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
