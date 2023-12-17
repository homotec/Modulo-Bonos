# -*- coding: utf-8 -*-


from odoo import models, api, _
from odoo.exceptions import ValidationError


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        user_limit = int(ICPSudo.get_param('user_limit_restriction.user_limit'))
        users = self.search_count([])
        if users >= user_limit:
            raise ValidationError(_('You cannot create more user, User Limit has been exceeded.'))
        return super(ResUsers, self).create(vals)

    def write(self, vals):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        user_limit = int(ICPSudo.get_param('user_limit_restriction.user_limit'))
        users = self.search_count([])
        if vals.get('active'):
            if users >= user_limit:
                raise ValidationError(_('You cannot create more user, User Limit has been exceeded.'))
        return super(ResUsers, self).write(vals)