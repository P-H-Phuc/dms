/** @odoo-module **/

import { registerPatch } from "@mail/model/model_core";
import { attr } from '@mail/model/model_field';

registerPatch({
    name: "Attachment",
    fields: {
        defaultSource: {
            compute() {
                if (this.isMsOfficeDocument) {
                    if (this.model_name === 'dms.file') {
                        const encodedRoute = encodeURIComponent(`/dms/preview-msoffice/${this.id}`);
                        return encodedRoute;
                    }
                    return this._super();
                }
                return this._super();
            }
        },
    },
});
