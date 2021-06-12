{ 
    'name': 'Service', 
    'description': 'Manage your personal tasks.', 
    'author': 'Joaquin Suarez', 
    'depends': ['base'], 
    'data': [
        'service_view.xml',
        'service_type_view.xml',
        'security.xml'
        ],
    'installable':True,
    'application': True, 
}