{
    'name': 'Online Food Store',
    'summary': 'Manage products in an online food store',
    'sequence': -100,
    'description': """Manage online food store products""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/food_product_views.xml',
        'views/food_product_menus.xml',
    ],
    'installable': True,
    'application': True,}
