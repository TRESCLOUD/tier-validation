# Copyright 2021 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ["product.template", "tier.validation"]
    _tier_validation_manual_config = False
    _state_to = ["sellable"]
    # product_state's header only has the statusbar field, no <button> to
    # anchor after (base_tier_validation's default xpath); anchor on the
    # last field instead so Request/Restart Validation still get injected.
    _tier_validation_buttons_xpath = "/form/header/field[last()]"

    def write(self, vals):
        # Tier Validation does not work with Stages, only States :-(
        # So, signal state transition by adding it to the vals
        if "product_state_id" in vals:
            stage_id = vals.get("product_state_id")
            stage = self.env["product.state"].browse(stage_id)
            vals["state"] = stage.code  # yes, "code" is used to represent a "state"
        res = super().write(vals)
        if "product_state_id" in vals:
            self.restart_validation()
        return res
