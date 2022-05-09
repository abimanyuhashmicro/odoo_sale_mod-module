from odoo import models, api, fields


class SaleInherited(models.Model):
    _inherit = 'sale.order'

    def createMoAuto(self):
        for record in self.order_line:
            for singlebom in record.product_id.bom_ids:
                bom_data = record.env['mrp.bom'].search([('id', '=', singlebom.id)]).read()
                if bool(bom_data) == True:
                    record.env['mrp.production'].create({
                        'product_id': record.product_id.id, 
                        'product_uom_id': record.product_id.bom_ids.product_uom_id.id, 
                        'bom_id': singlebom.id, 
                        'product_qty': record.product_uom_qty})


