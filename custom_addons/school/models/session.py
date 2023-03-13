from odoo import api, fields, models
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

class Session(models.Model):
    _name = "session"
    _description = "Session"

    name = fields.Char(string='Session', required=True, translate=True)
    type = fields.Selection([
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ], string="Class Type",
        required=True,
        help="The 'Class Type' is used for features available on "\
        "different types of classes: 5/6/7/8/9 type is for middle school subjects" \
        ", 10/11/12 is for high school subjects.")
    group = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ], string="Class Group",
        required=True, default='a',
        help="The 'Class Group' is used to filter classes based on the class group set on the class type.")
