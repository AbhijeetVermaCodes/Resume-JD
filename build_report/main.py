import os
import sys

# Ensure root workspace is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors

from build_report.styles import (
    PAGE_WIDTH, PAGE_HEIGHT, MARGIN, USABLE_WIDTH, USABLE_HEIGHT,
    COLOR_PRIMARY, COLOR_MUTED, COLOR_TEXT, COLOR_BORDER,
    get_report_styles
)
from build_report.front_matter import (
    build_cover_page,
    build_certificate,
    build_declaration,
    build_acknowledgement,
    build_abstract,
    build_table_of_contents,
    build_list_of_figures_and_tables
)
from build_report.chapters_1_to_4 import (
    build_chapter_1,
    build_chapter_2,
    build_chapter_3,
    build_chapter_4
)
from build_report.chapters_5_to_7 import (
    build_chapter_5,
    build_chapter_6,
    build_chapter_7
)
from build_report.chapters_8_to_10 import (
    build_chapter_8,
    build_chapter_9,
    build_chapter_10
)
from build_report.chapters_11_to_13_and_appendix import (
    build_chapter_11,
    build_chapter_12,
    build_chapter_13,
    build_references,
    build_appendix
)

class AcademicReportCanvas(canvas.Canvas):
    """
    Two-pass canvas that:
    1. Collects all page states.
    2. Determines the transition point from front-matter (Roman numerals) to main-matter (Arabic numerals).
    3. Draws professional academic running headers, footers, thin rules, and page numbers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        # Find start of main matter (Chapter 1)
        # By standard layout, front matter is pages 1 through 8 (Cover = 1, Cert = 2, Decl = 3, Ack = 4, Abs = 5-6, TOC = 7, LOF/LOT = 8)
        # Main matter starts on page 9
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_academic_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_academic_decorations(self, total_pages):
        p_num = self._pageNumber
        self.saveState()

        # Cover Page (Page 1): Draw decorative border, NO running headers/footers
        if p_num == 1:
            # Academic Double Outer Border
            self.setStrokeColor(colors.HexColor('#1E3A8A'))
            self.setLineWidth(2.0)
            self.rect(36, 36, PAGE_WIDTH - 72, PAGE_HEIGHT - 72)
            self.setStrokeColor(colors.HexColor('#93C5FD'))
            self.setLineWidth(0.8)
            self.rect(40, 40, PAGE_WIDTH - 80, PAGE_HEIGHT - 80)
            self.restoreState()
            return

        # Determine Front Matter vs Main Matter
        # Let's say front matter is pages 2 to 8
        is_front_matter = (p_num <= 8)
        
        # Roman numerals map for front matter
        roman_numerals = {
            2: "ii", 3: "iii", 4: "iv", 5: "v", 6: "vi", 7: "vii", 8: "viii"
        }

        # Running Header
        self.setFont('Helvetica-Bold', 7.8)
        self.setFillColor(colors.HexColor('#1E3A8A'))
        self.drawString(MARGIN, PAGE_HEIGHT - 38, 'AI-POWERED CV AND JOB DESCRIPTION MATCHER')
        
        self.setFont('Helvetica', 7.5)
        self.setFillColor(colors.HexColor('#64748B'))
        self.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 38, 'Academic Software Project Report')
        
        # Header separator line
        self.setStrokeColor(colors.HexColor('#CBD5E1'))
        self.setLineWidth(0.6)
        self.line(MARGIN, PAGE_HEIGHT - 44, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 44)

        # Running Footer
        self.setStrokeColor(colors.HexColor('#CBD5E1'))
        self.setLineWidth(0.6)
        self.line(MARGIN, 44, PAGE_WIDTH - MARGIN, 44)

        self.setFont('Helvetica', 7.5)
        self.setFillColor(colors.HexColor('#64748B'))
        self.drawString(MARGIN, 32, 'Department of Computer Science & Engineering')
        
        self.setFont('Helvetica-Oblique', 7.0)
        self.drawCentredString(PAGE_WIDTH / 2, 32, 'Confidential — For Academic Evaluation Only')

        # Page Number String
        self.setFont('Helvetica-Bold', 7.8)
        self.setFillColor(colors.HexColor('#0F172A'))
        if is_front_matter:
            page_str = roman_numerals.get(p_num, str(p_num))
            self.drawRightString(PAGE_WIDTH - MARGIN, 32, f'Page {page_str}')
        else:
            main_page_num = p_num - 8
            total_main_pages = total_pages - 8
            self.drawRightString(PAGE_WIDTH - MARGIN, 32, f'Page {main_page_num} of {total_main_pages}')

        self.restoreState()


def assemble_story(styles, registry):
    story = []
    
    # 1. Front Matter
    story.extend(build_cover_page(styles))
    story.extend(build_certificate(styles, registry))
    story.extend(build_declaration(styles, registry))
    story.extend(build_acknowledgement(styles, registry))
    story.extend(build_abstract(styles, registry))
    story.extend(build_table_of_contents(styles, registry))
    story.extend(build_list_of_figures_and_tables(styles, registry))

    # 2. Main Chapters
    story.extend(build_chapter_1(styles, registry))
    story.extend(build_chapter_2(styles, registry))
    story.extend(build_chapter_3(styles, registry))
    story.extend(build_chapter_4(styles, registry))
    story.extend(build_chapter_5(styles, registry))
    story.extend(build_chapter_6(styles, registry))
    story.extend(build_chapter_7(styles, registry))
    story.extend(build_chapter_8(styles, registry))
    story.extend(build_chapter_9(styles, registry))
    story.extend(build_chapter_10(styles, registry))
    story.extend(build_chapter_11(styles, registry))
    story.extend(build_chapter_12(styles, registry))
    story.extend(build_chapter_13(styles, registry))
    
    # 3. References & Appendix
    story.extend(build_references(styles, registry))
    story.extend(build_appendix(styles, registry))
    
    return story


def generate_pdf(output_filename="AI_CV_JD_Matcher_Project_Report.pdf"):
    print("=== AI-Powered CV & JD Matcher: Academic Report Generator ===")
    styles = get_report_styles()
    registry = {}

    # --- PASS 1: Calculate exact page positions of all chapters, sections, tables, and figures ---
    print("\n[Pass 1] Measuring document flow and mapping page numbers...")
    pass1_doc = SimpleDocTemplate(
        "pass1_temp.pdf",
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN
    )
    pass1_story = assemble_story(styles, registry)
    pass1_doc.build(pass1_story, canvasmaker=AcademicReportCanvas)
    
    # Convert absolute pages in registry to chapter/main relative pages for TOC display
    main_start_page = registry.get('ch1', {}).get('page', 9)
    print(f"[Pass 1 Complete] Mapped {len(registry)} structural bookmarks. Main matter starts on page {main_start_page}.")
    
    # Adjust main matter pages in registry so TOC displays relative page starting at 1 for Chapter 1
    display_registry = {}
    for key, data in registry.items():
        raw_p = data['page']
        if key in ['cert', 'decl', 'ack', 'abstract', 'toc']:
            disp_p = raw_p  # Front matter uses Roman mapping in front_matter.py
        else:
            disp_p = max(1, raw_p - (main_start_page - 1))
        display_registry[key] = {
            'page': disp_p,
            'title': data.get('title', ''),
            'type': data.get('type', '')
        }

    # --- PASS 2: Generate Final Polished PDF with 100% accurate Table of Contents & References ---
    print(f"\n[Pass 2] Building final publication-grade academic report: '{output_filename}'...")
    final_doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN
    )
    final_story = assemble_story(styles, display_registry)
    final_doc.build(final_story, canvasmaker=AcademicReportCanvas)

    if os.path.exists("pass1_temp.pdf"):
        os.remove("pass1_temp.pdf")

    # Read page count of generated file
    import pypdf
    reader = pypdf.PdfReader(output_filename)
    page_count = len(reader.pages)
    print(f"\n SUCCESS! Academic Project Report successfully generated!")
    print(f" Output File: {os.path.abspath(output_filename)}")
    print(f" Total Pages: {page_count} pages (Target: 40–60 pages)")

if __name__ == '__main__':
    generate_pdf()
