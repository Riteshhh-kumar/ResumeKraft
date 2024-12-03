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

styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='SUB', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Centered', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='CenteredName', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='CenteredAddress', alignment=TA_JUSTIFY))


styles["Justify"].spaceBefore = 0
styles["SUB"].spaceBefore = 0
styles["Justify"].spaceAfter = 0
styles["SUB"].spaceAfter = 0
styles["Centered"].spaceBefore = 7
styles["Centered"].spaceAfter = 5
styles["CenteredName"].spaceAfter = 15
styles["CenteredName"].spacebefor = 0

styles["Justify"].fontName = "Vera"
styles["Centered"].fontName = "VeraBd"
styles["SUB"].fontName = "VeraBd"
styles["CenteredName"].fontName = "VeraBd"
styles["CenteredAddress"].fontName = "VeraIt"

styles["Justify"].fontSize = 9
styles["Centered"].fontSize = 10
styles["SUB"].fontSize = 9
styles["CenteredName"].fontSize = 22


styles['SUB'].leftIndent = -15
styles['Centered'].leftIndent = -20
styles['CenteredAddress'].leftIndent = -20
styles['CenteredName'].leftIndent = -20

styles['Justify'].leftIndent = -10
styles['Justify'].rightIndent = -20
styles['Centered'].textColor = colors.blue
styles['CenteredName'].textColor = colors.blue


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
    line = [['']]
    
    tbl = Table(line,colWidths=494,rowHeights=0,spaceAfter=3)
    tblstyle = TableStyle([('BOX', (0,0), (-1,-1), 0.25, colors.black),
])
    tbl.setStyle(tblstyle)
    canv.append(para)
    canv.append(tbl)
    return canv

def sectionContent(string,canv):
    para = Paragraph(text='<para>'+string+'</para>',style=styles['Justify'])
    canv.append(para)
    return canv


def twoColumn(string1 , string2,canv):
    para = [['   '+string1,string2],]
    
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