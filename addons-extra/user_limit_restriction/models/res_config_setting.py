# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    user_limit = fields.Integer(string='Set User Limit')

    @api.model
    def get_values(self):
        res = super(ResConfig, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        user_limit = int(ICPSudo.get_param('user_limit_restriction.user_limit'))
        res.update(
            user_limit=user_limit,
        )
        return res

    def set_values(self):
        super(ResConfig, self).set_values()
        self.env['ir.config_parameter'].set_param("user_limit_restriction.user_limit", self.user_limit or '')
