{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Simple School Module',
    'sequence': -100,
    'description': """Manage schools and students""",
    'category': 'Education',
    'author': 'Thomas',
    'website': 'http://localhost',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
