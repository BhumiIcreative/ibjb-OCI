# boy_sale_order

**Table of Contents**

* Usage
* Dependencies
* Issues & Bugs
* Development

---

## Usage

* The BOY Sale Order module adds fields for lot ID, lot expiration date, 
  and lot count to enhance stock picking processes.
---

## Dependencies

### Odoo modules dependencies
| Module            | Technical Name    | Why Used?                             |
|-------------------|-------------------|---------------------------------------|
| base              | base              | Provides core Odoo functionalities and models. 
| sale              | sale              | Manages sales orders and related processes.
| boy_company       | boy_comapny       | Provides RCS,Fax and legal form related fields.
| delivery          | delivery          | Manage products expiration date related process.
| boy_stock_picking | boy_stock_picking | Provides lot ,lot count and life date of products.
| l10n_fr           | l10n_fr           | Provides configurations for French VAT rates and tax rules.


### Python library dependenci

* This module doesn't have any python dependencies

---

## Limitations, Issues & Bugs

* This module doesn't have any limitations, issues & bugs

---

## Development

- Inherited the 'sale.order.line' model by adding a new field called "Life date","Lot count" and "lot".
- Inherited the 'sale.order' model by adding a new fields 'Delivery Methods' and 'Purchase order reference'
- Inherited the 'base.document.layout' by adding a new fields 'Fax','RCS' and 'legal form'.
- Customized sale order report by adding a new fields 'Lot' and 'PEREMPTION' in order lines.
- Customized sale order report by adding new table including new fields 'Order Reference','Date','Purchase order reference','Date EXP','CUSTOMER CODE' and 'CARRIER'
- Defined '_get_life_date' method for  Computes the 'life_date' field based on the 'expiration_date' of the associated 'lot_id'.
- Defined '_get_lot_id' method for Computes the lot_id field based on associated move lines.
- Defined '_cpt_lot_count' method for  Computes the lot_count field based on the lot count from the associated move lines.

---
