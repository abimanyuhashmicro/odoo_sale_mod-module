from odoo import models, api, fields


class SaleInherited(models.Model):
    _inherit = 'sale.order'

    def createMoAuto(self):
        bom_data = self.env['mrp.bom'].search([('id', '=', self.order_line.product_id.bom_ids.id)]).read()
        if bom_data[0]['hrg_bom'] > 0:
            self.env['mrp.production'].create({
                'product_id': self.order_line.product_id.id, 
                'product_uom_id': self.order_line.product_id.bom_ids.product_uom_id.id, 
                'bom_id': self.order_line.product_id.bom_ids.id, 
                'product_qty': self.order_line.product_uom_qty})


