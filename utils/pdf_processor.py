from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re

def process_pdf(pdf_path):
    # Extract title (first non-empty text on first page)
    title = ""
    outline = []
    
    # Regular expressions to identify headings
    h1_pattern = re.compile(r'^(chapter|section|part)\s+\d+|^[A-Z][A-Z\s]+$', re.IGNORECASE)
    h2_pattern = re.compile(r'^\d+\.\d+\s+.+$|^[A-Z][a-z\s]+:$')
    h3_pattern = re.compile(r'^\d+\.\d+\.\d+\s+.+$|^[a-z\s]+:$')
    
    for page_num, page_layout in enumerate(extract_pages(pdf_path), start=1):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text().strip()
                
                # Skip empty or very short texts
                if not text or len(text) < 3:
                    continue
                
                # Determine heading level
                level = None
                if h1_pattern.match(text):
                    level = "H1"
                elif h2_pattern.match(text):
                    level = "H2"
                elif h3_pattern.match(text):
                    level = "H3"
                
                # If we found a heading, add to outline
                if level:
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num
                    })
                
                # Set title if not set yet (first significant text)
                if not title and text:
                    title = text.split('\n')[0]
    
    return {
        "title": title,
        "outline": outline
    }