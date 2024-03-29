import sys
import pypdf

if len(sys.argv) != 2:
    print('Usage: python split_each.py <file path>')
    sys.exit()

path = sys.argv[1]


def split_pdf_pages(src_path, dst_basepath):
    src_pdf = pypdf.PdfReader(src_path)
    for i, page in enumerate(src_pdf.pages):
        dst_pdf = pypdf.PdfWriter()
        dst_pdf.add_page(page)
        dst_pdf.write(f'{dst_basepath}_{i}.pdf')


split_pdf_pages(path, path.replace('.pdf', '_split'))
