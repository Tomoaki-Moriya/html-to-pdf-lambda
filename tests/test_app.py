
import base64
from unittest.mock import MagicMock
from pytest_mock import MockFixture

from invoice_service import Company, Customer, Invoice, Item


def test_lambda_handler(mocker: MockFixture):
    invoice = Invoice(
        issued_date="2021-01-01",
        customer=Customer(
            name="ABC Customer",
            postal_code="123-4567",
            address="1-2-3, Tokyo"
        ),
        company=Company(
            name="XYZ Company",
            postal_code="987-6543",
            address="4-5-6, Osaka",
            invoice_number=123,
            registration_number="ABC123",
            bank_name="Sample Bank",
            bank_branch_name="Sample Branch",
            bank_no="1234567"
        ),
        items=[
            Item(name="Item 1", price=100, quantity=2),
            Item(name="Item 2", price=200, quantity=1)
        ],
        total=1000
    )

    invoice_service_mock = MagicMock()
    invoice_service_mock.get.return_value = invoice
    mocker.patch(
        "invoice_service.InvoiceService.__new__", return_value=invoice_service_mock)

    html_service_mock = MagicMock()
    html_service_mock.render_invoice.return_value = "<html></html>"
    mocker.patch(
        "html_service.HtmlService.__new__", return_value=html_service_mock)

    pdf_service_mock = MagicMock()
    pdf_service_mock.create_from_html.return_value = b"pdf"
    mocker.patch(
        "pdf_service.PdfService.__new__", return_value=pdf_service_mock)

    from app import lambda_handler

    event = {}
    context = {}

    actual = lambda_handler(event, context)

    expected = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/pdf",
            "Content-Disposition": "attachment; filename=invoice.pdf"
        },
        "body": base64.b64encode(b"pdf").decode("utf-8"),
        "isBase64Encoded": True
    }

    assert expected == actual

    invoice_service_mock.get.assert_called_once()

    html_service_mock.render_invoice.assert_called_once_with(invoice)

    pdf_service_mock.create_from_html.assert_called_once_with("<html></html>")
