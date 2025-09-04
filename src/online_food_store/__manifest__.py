{
    'name': 'Online Food Store',
    'description': """Manage online food store products""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/food_product_views.xml',
        'views/food_product_menus.xml',
    ],
    'installable': True,
    'application': True,}
