from odoo import models, fields

class UzumProduct(models.Model):
    _name = "uzum.product"
    _description = "Uzum Market Product"

    name = fields.Char("Product Name", required=True)
    category = fields.Selection([
        ('electronics', 'Electronics'),
        ('books', 'Books'),
        ('home', 'Home'),
        ('sports', 'Sports'),
    ], required=True)
    subcategory = fields.Selection([
        ('laptop', 'Laptop'),
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('accessories', 'Accessories'),
        ('trousers', 'Trousers'),
        ('shoes', 'Shoes'),
        ('glasses', 'Glasses'),
    ])
    price = fields.Float("Price", required=True)
    stock = fields.Integer("Stock", default=0)
    color = fields.Selection([
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('black', 'Black'),
        ('white', 'White'),
    ])
    rating = fields.Float("Rating", default=0.0)
    description = fields.Text()

dealer_id = fields.Many2one("uzum.dealer", string="Dealer")
