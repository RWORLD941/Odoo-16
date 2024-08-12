from odoo import models,fields
import datetime


class SetuProfessor(models.Model):
    _name = "setu.professor"
    _rec_name = "id"
    _description = "Professor's Register"
    _order = "id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Professor Name",required=True,help="Enter Professor Name", tracking=True)
    avg_salary = fields.Float(string="Average Salary")
    age = fields.Integer("Age")
    subject = fields.Char("Subject")
    college_id = fields.Many2one('setu.college', string="College")