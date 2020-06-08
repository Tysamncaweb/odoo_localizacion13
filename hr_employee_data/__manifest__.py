# -*- coding: utf-8 -*-

{
        'name': 'Employees Data',
        'category': 'Human Resources',
        'author': 'Tysamnca',
        'description': """
            This module add information about family, address, studies and required fields for venezuelan law.
        """,
        'depends': [
            'base',
            'hr',
            'hr_contract'
            ],
        'data': [
            'views/private_information_views.xml',
            ],
        'installable': True,
        
        }
