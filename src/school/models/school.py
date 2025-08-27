from odoo import models, fields

class School(models.Model):
    _name = 'school.school'
    _description = 'School'

    name = fields.Char(string="School Name", required=True)
    city = fields.Char(string="City")
    student_ids = fields.One2many('school.student', 'school_id', string="Students")


class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Full Name", required=True)
    age = fields.Integer(string="Age")
    school_id = fields.Many2one('school.school', string="School")
