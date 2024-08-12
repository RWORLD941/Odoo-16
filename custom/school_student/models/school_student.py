from odoo import fields, models

class school_student(models.Model):
    _name = "school.student"
    _description = "school_student.school_student"

    name = fields.Char()
    school_id = fields.Many2one("school.profile",string="School",required=True)