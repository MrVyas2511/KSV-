from odoo import api,models,fields
from datetime import date
class OutwardRegister(models.Model):
    _name = "outward.register"
    _description = "Outward Register"
    
    # Fields Outward registrer contains
    # Date | Serial No | Full Name | Address | Place | Description | Stamp Recieved | Stamp Affixed | Balance  | Remark  

    name = fields.Char(compute="_compute_name")
    serial_no = fields.Char('Serial Number', required=True)
    date = fields.Date('Date',default=fields.Date.context_today, required=True)
    month = fields.Char('month', compute="_compute_month", store=True)
    full_name = fields.Char('Full Name', required=True)
    address = fields.Char('Address')
    place = fields.Char('Place')
    description = fields.Char('Subject')
    stamp_received = fields.Char('Stamp Received')
    stamp_affixed = fields.Char('Stamp Affixed')
    balance = fields.Char('Balance')
    remark = fields.Char('Remark')
    body = fields.Html('body', default="""
        <p><strong><span class="h6-fs">સંદર્ભ</span></strong><span class="h6-fs">: માસ ડીસ-2023 નું પગાર બિલ</span></p><p><strong><span class="h6-fs">મે. સાહેબશ્રી,</span></strong></p><p><br></p><div class="container o_text_columns"><div class="row"><div class="col-3"><p><strong><span class="h6-fs">બીજક</span></strong><span class="h6-fs">:</span></p><p><br></p></div><div class="col-3"><p><strong><span class="h4-fs"><span class="oe-tabs" style="width: 38.4px;">       </span></span><span class="h6-fs">​</span><span class="h4-fs"><span class="oe-tabs" style="width: 40px;">      </span></span><span class="h6-fs">​</span><span class="h4-fs"><span class="oe-tabs" style="width: 40px;">      </span></span><span class="h6-fs">​</span><span class="h4-fs"><span class="oe-tabs" style="width: 40px;">      </span></span></strong></p></div><div class="col-3"><p><br></p></div><div class="col-3"><p><strong><span class="h6-fs">​તમારા વિશ્વાસુ,</span></strong></p><p><br></p></div></div></div><p><br></p>
    """)

    attachment = fields.Binary("Attachment")

    @api.depends('date')
    def _compute_month(self):
        for rec in self:
            if rec.date:
                rec.month = rec.date.strftime("%B")

    def _compute_name(self):
        for rec in self:
            rec.name = rec.serial_no

    def action_print_letter(self):
        return self.env.ref('registers.outward_letter_report').report_action(self)

