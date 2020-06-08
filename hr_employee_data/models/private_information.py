# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PrivateInformation(models.Model):
    _inherit = 'hr.employee'

    

    country_birth_id = fields.Many2one('res.country', string='Country of birth')
    state_birth_id = fields.Many2one('res.country.state', string='State of birth')
    city_birth_id = fields.Many2one(string='City of birth')
    age = fields.Integer(string='Age')
    marriage_certificate = fields.Boolean(string='Marriage certificate')
    rif = fields.Char(string='RIF')
    blood_group = fields.Selection([
        ('a','A'),
        ('b','B'),
        ('ab','AB'),
        ('o','O')], string='Blood group')
    hr_factor = fields.Selection([
        ('negative','Negative'),
        ('positive', 'Positive')], string='Hr factor')
    state_residence_id = fields.Many2one('res.country.state', string='Country of residence')
    city_residence_id = fields.Many2one('res.country.city', string='City of residence')
    residence_municipality = fields.Char(string='Municipality')
    postal_code = fields.Char(string='Postal code')
    avenue_street = fields.Char(string='Avenue/street')
    building_house = fields.Char(string='Building/House')
    apartment = fields.Char(string='Apartment')
    floor = fields.Integer(string='Floor')
    mobile_phone = fields.Char(string='Mobile phone')
    shoes_size = fields.Char(string='Shoes size')
    height = fields.Integer(string='Height')
    weight = fields.Integer(string='Weight')
    disable_employee = fields.Boolean(string="Disable")
    resignation = fields.Selection([
        ('dismissal', 'Dismissal'),
        ('resignation', 'Resignation'),
    ], string='Resignation / Dismissal')
    observation = fields.Char(string='Observation')
    hand = fields.Selection([
        ('left', 'Left handed'),
        ('right', 'Right Handed'),
    ], string='Hand')
    years = fields.Integer(string='Years')
    months = fields.Integer(string='Months')
    days = fields.Integer(string='Days')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    transport =fields.Selection([
        ('bus','Bus'),
        ('car','Car'),
        ('motorcircly', 'Motorcicly'),
        ('subway', 'Subway'),
        ('train', 'Train'),
    ], string='Transport')
    work_home_distance = fields.Integer(string='Distance home work', help="Distance from home to work in km")
    leave_types = fields.Selection([
        ('excused_absences', 'Excused Absences'),
        ('unexcused_absences', 'Unexcused Absences')
    ], string='Leave types')
