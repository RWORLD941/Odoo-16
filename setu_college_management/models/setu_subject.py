from odoo import models,fields
import datetime


class SetuSubject(models.Model):
    _name = "setu.subject"
    _rec_name = "name"
    _description = "Subject Records"
    _order = "id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Subject Name", required=True, tracking=True)
    # professor = fields.Char("Professor Name")
    medium = fields.Selection(selection=[('english', 'English'),
                                ('hindi', 'Hindi')],
                                required=True, default='english')


    book_ids = fields.One2many('setu.book','subject_id')