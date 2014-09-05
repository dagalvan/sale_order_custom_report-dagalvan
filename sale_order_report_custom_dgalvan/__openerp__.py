# -*- encoding utf-8 -*-

{
	'name':"sale_order_report_custom_dgalvan",
	'category':"Report",
	'version':"1.0",
	'depends':['base'],
	'author':"Daniel",
	
	'description':"""\
Generate a sale report that show:
----------------------------------------
	*Information
		Name and addres by the company
		Name and addres by the client
		Date
	
	
	*Products information
		Name
		Quantity
		Unitary price
		Tax
		Total price
	
	*Costs
		Subtotal
		Tax
		Total
		Salesman
		Web Company
	
	""",
	
	'data':['report/sale_order_report_custom_dgalvan.xml',
			'report/sale_order_report_custom.xml',
	
		],
	'depends':['base',
			
	],
	'installable':True,
}
