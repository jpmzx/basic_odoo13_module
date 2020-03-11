# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'

    name = fields.Char(string="Title", required=True, help="Name of the Course")
    description = fields.Text()