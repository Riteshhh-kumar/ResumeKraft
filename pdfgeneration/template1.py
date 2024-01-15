from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import  Paragraph,Table,TableStyle
from reportlab.platypus.paragraph import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER
from reportlab.lib import colors

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

styles = getSampleStyleSheet()
styles["Normal"].spaceBefore = 5
styles["Normal"].spaceAfter = 5


styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='SUB', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Centered', alignment=TA_CENTER))
styles.add(ParagraphStyle(name='CenteredName', alignment=TA_CENTER))
styles.add(ParagraphStyle(name='CenteredAddress', alignment=TA_CENTER))


styles["Justify"].spaceBefore = 3
styles["SUB"].spaceBefore = 3
styles["Justify"].spaceAfter = 3
styles["SUB"].spaceAfter = 3
styles["Centered"].spaceBefore = 7
styles["Centered"].spaceAfter = 3
styles["CenteredName"].spaceAfter = 7
styles["CenteredName"].spacebefor = 0

styles["Normal"].fontName = "Vera"
styles["Justify"].fontName = "Vera"
styles["Centered"].fontName = "VeraBd"
styles["SUB"].fontName = "VeraBd"
styles["CenteredName"].fontName = "VeraBd"
styles["CenteredAddress"].fontName = "VeraIt"

styles["Normal"].fontSize = 9
styles["Justify"].fontSize = 9
styles["Centered"].fontSize = 9
styles["SUB"].fontSize = 9
styles["CenteredName"].fontSize = 12


styles['Normal'].leftIndent = -20
styles['Normal'].rightIndent = -20

styles['SUB'].leftIndent = -15

styles['Justify'].leftIndent = -10
styles['Justify'].rightIndent = -20

styles['CenteredAddress'].leftIndent = -20
styles['CenteredAddress'].rightIndent = -20

a=40
def heading(string,canv):
    para = Paragraph(text='<para>'+string+'</para>',style=styles['CenteredName'])
    canv.append(para)
    return canv

def contactInfo(string,canv):
    para = Paragraph(text='<para>'+string+'</para>',style=styles['CenteredAddress'])
    canv.append(para)
    return canv

def sectionTitle(string,canv):
    para = Paragraph(text='<para>'+string+'</para>',style=styles['Centered'])
    canv.append(para)
    return canv

def sectionContent(string,canv):
    para = Paragraph(text='<para>'+string+'</para>',style=styles['Justify'])
    canv.append(para)
    return canv


def twoColumn(string1 , string2,canv):
    para = [['      '+string1,string2],]
    
    tbl = Table(para,colWidths=250)
    tblstyle = TableStyle([('FONT', (0, 0), (1, 0), 'Vera'),
                           ('FONTSIZE', (0, 0), (1, 0), 11),
                           ('ALIGN', (1, 0),(1, 0),'RIGHT'),
                           ('ALIGN', (0, 0), (0, 0), 'LEFT'),
])
    tbl.setStyle(tblstyle)
    canv.append(tbl)
    
    return canv

def subSection(string,canv):
    
    para = Paragraph(text='<para>'+string+'</para>',style=styles['SUB'])
    canv.append(para)
    return canv
    


def educationalInformation(school10,school12,score10,score12,ugcollege,ugcourse,ugscore,canv):
    global a
    canv = sectionContent(ugcollege,canv)
    a=50
    canv = twoColumn(ugcourse,ugscore+" CGPA",canv)
    a=40
    canv = sectionContent("High School",canv)
    a=50
    canv = twoColumn(school12,score12+"%",canv)
    a=40
    canv = sectionContent("Intermidiate",canv)
    a=50
    canv = twoColumn(school10,score10+"%",canv)
    a=40
    return canv