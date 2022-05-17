from odoo import models, api, fields


class SaleInherited(models.Model):
    _inherit = 'sale.order'

    def createMoAuto(self):
        for record in self.order_line:
            for singlebom in record.product_id.bom_ids:
                bom_data = record.env['mrp.bom'].search([('id', '=', singlebom.id)])
                stock_move_ids = []
                if bool(bom_data) == True:
                    record.env['mrp.production'].create({
                        'product_id': record.product_id.id, 
                        'product_uom_id': record.product_id.bom_ids.product_uom_id.id, 
                        'bom_id': singlebom.id, 
                        'product_qty': record.product_uom_qty,})
                    for bomsing in singlebom.bom_line_ids:
                        vals = {
                            'company_id': bomsing.company_id.id,
                            'bom_line_id': bomsing.id,
                            'name': 'New',
                            'product_id': bomsing.product_id.id,
                            'product_uom': record.product_uom.id,
                            'procure_method': 'make_to_order',
                            'product_uom_qty': bomsing.product_qty * record.product_uom_qty,
                            'company_id': self.company_id.id,
                            'location_id': record.product_id.with_company(self.company_id).property_stock_production.id,
                            'location_dest_id': record.product_id.with_company(self.company_id).property_stock_production.id,
                        }
                        record.env['stock.move'].create(vals)
                        stock_move = self.env['stock.move'].search([],limit=1, order='id desc')
                        stock_move_ids.append(stock_move.id)
                    target_mrp_prod = self.env['mrp.production'].search([],limit=1, order='id desc') # ambil record terbaru yang dibuat
                    self.env['mrp.production'].search([('id', '=', target_mrp_prod.id)]).write({'move_raw_ids': stock_move_id,}) # update move_raw_ids


