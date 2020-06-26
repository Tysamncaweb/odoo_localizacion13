# -*- coding: utf-8 -*-


{
    'name': 'Municipal Withholdings for Venezuela',
    'version': '0.2',
    'author': 'Tysamnca',
    'description': 'Municipal Withholding for Venezuela',
    'category': 'Accounting/Accounting',
    'depends': [
        'account',
        'account_accountant',
        'base',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/wh_municipality_views.xml',
        'report/report_wh_tax_voucher.xml',
        ],
    'installable': True,        
}
