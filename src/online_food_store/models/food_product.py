from odoo import models, fields

class FoodProduct(models.Model):
    _name = "food.product"
    _description = "Food Product"

    name = fields.Char(string="Product Name", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price", required=True)
    quantity = fields.Integer(string="Quantity in Stock", default=0)
