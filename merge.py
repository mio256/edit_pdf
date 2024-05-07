import sys
import pypdf

if len(sys.argv) < 3:
    print('Usage: python merge.py <file1> <file2> ... <fileN>')
    sys.exit()

merger = pypdf.PdfWriter()

for i in range(1, len(sys.argv)):
    if not sys.argv[i].endswith('.pdf'):
        print('All files must be PDF files')
        sys.exit()
    merger.append(sys.argv[i])

merger.write(sys.argv[1].replace('.pdf', '_merged.pdf'))
merger.close()
