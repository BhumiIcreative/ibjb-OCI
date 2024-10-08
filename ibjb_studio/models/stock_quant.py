# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.addons.ibjb_studio import common


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    date_de_premption = fields.Datetime(
        related="lot_id.expiration_date",
        store=True,
        string="Expiration date",
        readonly=False,
        help="This is the date when goods with this serial number become dangerous and should no longer be consumed.")

    coutlot_lot = fields.Float(
        related="lot_id.lot_cout",
        string="Coût du lot",
        readonly=True,
        store=True,
    )

    categorie = fields.Char(
        related="product_id.categorie",
        string="Category",
        readonly=True,
        store=True,
        translate=True
    )

    invenory_coutxqty = fields.Float(
        string="Cout x Qty",
    )

    active = fields.Boolean(
        rletaed="product_id.active",
        string="Activ",
        help="If unchecked, it will allow you to hide the product without removing it.",
        store=True,
        readonly=True,
    )

    catg_art = fields.Char(
        related="product_id.categ_id.name",
        string="Product reference",
        readonly=True,
        translate=True,
        store=True
    )

    ref_interne_1 = fields.Char(
        related="product_id.default_code",
        readonly=True,
        store=True,
        copy=False,
    )

    ref_interne_1 = fields.Char(
        related="product_id.default_code",
        string="ref_interne",
        store=True,
        readonly=True,
    )

    field_WfwqV = fields.Datetime(
        related='lot_id.expiration_date',
        string="Expiration date",
        readonly=True,
        store=True,
        help="This is the date on which the goods with this Serial Number may become dangerous and must not be consumed.",
    )

    oci_inventaire_note = fields.Text(
        string="Possible Comment",
        copy=False,
        store=True,
        tracking=True,
    )

    def Update_stock_quant_studio_fields(self):
        """
        server action code to migrate stock quant studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_date_de_premption": "date_de_premption",
            "x_studio_oci_coutlot_lot": "coutlot_lot",
            "x_studio_catgorie": "categorie",
            "x_studio_oci_invenory_coutxqty": "invenory_coutxqty",
            "x_studio_actif": "active",
            "x_studio_catg_art": "catg_art",
            "x_studio_field_WfwqV": "field_WfwqV",
            "x_studio_oci_inventaire_note": "oci_inventaire_note",
            "x_studio_ref_interne_1": "ref_interne_1",

        }
        for rec in self:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
