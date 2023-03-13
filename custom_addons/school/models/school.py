from odoo import api, fields, models

class choolProfile(models.Model):
    _name = "school.profile"
    _description = "university Profile"

    name = fields.Char(string="University Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
