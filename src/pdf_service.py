
from weasyprint import HTML


class PdfService:

    def create_from_html(self, content: str) -> bytes:
        pdf = HTML(string=content,
                   encoding="utf-8").write_pdf()
        if not pdf:
            raise ValueError("PDF generation failed")
        return pdf
