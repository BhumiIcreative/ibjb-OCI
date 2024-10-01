# boy_stock_picking

**Table of Contents**

* Usage
* Dependencies
* Issues & Bugs
* Development

---

## Usage

* The BOY Stock Picking module enhances stock picking by adding fields 
  for actual lot ID, lot expiration date, and lot count.

---

## Dependencies

### Odoo modules dependencies
| Module          | Technical Name | Why Used?                             |
|-----------------|----------------|---------------------------------------|
| stock           | stock          | Provides core stock management functionalities. |
| product_expiry   | product_expiry  | Manages product expiration dates and related features. |

### Python library dependenci

* This module doesn't have any python dependencies

---

## Limitations, Issues & Bugs

* This module doesn't have any limitations, issues & bugs

---

## Development

- Inherited the 'stock.move' model by adding a new field called "Life date","Lot count" and "lot".
- Defined '_get_life_date' method for  Computes the 'life_date' field based on the 'expiration_date' of the associated 'lot_id'.
- Defined '_get_lot_id' method for Computes the lot_id field based on associated move lines.
- Defined '_cpt_lot_count' method for  Computes the lot_count field based on the lot count from the associated move lines.