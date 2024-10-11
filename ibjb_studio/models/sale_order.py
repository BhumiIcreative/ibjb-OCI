# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.addons.ibjb_studio import common

# logger = logging.getLogger(__name_)


# from v12.enterprise.pos_blackbox_be.models.pos_blackbox_be import product_template


class SaleOrder(models.Model):
    _inherit = "sale.order"

    abonnement_equipement_id = fields.Many2one(
        "maintenance.equipment",
        string="Maintenance Equipement",
        ondelete="set null",
        copy=False,
    )  # sale_subscription field

    # No need to migarte below fields as they are all related field
    customer_vat = fields.Char(
        related="partner_id.tva",
        string="Customer TVA",
        readonly=True,
        copy=False,
        store=True,
    )
    oci_saleorder_codetiers = fields.Char(
        related="partner_id.customer_code",
        string="Code tiers",
        readonly=True,
        copy=False,
        store=True,
    )
    oci_vente_langcustomer = fields.Selection(
        related="partner_id.lang",
        string="Customer language",
        help=(
            "All emails and documents sent to this contact will be translated into this language."
        ),
        store=True,
        copy=False,
        readonly=True,
    )

    field_aueov_id = fields.Many2one(
        "maintenance.equipment", string="Equipement de maintenance"
    )

    oci_bdc_dateexpsht = fields.Date(
        string="Desired shipping date",
        store=True,
        copy=False,
    )

    oci_sale_priceliste_enddate = fields.Date(
        related="pricelist_id.datelifeend",
        string="End of validity of price list",
        store=True,
        copy=False,
    )

    saleorder_order_carrier = fields.Selection(
        related="partner_id.oci_contact_transporteur",
        string="Transportor Carrier",
        copy=False,
        readonly=True,
    )

    oci_bdc_transporteur = fields.Selection(
        selection=[
            ("DHL", "DHL"),
            ("DPD", "DPD"),
            ("TNT", "TNT"),
            ("TSE", "TSE"),
            ("ENLEVEMENT", "ENLEVEMENT"),
            ("CHRONOPOST", "CHRONOPOST"),
            ("CHRONOPOST INTERNATIONAL", "CHRONOPOST INTERNATIONAL"),
            ("TNT INTERNATIONAL", "TNT INTERNATIONAL"),
            ("Transporteur client / Customer carrier", "Transporteur client / Customer carrier"),
        ],
        copy=False,
        string="Transportor",
        store=True,
        tracking=True,
    )

    oci_chplie_customercomment1 = fields.Html(
        related="partner_id.comment",
        string="Internal note",
        copy=False,
        readonly=True,
        store=True,
    )

    purchase_order_reference = fields.Char(
        string="Order reference",
        copy=False,
        store=True,
    )

    tva_msg_europe = fields.Char(
        copy=False,
        store=True,
    )

    @api.model
    def update_studio_fields(self):
        print('\n\n\n\nupdate_sale_studio_fields', self)
        """
        schedule action code to migrate sale studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_customer_tva": "customer_vat",
            "x_studio_oci_saleorder_codetiers":"oci_saleorder_codetiers",
            "x_studio_oci_vente_langcustomer":"oci_vente_langcustomer",

        }
        sale_orders = self.search([])  # Fetch all sale  records
        print('\n\n\n\nsale_orders',sale_orders)
        for rec in sale_orders:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)

    @api.model
    def update_sale_order_line_studio_fields(self):
        print('\n\n\n\nupdate_sale_studio_fields', self)
        """
        schedule action code to migrate sale studio fields data to custom fields.
        """
        migration_fields = {
            "x_studio_studio_customer_code": "name",

        }
        sale_orders = self.search([])  # Fetch all sale  records
        print('\n\n\n\nsale_orders', sale_orders)
        for rec in sale_orders.order_line:
            for x_field, field in migration_fields.items():
                common.set_customer_field(rec, x_field, field)

    # def get_field_type(self, field_name):
    #     print('\n\n\n\nget_field_type',self)
    #     """
    #     Return the field type
    #     """
    #     field_info = self.fields_get([field_name], attributes=("type"))
    #     if field_info:
    #         return field_info.get(field_name, {}).get("type")
    #     else:
    #         return False
    #
    # def set_customer_field(self, rec, x_field_name, field):
    #     print('\n\n\n\nset_customer_field', self)
    #     """
    #     Function to set the custom field same as studio field if has same field type
    #     """
    #     if hasattr(rec, x_field_name):
    #         print('\n\n\nhas attr rec',rec)
    #         print('\n\n\nhas attr x_field_name', x_field_name)
    #         x_field_type = self.get_field_type(x_field_name)
    #         print('\n\n\nhas attr x_field_type', x_field_type)
    #         custom_field_type = self.get_field_type(field)
    #         print('\n\n\nhas attr custom_field_type', custom_field_type)
    #         if x_field_type == custom_field_type:
    #             setattr(rec, field, getattr(rec, x_field_name, False))

    #
    # def update_fields_data(self):
    #     print('\n\n\n\ncron job running')
    #
    #     # Odoo v12 connection
    #     url = "http://localhost:8011"
    #     db = 'v12_2024_10_04'
    #     username = 'admin'
    #     password = 'admin'
    #
    #     # Odoo v17 connection
    #     second_url = "http://localhost:8080"
    #     second_db = 'injb_studio_v17_8'
    #     second_username = 'admin'
    #     second_password = 'admin'
    #
    #     # Connect to Odoo v12
    #     common_v12 = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    #     uid_v12 = common_v12.authenticate(db, username, password, {})
    #     models_v12 = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    #
    #     # Connect to Odoo v17
    #     common_v17 = xmlrpc.client.ServerProxy(f'{second_url}/xmlrpc/2/common')
    #     uid_v17 = common_v17.authenticate(second_db, second_username, second_password, {})
    #     models_v17 = xmlrpc.client.ServerProxy(f'{second_url}/xmlrpc/2/object')
    #
    #     # Connect to PostgreSQL for direct queries
    #     connection = psycopg2.connect(database=db)
    #     cursor = connection.cursor()
    #
    #     # Fetch custom fields from Odoo v12
    #     fields = models_v12.execute_kw(db, uid_v12, password, 'ir.model.fields', 'search', [
    #         [['state', '=', 'manual'], ["related", "=", False], ["compute", "=", False], ["store", "=", True],
    #          ['ttype', '=', 'char']]
    #     ])
    #
    #     print("fields================", len(fields))
    #
    #     for field_id in fields:
    #         field_model_id = models_v12.execute_kw(db, uid_v12, password, 'ir.model.fields', 'search_read',
    #                                                [[['id', '=', field_id]]],
    #                                                {'fields': ['model_id', 'name']})
    #         model_id = field_model_id[0].get("model_id")[0]
    #         field_name = field_model_id[0].get("name")
    #         # print('\n\n\n\nfield_name',field_name)
    #
    #         model_name_list = models_v12.execute_kw(db, uid_v12, password, 'ir.model', 'search_read',
    #                                                 [[['id', '=', model_id]]],
    #                                                 {'fields': ['model']})
    #         model_name = model_name_list[0].get("model")
    #
    #         all_recs = models_v12.execute_kw(db, uid_v12, password, model_name, 'search', [[]])
    #         # print('\n\n\nall recs',all_recs)
    #
    #         model_field = models_v12.execute_kw(db, uid_v12, password, model_name, "fields_get", [field_name])
    #         # print('\n\n\nmodel_field',model_field)
    #
    #         count = 0
    #         for record in all_recs:
    #             # print('\n\n\nrecord',record)
    #             field_type = model_field.get(field_name).get("type")
    #             # print('\n\n\nfield_type',field_type)
    #             if field_type == "char":
    #                 updated_model_name = model_name.replace(".", "_")
    #                 # print('\n\n\nupdated_model_name',updated_model_name)
    #                 cursor.execute(f"SELECT \"{field_name}\" FROM {updated_model_name} WHERE id={record};")
    #                 char_field_val = cursor.fetchone()
    #                 # print('\n\n\nchar_field_val',char_field_val)
    #                 if isinstance(char_field_val, tuple):
    #                     val = char_field_val[0]
    #                     print('\n\n\n\nval===1',val)
    #                 else:
    #                     val = char_field_val
    #                     print('\n\n\n\nval===2', val)
    #
    #                 # if field_name == "x_studio_categorie":
    #                     #     # val = False
    #                     # print("char_field_val===============================", val, field_name, record, model_name)
    #                     # local_field = models_v17.execute_kw(second_db, uid_v17, second_password, model_name, 'write',
    #                     #                                     [[record], {field_name: val}])
    #
    #     cursor.close()
    #     connection.close()
    #     print("\n\n\n\n\nData migration completed.")

    # ====================================================================================

    # def update_fields_data(self):
    #     orders = self.search([])
    #     print('\norders::::::::', orders)
    #     for order in orders:
    #             order.origin = order.x_studio_new_source_doc
    #
    #
    #     # Odoo v12 connection
    #     url = "http://localhost:8011"
    #     db = 'v12_2024_10_04'
    #     username = 'admin'
    #     password = 'admin'
    #
    #     # Odoo v17 connection
    #     second_url = "http://localhost:8080"
    #     second_db = 'injb_studio_v17_8'
    #     second_username = 'admin'
    #     second_password = 'admin'
    #
    #     # Connect to Odoo v12
    #     common_v12 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    #     uid_v12 = common_v12.authenticate(db, username, password, {})
    #     models_v12 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #
    #     connection = psycopg2.connect(
    #         database="v12_2024_10_04"
    #     )
    #     cursor = connection.cursor()
    #
    #     # Connect to Odoo v17
    #     common_v17 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(second_url))
    #     uid_v17 = common_v17.authenticate(second_db, second_username, second_password, {})
    #     models_v17 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(second_url))
    #     #
    #     # studio_fields_data_12 = models_v12.execute_kw(db, uid_v12, password,
    #     #                                            'sale.order', 'search_read',
    #     #                                            [[('id','=',20029)]],
    #     #                                            {'fields': ['name','x_studio_oci_sale_priceliste_enddate','x_studio_oci_saleorder_codetiers','x_studio_customer_vat','x_studio_oci_vente_langcustomer'],'limit': 30})
    #     studio_fields_data_12 = models_v12.execute_kw(
    #         db,
    #         uid_v12,
    #         password,
    #         'product.pricelist',
    #         'search_read',
    #         [[]],
    #         {'fields': ['name', 'x_studio_oci_pricelist_orderref', 'x_studio_x_studio_x_studio_offre_de_prix_annee',
    #                     'x_studio_oci_pricelist_alintentionde', '', 'x_studio_oci_datelifestart',
    #                     'x_studio_oci_datelifeend'], 'order': 'id asc', 'limit': 10}
    #     )
    #
    #     print('\n\n\n\nstudio_fields_data_12', studio_fields_data_12)
    #
    #     # Iterate over the fetched records
    #     for record in studio_fields_data_12:
    #         v12_id = record['id']
    #         name = record['name']
    #         pricelist_orderref = record.get('x_studio_oci_pricelist_orderref')
    #         offre_de_prix_annee = record.get('x_studio_x_studio_x_studio_offre_de_prix_annee')
    #         pricelist_alintentionde = record.get('x_studio_oci_pricelist_alintentionde')
    #         date_life_start = record.get('x_studio_oci_datelifestart')
    #         datelifeend = record.get('x_studio_oci_datelifeend')
    #         try:
    #             models_v17.execute_kw(second_db, uid_v17, second_password,
    #                                   'product.pricelist', 'write',
    #                                   [[v12_id],
    #                                    {
    #                                     'name': name,
    #                                     'pricelist_orderref': pricelist_orderref,
    #                                     'offre_de_prix_annee': offre_de_prix_annee,
    #                                     'pricelist_alintentionde': pricelist_alintentionde,
    #                                     'date_life_start': date_life_start,
    #                                     'datelifeend': datelifeend
    #                                    }
    #                                     ])
    #             print(f'Updated record in v17: ID={v12_id}, Name={name}')
    #         except Exception as e:
    #             print(f'Error updating record in v17 for ID={v12_id}: {e}')
    # #
    #     # studio_fields_data_12 = models_v12.execute_kw(db, uid_v12, password,
    #     #                                               'sale.order', 'search',
    #     #                                               [[]], order="id asc" )
    #     # studio_fields_data_17 = models_v17.execute_kw(second_db, uid_v17, second_password,
    #     #                                               'sale.order', 'search',
    #     #                                               [[('id','=',28)]],
    #     #                                               {'limit': 30})
    #
    #     # print('\n\n\nstudio_fields_data_12', studio_fields_data_12)
    #     # print('\n\n\nstudio_fields_data_17', len(studio_fields_data_17))
    #     # print('\n\n\n\nstudio_fields_data', studio_fields_data_12)
    #     # print('\n\n\n\nstudio_fields_data', len(studio_fields_data_12))
    #
    #     # for partner in studio_fields_data_12:
    #     #     name = partner.get('name')
    #     #     oci_saleorder_codetiers = partner.get('x_studio_oci_saleorder_codetiers')
    #     #     customer_vat = partner.get('x_studio_customer_vat')
    #     #     oci_vente_langcustomer = partner.get('x_studio_oci_vente_langcustomer')
    #     #     pricelist_enddate = partner.get('x_studio_oci_sale_priceliste_enddate')
    #     #
    #     #     if name:
    #     #         order_vals = {
    #     #             'oci_saleorder_codetiers': oci_saleorder_codetiers if oci_saleorder_codetiers is not None else '',
    #     #             'customer_vat': customer_vat if customer_vat is not None else '',
    #     #             'oci_vente_langcustomer': oci_vente_langcustomer if oci_vente_langcustomer is not None else '',
    #     #             'oci_sale_priceliste_enddate':pricelist_enddate if pricelist_enddate is not None else False
    #     #
    #     #         }
    #     #         print('\n\n\nUpdated fields in v17: ', order_vals)
    #     #
    #     #         try:
    #     #             models_v17.execute_kw(second_db, uid_v17, second_password,
    #     #                                   'sale.order', 'write',
    #     #                                   [studio_fields_data_17, order_vals])
    #     #         except Exception as e:
    #     #             print(f'Error creating partner {name}: {e}')
    #     #     else:
    #     #         print(f'Skipping partner with missing name: {partner}')
    #
    # # ===========================================================================================
    #
    # # def update_fields_data(self):
    # #     print('\n\n\n\ncron job running')
    # #
    # #     # Odoo v12 connection
    # #     url = "http://localhost:8011"
    # #     db = 'v12_2024_10_04'
    # #     username = 'admin'
    # #     password = 'admin'
    # #
    # #     # Odoo v17 connection
    # #     second_url = "http://localhost:8080"
    # #     second_db = 'injb_studio_v17_2'
    # #     second_username = 'admin'
    # #     second_password = 'admin'
    # #
    # #     # Connect to Odoo v12
    # #     common_v12 = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    # #     uid_v12 = common_v12.authenticate(db, username, password, {})
    # #     models_v12 = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    # #
    # #     # Connect to Odoo v17
    # #     common_v17 = xmlrpc.client.ServerProxy(f'{second_url}/xmlrpc/2/common')
    # #     uid_v17 = common_v17.authenticate(second_db, second_username, second_password, {})
    # #     models_v17 = xmlrpc.client.ServerProxy(f'{second_url}/xmlrpc/2/object')
    #
    # # Fetch char fields that are stored, not computed, manual state from Odoo v12
    # # v12_char_fields = models_v12.execute_kw(db, uid_v12, password, 'ir.model.fields', 'search_read', [[
    # #     ['model', '=', 'res.partner'],
    # #     ['ttype', '=', 'char'],
    # #     ['store', '=', True],
    # #     ['compute', '=', False],
    # #     ['state', '=', 'manual'],
    # # ]])
    # # fields = model.execute_kw(db, uid, password, 'ir.model.fields', 'search', [
    # #     [['state', '=', 'manual'], ["related", "=", False], ["compute", "=", False], ["store", "=", True],
    # #      ['ttype', '=', 'selection']]])
    # # print("fields================", len(fields))
    #
    # # print('\n\n\nv12_char_fields',v12_char_fields)
    # #
    # # for record in v12_char_fields:
    # #     print('\n\n\nrecord',record)
    #
    # # # Fetch char field details from Odoo v17
    # # v17_char_fields = models_v17.execute_kw(second_db, uid_v17, second_password, 'ir.model.fields', 'search_read', [
    # #     ('model', '=', 'sale.order'),
    # #     ('ttype', '=', 'char')
    # # ], {'fields': ['name']})
    # #
    # # # Create a dynamic mapping based on char fields
    # # field_mapping = {}
    # # for field in v12_char_fields:
    # #     old_field_name = field['name']
    # #
    # #     # Find matching field in v17
    # #     for new_field in v17_char_fields:
    # #         if old_field_name.lower() == new_field['name'].lower():
    # #             field_mapping[old_field_name] = new_field['name']
    # #
    # # # Fetch sale orders from v12
    # # sale_orders = models_v12.execute_kw(db, uid_v12, password, 'sale.order', 'search_read', [[]],
    # #                                     {'fields': list(field_mapping.keys())})
    # #
    # # for order in sale_orders:
    # #     order_vals = {}
    # #     for old_field, new_field in field_mapping.items():
    # #         order_vals[new_field] = order.get(old_field)
    # #
    # #     # Create the new sale order in v17
    # #     try:
    # #         models_v17.execute_kw(second_db, uid_v17, second_password, 'sale.order', 'create', [order_vals])
    # #         print(f'Created sale order with values: {order_vals}')
    # #     except Exception as e:
    # #         print(f'Error creating sale order: {e}')
    # #
    #
    # #     fields = models_v12.execute_kw(db, uid_v12, password, 'ir.model.fields', 'search', [
    # #         [['state', '=', 'manual'], ["related", "=", False], ["compute", "=", False], ["store", "=", True],
    # #          ['ttype', '=', 'char']]])
    # #     # print("fields================", (fields))
    # #     # print("fields================", len(fields))
    # #
    # #     for field_id in fields:
    # #         field_model_id = models_v12.execute_kw(db, uid_v12, password, 'ir.model.fields', 'search_read',
    # #                                                [[['id', '=', field_id]]],
    # #                                                {'fields': ['model_id', 'name']})
    # #         # print('\n\n\nfield_model_id',field_model_id)
    # #
    # #         model_id = field_model_id[0].get("model_id")[0]
    # #         field_name = field_model_id[0].get("name")
    # #         # print('\n\n\nfield_name',field_name)
    # #         model_name_list = models_v12.execute_kw(db, uid_v12, password, 'ir.model', 'search_read',
    # #                                                 [[['id', '=', model_id]]],
    # #                                                 {'fields': ['model']})
    # #         model_name = model_name_list[0].get("model")
    # #         all_recs = models_v12.execute_kw(db, uid_v12, password, model_name, 'search', [[]])
    # #         # print("\nall_recs===model_name====field_name===", len(all_recs), model_name, field_name)
    # #         model_field = models_v12.execute_kw(
    # #             db, uid_v12, password, model_name, "fields_get", [field_name]
    # #         )
    # #
    # #         # print('\n\n\n\n\nmodel_field', model_field)
    # #
    # #         count = 0
    # #         for record in all_recs:
    # #             field_type = model_field.get(field_name).get("type")
    # #     #         # print('\n\n\nfield_type',field_type)
    # #             if field_type == "char":
    # #                 updated_model_name = model_name.replace(".","_")
    # #     #             # print('\n\n\nupdated_model_name',updated_model_name)
    # #     #     #         if updated_model_name == 'stock_lot':
    # #     #     #             updated_model_name = 'stock_production_lot'
    # #                 if field_name in ['x_studio_numero_projet']:
    # #                     print('\n\n\n\n\nyes have field')
    # #         #
    # #                     cursor.execute(f"SELECT \"{field_name}\" FROM {updated_model_name} WHERE id=20095;")
    # #                     char_field_val = cursor.fetchone()
    # #                     print('\n\n\nchar_field_val',char_field_val)
    # #     #                 if isinstance(char_field_val, tuple):
    # #     #                     val = char_field_val[0]
    # #     #                 else:
    # #     #                     val = char_field_val
    # #     #         #
    # #     #                 if val:
    # #     #                     # val = False
    # #     #                     # print("char_field_val===============================",val, field_name, record, model_name)
    # #     #                     models_v17.execute_kw(second_db, uid_v17, second_password, model_name, 'write', [[record], {'field_name': val}])
    # #     #         #
    # #     #     # print("count+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",count)
    # #     #     count += 1
