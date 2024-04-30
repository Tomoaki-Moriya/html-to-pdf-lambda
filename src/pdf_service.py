
import base64
from weasyprint import HTML


class PdfService:

    def create_from_html(self, content: str, filepath: str | None = None) -> bytes | None:
        pdf = HTML(string=content, encoding="utf-8").write_pdf(target=filepath)
        return pdf
