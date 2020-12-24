from odoo import models,fields

class Person(models.Model):
	_name = "zakat.person"
	name = fields.Char(required=True)
	national_no = fields.Integer()
	phone = fields.Char(string="Mobile")
	birth_date = fields.Date()
	image = fields.Binary()
	address = fields.Text(help="Enter Your city")
	gender = fields.Selection(selection=[("male","Male"), ("female","Female")], default="male")
	is_deserve = fields.Boolean()
	orders = fields.One2many("zakat.order","person")
	masrif_type = fields.Many2many("zakat.type")
	salary = fields.Float()


class Order(models.Model):
	_name = "zakat.order"
	topic = fields.Text()
	date = fields.Date()
	money = fields.Float(readonly=True)
	time = fields.Datetime()
	description = fields.Html()
	person = fields.Many2one("zakat.person")

	_rec_name = "person"

class MType(models.Model):
	_name = "zakat.type"
	name = fields.Char()