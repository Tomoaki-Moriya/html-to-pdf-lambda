import base64

from html_service import HtmlService
from invoice_service import InvoiceService
from pdf_service import PdfService

html_service = HtmlService()
invoice_service = InvoiceService()
pdf_service = PdfService()


def lambda_handler(event, context):
    invoice = invoice_service.get()
    html = html_service.render_invoice(invoice)
    pdf = pdf_service.create_from_html(html)
    pdf_base64 = base64.b64encode(pdf).decode("utf-8")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/pdf",
            "Content-Disposition": "attachment; filename=invoice.pdf"
        },
        "body": pdf_base64,
        "isBase64Encoded": True
    }
