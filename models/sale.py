from odoo import models, api, fields


class SaleInherited(models.Model):
    _inherit = 'sale.order'

    def createMoAuto(self):
        target = []
        target_browse = self.env['sale.order'].browse(self.id)
        for k in target_browse:
            target.append([{
                'product_id':k.order_line.product_id.id,
                'bom_id':k.order_line.product_id.bom_ids.id,
                'hrg_bom':k.order_line.product_id.bom_ids.hrg_bom,
                'product_qty':k.order_line.product_uom_qty,
                'product_uom_id':k.order_line.product_id.bom_ids.product_uom_id.id,
            }])
        tar_product_id = target[0][0]["product_id"]
        tar_product_qty = target[0][0]["product_qty"]
        tar_bom_id = target[0][0]["bom_id"]
        tar_hrg_bom = target[0][0]["hrg_bom"]
        tar_product_uom_id = target[0][0]["product_uom_id"]
        if tar_hrg_bom > 0:
            self.env['mrp.production'].create({'product_id': tar_product_id, 'product_uom_id': tar_product_uom_id, 'bom_id': tar_bom_id, 'product_qty': tar_product_qty})
        else:
            pass

