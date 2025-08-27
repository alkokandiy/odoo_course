# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleTwo(http.Controller):
#     @http.route('/module_two/module_two', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_two/module_two/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_two.listing', {
#             'root': '/module_two/module_two',
#             'objects': http.request.env['module_two.module_two'].search([]),
#         })

#     @http.route('/module_two/module_two/objects/<model("module_two.module_two"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_two.object', {
#             'object': obj
#         })

