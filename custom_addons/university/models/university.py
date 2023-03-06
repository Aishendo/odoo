from odoo import fields, models

class UniProfile(models.Model):
    _name = "uni.profile"

    name = fields.Char(string="University Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
