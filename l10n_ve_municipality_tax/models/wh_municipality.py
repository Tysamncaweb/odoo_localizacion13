# -*- coding: utf-8 -*-



from odoo import api, fields, models, _



class WhMuniConcepts(models.Model):
    _name = 'wh.muni.concepts'

    name = fields.Char(string='Concept', help='Withholding Municipality Concept.')
    code = fields.Char(string='Code')
    aliquot = fields.Float(string='Aliquot')



class MuniLineTaxes(models.Model):
    """This model is Withholding Voucher for Municipality taxes."""
    _name = 'muni.line.taxes'

    name = fields.Text(string="Description")
    wh_muni_id = fields.Many2one('wh.municipality', string='Withholding')
    concept_id = fields.Many2one('wh.muni.concepts', string='wh.muni.concepts')
    invoice_id = fields.Many2one('account.move', string='Invoice')


class WhMunicipality(models.Model):
    _name = 'wh.municipality'


    name = fields.Char(string='Voucher number')
    description = fields.Char(string='Description')
    partner_id = fields.Many2one('res.partner', string="Partner")
    rif = fields.Char(string='RIF')
    type = fields.Selection(selection=[
        ('out_invoice', 'Customer Invoice'),
        ('in_invoice', 'Supplier Invoice'),
        ], string='Origin', readonly="True")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ], string='Status')
    acc_date = fields.Date(string="Accounting Date")
    muni_line_tax_ids = fields.One2many('muni.line.taxes', 'wh_muni_id', string='Municipality Taxes')
