from odoo import _, api, fields, models, tools

class Teacher(models.Model):
    _name='schl.teacher'
    _description='schl_teacher'

    name = fields.Char(string="Name")
    age = fields.Char(string="Age")
    cls = fields.Char(string="Class")