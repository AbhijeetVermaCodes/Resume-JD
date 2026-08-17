import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Flowable, Spacer

# Page Geometry
PAGE_WIDTH, PAGE_HEIGHT = A4  # 595.27 x 841.89 pt
MARGIN = 54.0  # 0.75 in
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN  # 487.27 pt
USABLE_HEIGHT = PAGE_HEIGHT - 2 * MARGIN  # 733.89 pt

# Academic Color Palette
COLOR_PRIMARY = colors.HexColor('#1E3A8A')     # Deep Navy
COLOR_SECONDARY = colors.HexColor('#0F766E')   # Deep Teal
COLOR_ACCENT = colors.HexColor('#4338CA')      # Indigo
COLOR_DARK = colors.HexColor('#0F172A')        # Slate 900
COLOR_TEXT = colors.HexColor('#334155')        # Slate 700
COLOR_MUTED = colors.HexColor('#64748B')       # Slate 500
COLOR_LIGHT_BG = colors.HexColor('#F8FAFC')    # Slate 50
COLOR_CARD_BG = colors.HexColor('#F1F5F9')     # Slate 100
COLOR_BORDER = colors.HexColor('#CBD5E1')      # Slate 300
COLOR_BORDER_LIGHT = colors.HexColor('#E2E8F0')# Slate 200
COLOR_SUCCESS = colors.HexColor('#15803D')     # Green 700
COLOR_SUCCESS_BG = colors.HexColor('#DCFCE7')  # Green 100
COLOR_WARNING = colors.HexColor('#B45309')     # Amber 700
COLOR_WARNING_BG = colors.HexColor('#FEF3C7')  # Amber 100
COLOR_DANGER = colors.HexColor('#B91C1C')      # Red 700
COLOR_DANGER_BG = colors.HexColor('#FEE2E2')   # Red 100
COLOR_CODE_BG = colors.HexColor('#0F172A')     # Dark background for code
COLOR_CODE_TEXT = colors.HexColor('#F8FAFC')   # Light text for code

def get_report_styles():
    styles = getSampleStyleSheet()
    
    # Custom Paragraph Styles
    styles.add(ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=COLOR_PRIMARY,
        alignment=1,  # Center
        spaceAfter=12
    ))
    
    styles.add(ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=COLOR_MUTED,
        alignment=1,
        spaceAfter=24
    ))
    
    styles.add(ParagraphStyle(
        'CoverMetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=COLOR_DARK,
    ))
    
    styles.add(ParagraphStyle(
        'CoverMetaValue',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=COLOR_TEXT,
    ))

    styles.add(ParagraphStyle(
        'DocChapterTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=24,
        textColor=COLOR_PRIMARY,
        spaceBefore=14,
        spaceAfter=12,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'DocSectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=COLOR_ACCENT,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'DocSubsectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=COLOR_DARK,
        spaceBefore=9,
        spaceAfter=4,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.8,
        textColor=COLOR_TEXT,
        spaceAfter=6,
        alignment=4  # Justified
    ))

    styles.add(ParagraphStyle(
        'DocBodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.8,
        textColor=COLOR_DARK,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=13.2,
        textColor=COLOR_TEXT,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        'DocCalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.0,
        leading=13.0,
        textColor=COLOR_DARK
    ))

    styles.add(ParagraphStyle(
        'DocCalloutTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=COLOR_PRIMARY,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        'DocTableHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.white,
        alignment=0
    ))

    styles.add(ParagraphStyle(
        'DocTableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.3,
        leading=11.2,
        textColor=COLOR_TEXT,
        alignment=0
    ))

    styles.add(ParagraphStyle(
        'DocTableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.3,
        leading=11.2,
        textColor=COLOR_DARK,
        alignment=0
    ))

    styles.add(ParagraphStyle(
        'DocCodeBlock',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.6,
        leading=9.8,
        textColor=colors.HexColor('#E2E8F0')
    ))

    styles.add(ParagraphStyle(
        'DocCaption',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=COLOR_MUTED,
        alignment=1,  # Center
        spaceBefore=5,
        spaceAfter=9
    ))

    styles.add(ParagraphStyle(
        'TOCItem',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=14.0,
        textColor=COLOR_DARK
    ))

    styles.add(ParagraphStyle(
        'TOCChapter',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.8,
        leading=15.0,
        textColor=COLOR_PRIMARY
    ))

    return styles

class PageTracker(Flowable):
    """Flowable used to track exact target page numbers for TOC and figures."""
    def __init__(self, key, registry, title="", item_type="section"):
        super().__init__()
        self.key = key
        self.registry = registry
        self.title = title
        self.item_type = item_type
        self.width = 0
        self.height = 0

    def wrap(self, availWidth, availHeight):
        return 0, 0

    def draw(self):
        self.registry[self.key] = {
            'page': self.canv._pageNumber,
            'title': self.title,
            'type': self.item_type
        }

def make_callout(title, text, styles, alert_type="info"):
    """Generates a styled academic callout box."""
    if alert_type == "info":
        bg_color = colors.HexColor('#EFF6FF')
        border_color = colors.HexColor('#3B82F6')
        title_color = colors.HexColor('#1D4ED8')
        icon = "[INFO]"
    elif alert_type == "warning":
        bg_color = COLOR_WARNING_BG
        border_color = COLOR_WARNING
        title_color = colors.HexColor('#92400E')
        icon = "[IMPORTANT NOTE]"
    elif alert_type == "danger":
        bg_color = COLOR_DANGER_BG
        border_color = COLOR_DANGER
        title_color = colors.HexColor('#991B1B')
        icon = "[CRITICAL DISCLAIMER]"
    elif alert_type == "success":
        bg_color = COLOR_SUCCESS_BG
        border_color = COLOR_SUCCESS
        title_color = colors.HexColor('#166534')
        icon = "[KEY PRINCIPLE]"
    else:
        bg_color = COLOR_CARD_BG
        border_color = COLOR_BORDER
        title_color = COLOR_PRIMARY
        icon = "[NOTE]"

    t_style = ParagraphStyle(
        'CalloutT',
        parent=styles['DocCalloutTitle'],
        textColor=title_color
    )
    
    content = [
        Paragraph(f"<b>{icon} {title}</b>", t_style),
        Spacer(1, 2),
        Paragraph(text, styles['DocCalloutText'])
    ]
    
    t = Table([[content]], colWidths=[USABLE_WIDTH])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('BOX', (0,0), (-1,-1), 0.5, border_color),
        ('LINEBEFORE', (0,0), (0,-1), 3.5, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

def make_code_box(code_text, filename, styles):
    """Creates a beautifully styled code listing box with header banner."""
    header_content = Paragraph(f"<b>Listing File:</b> <font name='Courier-Bold'>{filename}</font>", styles['DocTableHead'])
    header_table = Table([[header_content]], colWidths=[USABLE_WIDTH])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E293B')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))

    code_lines = []
    lines = code_text.strip().split('\n')
    for idx, line in enumerate(lines, start=1):
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;')
        code_lines.append(f"<font color='#64748B'>{idx:3d} | </font>{escaped_line}")
    
    code_para = Paragraph("<br/>".join(code_lines), styles['DocCodeBlock'])
    
    body_table = Table([[code_para]], colWidths=[USABLE_WIDTH])
    body_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_CODE_BG),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#334155')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    
    return Table([[header_table], [body_table]], colWidths=[USABLE_WIDTH], style=[
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1E293B')),
    ])
