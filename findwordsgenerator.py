import wsfunkcje
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def def_size(w):
    matrix = [[" " for x in range(w)] for i in range(w)]
    return matrix


def words_generator(input, output, int):
    print(input, output, int)
    matrix = def_size(int)
    list_of_words = wsfunkcje.ipmort_from_txt(input)

    wsfunkcje.select_word(list_of_words, matrix)
    wsfunkcje.printMatrix(matrix)

    # zapisywanie wylosowanej tabeli do PDFa
    doc = SimpleDocTemplate(output)
    elements = []
    styles = getSampleStyleSheet()
    t = Table(matrix)
    para = Paragraph(str(', '.join(list_of_words)), style=styles["Normal"])
    elements.append(t)
    elements.append(para)
    doc.build(elements)
