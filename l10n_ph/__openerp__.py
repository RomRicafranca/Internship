# -*- coding: utf-8 -*-

{
    'name': 'Philippines - Accounting',
    'version': '1.0',
	'author': 'Romulus Ricafranca',
    'category': 'Localization/Account Charts',
    'description': """
Philippine accounting chart and localization.
    """,
    'depends': ['base', 'account'],
    'demo': [ ],
    'data': [
             'l10n_ph_chart.xml',
			 'l10n_ph_chart_tax.xml',
             'account_chart_template.yml',
    ],
    'installable': True,
}