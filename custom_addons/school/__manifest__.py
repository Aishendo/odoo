# -*- coding: utf-8 -*-

{
    'name': 'University Management',
    'version': '1.0.0',
    'author' : 'Aisha',
    'category': 'University',
    'sequence': -100,
    'summary': 'University Management System',
    'description': """University Management System""",
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/univer_view.xml"
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}