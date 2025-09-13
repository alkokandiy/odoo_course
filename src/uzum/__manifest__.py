{
    'name': "Uzum Market",
    'version': '1.0',
    'summary': "E-commerce structure with customer, POS, dealer, and supplier",
    'description': """
        Uzum Market Module
        ==================
        - Manage products
        - Manage customers
        - POS orders with salespersons
        - Dealers and suppliers workflow
    """,
    'author': "Abubakr Al-Kokandiy",
    'website': "http://www.alkokandiy.com",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
