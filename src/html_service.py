from dataclasses import asdict
from typing import Final
from jinja2 import Environment, FileSystemLoader

from invoice_service import Invoice


def number_format(price: int) -> str:
    return "{:,}".format(price)


class HtmlService:
    def __init__(self):
        self._env: Final = Environment(loader=FileSystemLoader("./templates"))
        self._env.filters["number_format"] = number_format

    def render_invoice(self, invoice: Invoice) -> str:
        template = self._env.get_template("invoice.html")
        params = asdict(invoice)
        html = template.render(params)
        return html
