from odoo import models, fields

class Document(models.Model):
    _name = "school.document"
    _description = "Talaba hujjatlari"

    name = fields.Char(string="Hujjat nomi", required=True)
    file_data = fields.Binary(string="Fayl")
    file_name = fields.Char(string="Fayl nomi")
