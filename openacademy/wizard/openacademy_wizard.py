# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    
    def _default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_wiz_ids = fields.Many2many('openacademy.session',
            string="Session", required=True, default=_default_session)
    attendee_wiz_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        self.session_wiz_ids.attendee_ids |= self.attendee_wiz_ids
        return {}
