from openerp import models, fields, api

'''
This module create model of course
'''

class Course(models.Model):
    '''
    This class create model of course
    '''
    _name = 'openacademy.course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',
                                    ondelete='set null', 
                                    string="Responsible", index=True)

