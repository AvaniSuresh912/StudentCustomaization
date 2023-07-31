# -*- coding: utf-8 -*-
# from odoo import http


# class Student1(http.Controller):
#     @http.route('/student1/student1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student1/student1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student1.listing', {
#             'root': '/student1/student1',
#             'objects': http.request.env['student1.student1'].search([]),
#         })

#     @http.route('/student1/student1/objects/<model("student1.student1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student1.object', {
#             'object': obj
#         })
