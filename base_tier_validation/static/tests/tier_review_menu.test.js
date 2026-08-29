import {click, contains} from "@mail/../tests/mail_test_helpers_contains";
import {start} from "@mail/../tests/mail_test_helpers";
import {describe, test} from "@odoo/hoot";
import {onRpc} from "@web/../tests/web_test_helpers";

describe.current.tags("desktop");

test("tier review systray shows the pending count and opens the review group", async () => {
    onRpc("res.users", "review_user_count", () => [
        {
            id: 1,
            name: "Sale Order",
            model: "sale.order",
            active_field: true,
            icon: "/base_tier_validation/static/description/icon.png",
            type: "tier_review",
            pending_count: 3,
        },
    ]);
    await start();
    await click(".o_menu_systray i[aria-label='Reviews']");
    await contains(".o-mail-ActivityMenu-counter", {text: "3"});
    await contains(".o-mail-ActivityGroup", {text: "Sale Order"});
});
