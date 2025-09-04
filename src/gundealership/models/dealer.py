from odoo import models, fields

class Dealer(models.Model):
    _name = 'gun.dealership.dealer'
    _description = 'Gun Dealer'

    name = fields.Char(string="Dealer Name", required=True)
    country = fields.Char(string="Country")
    license_no = fields.Char(string="License Number")
    gun_ids = fields.One2many('gun.dealership.gun', 'dealer_id', string="Guns")
