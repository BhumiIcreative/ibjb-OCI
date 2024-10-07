# -*- coding: utf-8 -*-

from odoo import fields, models, api


class StockLot(models.Model):
    _inherit = 'stock.lot'

    motif_de_retrait_id = fields.Many2one(
        'lot.motif.retrait',
        string="Reason for withdrawal"
    )
    lot_date_stock = fields.Date(
        string="Date of entry into stock",
    )
    lot_pvcontrolekmatic = fields.Binary(
        string="PV supplier"
    )
    lot_pvcontrolekmatic_filename = fields.Char(
        string="Filename for lot_pvcontrolekmatic"
    )
    lot_versionihm = fields.Char(
        string="Version IHM"
    )
    lot_versionmoteur = fields.Char(
        string="Engine version",
    )
    lot_versionrfid = fields.Char(
        string="RFID version",
    )
    lot_versionmanuel = fields.Char(
        string="Manual version",
    )
    lot_cout = fields.Float(
        string="Cost of the lot",
    )
    inventory_lot_kmdispo = fields.Boolean(
        string="KM Available @IBJB",
    )
    inventory_lot_catgory = fields.Char(
        string="Category",
        related="product_id.categorie",
        store=True,
        translate=True,
        readonly=True,
    )
    cout_x_quantit = fields.Float(
        string="Cost x Quantity",
        comnpute="_compute_cout_x_quantit",
    )
    stock_cout_du_lot_unitaire = fields.Float(
        related="product_id.standard_price",
        store=False,
        readonly=True,
        string="Unit cost of the item",
        help="Cost used for stock valuation in standard price and as a first price to set in average/fifo. Also used "
             "as a base price for price lists. Expressed in the default unit of measurement of the product."
    )

    @api.depends('product_qty', 'lot_cout')
    def _compute_cout_x_quantit(self):
        """
            Compute the total cost (`cout_x_quantit`) for each record.
        """
        for record in self:
            if record.product_qty and record.lot_cout:
                record.cout_x_quantit = record.product_qty * record.lot_cout
            else:
                record.cout_x_quantit = 0
