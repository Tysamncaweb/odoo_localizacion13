# -*- coding: utf-8 -*-

from odoo import api, fields, models, _ 



class AccountMove(models.Model):
    _inherit = 'account.move'

    wh_muni_id = fields.Many2one('wh.municipality', string='Withholding')


    def action_post(self):
        super().action_post()
        vals = {}
        voucher = self.env['wh.municipality']
        vals = {
            'partner_id': self.partner_id.id,
            'vat': self.partner_id.vat,
        }
        muni_id = voucher.create(vals)
        self.write({'wh_muni_id': muni_id})
