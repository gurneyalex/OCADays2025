from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_sales_count = fields.Integer(compute="_compute_product_sales_count")


    @api.depends("order_id.partner_id", "product_id", "product_uom_qty")
    def _compute_product_sales_count(self):
        for line in self:
            partner = line.order_id.partner_id
            product = line.product_id
            domain = [("order_id.partner_id", "=", partner.id), ("product_id", "=", product.id), ("order_id.state", "=", "sale")]
            if line.id:
                domain.append(("id", "!=", line.id))
            lines = self.env['sale.order.line'].search(domain)
            line.product_sales_count = sum(lines.mapped("product_uom_qty"))
