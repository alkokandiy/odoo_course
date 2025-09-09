# __manifest__.py
{
    'name': 'Gun Dealership',
    'version': '1.0',
    'summary': 'Manage guns, dealers, and killer customers',
    'description': "Buy guns from Continental, sell to John Wick & Co.",
    'author': 'Abubakr Siddiq al-Kokandiy',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/gun_views.xml',
        'views/dealer_views.xml',
        'views/customer_views.xml',
        'views/menus.xml',
    ],

    'application': True,
}
