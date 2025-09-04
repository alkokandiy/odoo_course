{
    'name': 'Gun Dealership',
    'version': '1.0',
    'description': 'A module for managing gun dealerships',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/gun_views.xml',
        'views/customer_views.xml',
    ],
    'application': True,
}
