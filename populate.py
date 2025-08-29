# create products
import random
products = []
for i in range(500):
    p = self.env['product.product'].create({"name": f"test_{i}", "type": "consu", "is_storable": True, "list_price": random.randint(40,90)})
    products.append(p)

for product in products: 
    price = random.randint(10, 40)
    for i in (1, 10, 100):
        self.env['product.supplierinfo'].create({'product_id': product.id, "partner_id":15, "min_qty": i, "price": price})
        price *= .97


for product in products:
    self.env['stock.warehouse.orderpoint'].create({'product_id': product.id, "product_min_qty": random.randint(10,20), "product_max_qty": random.randint(30,50), "location_id": 8})


from odoo.fields import Command
purchase_vals = {"partner_id": 15, "order_line": []}
for product in products:
    purchase_vals["order_line"].append(Command.create({"name": product.name, "product_id": product.id, "product_qty": 15}))

self.env['purchase.order'].create(purchase_vals)

sale_vals = {"partner_id": 11, "order_line": [], "user_id": 2}
for product in products:
    sale_vals["order_line"].append(Command.create({"name": product.name, "product_id": product.id, "product_uom_qty": random.randint(10,40), "price_unit": random.randint(10,40)}))


self.env["sale.order"].create(sale_vals)
