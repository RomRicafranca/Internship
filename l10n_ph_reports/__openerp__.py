# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Philippines - Accounting Reports',
    'version': '1.0',
    'author': 'Romulus Ricafranca',
    'category': 'Localization/Account Report',
    'description': """
Accounting reports for Philippines
================================
    """,
    'depends': [
        'l10n_ph'
    ],
    'data': [
        'account_financial_html_report.xml',
    ],
    'installable': True,
    'auto_install': True,
}
