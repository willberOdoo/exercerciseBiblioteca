# -*- coding: UTF-8 -*-

from odoo import models, fields, api


class Library(models.Model):

    _name = 'library'
    _description = 'choose books'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(String='Description')

    level = fields.Selection(string='Book features',
                             selection=[('scientific', 'Scientific'),
                                        ('biographies', 'Biographies'),
                                        ('monographs',  'Monographs'),
                                        ('verse',       'Verse')],
                             copy=False)

    activate = fields.Boolean(string='Activate', default=True)

