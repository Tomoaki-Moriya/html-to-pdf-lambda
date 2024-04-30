from dataclasses import asdict, dataclass
from typing import Any, Final, List
from jinja2 import Environment, FileSystemLoader


@dataclass(frozen=True)
class Item:
    name: str
    price: int


@dataclass(frozen=True)
class Company:
    name: str
    postal_code: str
    address: str
    corporate_number: str


@dataclass(frozen=True)
class InvoiceParams:
    title: str
    issue_date: str
    invoice_number: str
    item_list: List[Item]
    total: int
    bank_account: str
    company: Company


class HtmlService:
    def __init__(self):
        self._env: Final = Environment(loader=FileSystemLoader("./templates"))

    def render_invoice(self, params: dict[str, Any]) -> str:
        template = self._env.get_template("invoice.html")
        html = template.render(params)
        return html
