from odoo import models, fields

class Gun(models.Model):
    _name = "gun.dealership.gun"
    _description = "Gun"

    name = fields.Char(string="Gun Name", required=True)
    type = fields.Selection([
        ('rifle', 'Rifle'),
        ('pistol', 'Pistol'),
        ('shotgun', 'Shotgun'),
        ('other', 'Other')
    ], string="Type", required=True)

    caliber = fields.Char(string="Caliber")
    price = fields.Float(string="Price", required=True)
    stock = fields.Integer(string="Stock", required=True)
    dealer_id = fields.Many2one("gun.dealership.dealer", string="Dealer", required=True)
