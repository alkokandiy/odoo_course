from odoo import models, fields


class Customer(models.Model):
    _name = 'gun.dealership.customer',
    _description = 'Customer (Killer/Agent)'

    name = fields.Char("Full Name / Alias", required=True)
    codename = fields.Chat("Codeename")
    affiliation = feilds.Selection([
        ('assassin', 'Assassin'),
        ('spy', 'Spy'),
        ('mercenary', 'Mercenary'),
        ('antihero', 'Antihero')
    ], string="Affiliation")

    favourite_weapon = fields.Many2one('gun.dealership.gun', string="Favourite Gun")
