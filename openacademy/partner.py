from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
