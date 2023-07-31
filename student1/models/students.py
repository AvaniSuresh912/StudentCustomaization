from odoo import _, api, fields, models, tools

class Student(models.Model):
    _name='schl.student'
    _description='schl_student'

    name = fields.Char(string="Name")
    age = fields.Char(string="Age")
    cls = fields.Char(string="Class")