from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'
    iface_product_label = fields.Boolean(
        'Show product label button',
        help="Print product labels with this POS"
    )
