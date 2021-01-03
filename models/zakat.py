from odoo import models,fields, api
from odoo.exceptions import UserError

class Person(models.Model):
	_name = "zakat.person"
	name = fields.Char(required=True, string="الاسم")
	national_no = fields.Integer()
	phone = fields.Char(string="mobile")
	brith_date = fields.Date()
	image = fields.Binary()
	address = fields.Text(help="Enter city ")
	gender = fields.Selection(selection=[("male","Male"),("famel","Fmale")], default="male")
	is_deserve = fields.Boolean()
	state = fields.Selection(selection=[("draft","Draft"),("submit","Submit"),("confirm","Confirm"),("cancel","Cancel")], default="draft")
	orders  = fields.One2many("zakat.oreder", "person")
	# mtype = fields.Many2many("zakat.type")
	salary = fields.Float(string="المرتب")
	masrif_type = fields.Many2many("zakat.type")
	salary = fields.Float()
	@api.model
	def create(self, vals):
		if 'name' in vals and len(vals['name']) < 10 or len(vals['name']) > 15:
			raise UserError('Name length must be > 10 and < 15')
		new_record_id = super(Person, self).create(vals)
		return new_record_id

	# def write(self, vals):
	# 	if 'name' in vals and len(vals['name']) < 10 or len(vals['name']) > 15:
	# 		raise UserError('Name length must be > 10 and < 15')
	# 	super(Person, self).write(vals)
	# 	return True

	def submit(self):
		self.state = "submit"

	def confirm(self):
		self.is_deserve = True
		self.state = 'confirm'
	# @api.multi
	# def unlink(self):
	# 	if 'name' in vals and len(vals['name']) < 10:
	# 		raise UserError('Name is deleted')
	# 	super(Person, self).write(vals)
	# 	return True

class Order(models.Model):
	_name = "zakat.oreder"
	# person = fields.Char()
	topic = fields.Text()
	date = fields.Date()
	money = fields.Float(readonly=True)
	descripttion = fields.Html()
	person = fields.Many2one("zakat.person")

class Mtype(models.Model):
	_name = "zakat.type"
	name  = fields.Char()

class Employee (models.Model):
	_inherit = "hr.employee"

	desc = fields.Text("Descripion", required=True)
