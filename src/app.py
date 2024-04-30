import base64
from dataclasses import asdict
import tempfile
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from html_service import HtmlService
from invoice_service import InvoiceService
from pdf_service import PdfService

html_service = HtmlService()
invoice_service = InvoiceService()
pdf_service = PdfService()


def lambda_handler(event, context):
    invoice = invoice_service.create()
    html = html_service.render_invoice(asdict(invoice))
    pdf = pdf_service.create_from_html(html)
    if pdf:
        pdf_base64 = base64.b64encode(pdf).decode("utf-8")
        print(pdf_base64)


lambda_handler(None, None)
