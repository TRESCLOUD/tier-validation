# Copyright 2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Product State",
    "summary": """
        Module introducing a state field on product template""",
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/product-attribute",
    "category": "Product",
    "version": "1.0",
    "license": "AGPL-3",
    "maintainer": "Odoo Community Association (OCA)",
    "development_status": "Beta",
    "demo": [],
    "depends": ["product"],
    "data": [
        "data/product_state_data.xml",
        "security/product_state_security.xml",
        "security/ir.access.csv",
        "views/product_template_views.xml",
        "views/product_state_views.xml",
    ],
    "application": False,
    "maintainers": ["emagdalenaC2i"],
    "post_init_hook": "post_init_hook",
}
