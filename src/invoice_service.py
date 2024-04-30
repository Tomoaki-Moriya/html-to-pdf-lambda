from dataclasses import dataclass
from typing import List


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


class InvoiceService:

    def create(self) -> InvoiceParams:
        item1 = Item(name="商品A", price=1000)
        item2 = Item(name="商品B", price=2000)
        item3 = Item(name="商品C", price=3000)
        item_list = [item1, item2, item3]

        company = Company(
            name="株式会社サンプル",
            postal_code="100-0001",
            address="東京都千代田区千代田1-1-1",
            corporate_number="1234567890123"
        )

        invoice_params = InvoiceParams(
            title="請求書",
            issue_date="2021年8月1日",
            invoice_number="00001",
            item_list=item_list,
            total=6000,
            bank_account="1234567",
            company=company
        )

        return invoice_params
