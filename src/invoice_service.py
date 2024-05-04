from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    price: int
    quantity: int


@dataclass(frozen=True)
class Customer:
    name: str
    postal_code: str
    address: str


@dataclass(frozen=True)
class Company:
    name: str
    postal_code: str
    address: str
    invoice_number: int
    registration_number: str
    bank_name: str
    bank_branch_name: str
    bank_no: str


@dataclass(frozen=True)
class Invoice:
    issued_date: str
    customer: Customer
    company: Company
    items: list[Item]
    total: int


class InvoiceService:

    def get(self) -> Invoice:
        customer = Customer(
            name="株式会社サンプル",
            postal_code="123-4567",
            address="東京都新宿区1-2-3"
        )
        company = Company(
            name="株式会社PDF",
            postal_code="987-6543",
            address="大阪府大阪市4-5-6",
            invoice_number=123,
            registration_number="ABC123",
            bank_name="サンプル銀行",
            bank_branch_name="サンプル支店",
            bank_no="1234567"
        )
        items = [
            Item(name="サンプル商品1", price=1000, quantity=2),
            Item(name="サンプル商品2", price=2000, quantity=1)
        ]
        total = sum(item.price * item.quantity for item in items)
        return Invoice(
            issued_date="2024年4月1日",
            customer=customer,
            company=company,
            items=items,
            total=total
        )
