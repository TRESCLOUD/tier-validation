# Copyright 2025 Spearhead - Ricardo Jara
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Payment Tier Validation",
    "summary": "Extends the functionality of Payment to "
    "support a tier validation process.",
    "version": "1.0",
    "category": "Generic Modules/Payment",
    "website": "https://github.com/OCA/account-payment",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "maintainer": "Odoo Community Association (OCA)",
    "development_status": "Beta",
    "demo": [],
    "application": False,
    "installable": True,
    "depends": ["account", "base_tier_validation"],
    "data": ["views/account_payment_view.xml"],
}
