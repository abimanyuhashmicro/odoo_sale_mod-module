from odoo import models, api, fields


class SaleInherited(models.Model):
    _inherit = 'sale.order'

    def createMoAuto(self):
        pass
