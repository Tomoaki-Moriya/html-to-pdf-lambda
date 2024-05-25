

from typing import Final


class PdfService:

    def __init__(self) -> None:
        # for testing
        from weasyprint import HTML
        self._HTML: Final = HTML

    def create_from_html(self, content: str) -> bytes:
        pdf = self._HTML(string=content,
                         encoding="utf-8").write_pdf()
        if not pdf:
            raise ValueError("PDF generation failed")
        return pdf
