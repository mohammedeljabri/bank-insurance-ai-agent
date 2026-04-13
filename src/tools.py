import pdfplumber


def lire_pdf(chemin: str) -> str:
    """Extrait le texte d'un contrat PDF"""
    texte = ""
    with pdfplumber.open(chemin) as pdf:
        for page in pdf.pages:
            texte += page.extract_text() or ""
    return texte
