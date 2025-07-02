# -*- coding: utf-8 -*-

{
    'name': 'DMS Preview MS Office',
    'version': '16.0.1.0.0',
    'description': 'DMS Preview MS Office Documents in Odoo',
    'summary': 'DMS Preview MS Office Documents in Odoo',
    'category': 'Tools',
    'website': 'https://github.com/OCA/dms',
    'maintainer': 'Phan Hong Phuc',
    'author': 'Phan Hong Phuc',
    'license': 'LGPL-3',
    'depends': ['web_preview_ms_office', 'dms'],
    'assets': {
        'web.assets_backend': [
            'dms_preview_ms_office/static/src/js/attachment.js',
        ],
    },
    'installable': True,
    'application': False,
    'images': ['static/description/icon.png'],
    'auto_install': False,
}
