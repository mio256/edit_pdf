import sys
import pypdf

if len(sys.argv) != 3:
    print('Usage: python split.py <file path> <number of pages to split>')
    sys.exit()

path = sys.argv[1]
page = sys.argv[2]

merger = pypdf.PdfMerger()
merger.append(path, pages=pypdf.PageRange(':{}'.format(page)))
merger.write(path.replace('.pdf', '_split1.pdf'))
merger.close()

merger = pypdf.PdfMerger()
merger.append(path, pages=pypdf.PageRange('{}:'.format(page)))
merger.write(path.replace('.pdf', '_split2.pdf'))
merger.close()
