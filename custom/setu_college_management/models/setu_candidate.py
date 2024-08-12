from odoo import models,fields
import datetime


class SetuCandidate(models.Model):
    _name = "setu.candidate"
    _rec_name = "roll_no"
    _description = "Candidate Register"
    _order = "id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Candidate Name", required=True, help="Enter Candidate Name", tracking=True)
    roll_no = fields.Integer("Roll No")
    year = fields.Integer("Year")
    subject = fields.Char("Subject")