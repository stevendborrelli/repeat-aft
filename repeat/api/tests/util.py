from . import util

class PDFToTextTests(django.test.TestCase):

    def test_pdf_to_text(self):
        self.assertEqual("", util.pdf_to_text("TODO"))
