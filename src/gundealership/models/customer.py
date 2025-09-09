from odoo import models, fields

class Customer(models.Model):
    _name = 'gun.dealership.customer'
    _description = 'Customer (Killer/Agent)'

    name = fields.Char("Full Name / Alias", required=True)
    codename = fields.Char("Codename")
    affiliation = fields.Selection([
        ('assassin', 'Assassin'),
        ('spy', 'Spy'),
        ('mercenary', 'Mercenary'),
        ('antihero', 'Anti-Hero'),
    ], string="Affiliation")
    # NOTE: Use 'favorite_weapon' (US spelling) to match the views below
    favorite_weapon = fields.Many2one('gun.dealership.gun', string="Favorite Gun")
