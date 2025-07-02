# -*- coding: utf-8 -*-

import base64

from odoo import http
from odoo.http import request
from odoo.addons.web_preview_ms_office.controllers.main import OfficeConvertController


class DmsOfficeConvertController(OfficeConvertController):
    
    @http.route('/dms/preview-msoffice/<int:file_id>', auth='user')
    def dms_convert_pdf_attachment(self, file_id):
        DmsFile = request.env['dms.file'].sudo()
        file = DmsFile.browse(file_id)
        attachment = file.attachment_id
        if attachment.exists():
            return super().convert_pdf_attachment(attachment.id)
        
        else:
            try:
                attachment_bytes = file.content_binary
                if not isinstance(attachment_bytes, bytes):
                    attachment_bytes = base64.b64decode(file.content_file)
                pdf_data = request.env['converter.msoffice2pdf'].convert_msoffice2pdf(
                    binary_data=attachment_bytes,
                    filename=file.name
                )
                headers = [
                    ('Content-Type', 'application/pdf'),
                    ('Content-Disposition', f'inline; filename="{file.name}.pdf"'),
                    ('Content-Length', str(len(pdf_data)))
                ]
                return request.make_response(
                    pdf_data,
                    headers=headers
                )
            except Exception as e:
                return request.make_response(
                    f"Error previewing DMS file: {str(e)}",
                    headers=[('Content-Type', 'text/plain')]
                )
