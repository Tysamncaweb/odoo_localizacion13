# -*- coding: utf-8 -*-



from odoo import api, fields, models, _



class ConceptRetentionIslr(models.Model):
    """This model set the concept of application for ISLR """
    _name = 'concept.retention.islr'


    name = fields.Char(string='Concept')
    






class IslrRetentionRates(models.Model):
    """Rates for ISLR. """
    _name = 'islr.retention.rate'


    name = fields.Char(string='Name')






