# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.addons.ibjb_studio import common


class Family(models.Model):
    _name = 'family'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This Model is Family of articles"

    name = fields.Char(string="Name")
    oci_famille_article_product_template_count = fields.Integer(string="Article(s)",
                                                                compute="_compute_product_template_count",
                                                                readonly=False)
    oci_famillearticle_description = fields.Text(string="Description")

    def _compute_product_template_count(self):
        """
            Compute the number of product templates linked to the current record (oci_famille_article_id).
        """
        product_templates = self.env['product.template'].search(
            [('oci_famille_article_id', 'in', self.ids)]
        )

        # Create a dictionary to store the counts per famille_id
        famille_article_counts = {}
        for product in product_templates:
            famille_id = product.oci_famille_article_id.id
            famille_article_counts[famille_id] = famille_article_counts.get(famille_id, 0) + 1

        # Update the count on each record in self
        for record in self:
            record.oci_famille_article_product_template_count = famille_article_counts.get(record.id, 0)

    def Update_family_studio_fields(self):
        """
            server action code to migrate Family studio fields data to custom fields.
        """
        migration_fields = {
            "x_name": "name",
            # "x_x_studio_oci_famille_article__product_template_count": "oci_famille_article_product_template_count",
            "x_studio_oci_famillearticle_description": "oci_famillearticle_description",
        }
        family_records = self.search([])
        for rec in family_records:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)
