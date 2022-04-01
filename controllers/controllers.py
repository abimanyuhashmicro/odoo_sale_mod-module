# -*- coding: utf-8 -*-
# from odoo import http


# class SaleMod(http.Controller):
#     @http.route('/sale_mod/sale_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_mod/sale_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_mod.listing', {
#             'root': '/sale_mod/sale_mod',
#             'objects': http.request.env['sale_mod.sale_mod'].search([]),
#         })

#     @http.route('/sale_mod/sale_mod/objects/<model("sale_mod.sale_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_mod.object', {
#             'object': obj
#         })
