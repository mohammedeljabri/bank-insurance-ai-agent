from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from tools import lire_pdf


# Connexion à Mistral local
llm = ChatOllama(model="mistral")

# Système bancaire
system_prompt = """Tu es un assistant bancaire expert. 
Tu analyses les contrats d'assurance et extrais les informations clés.
Tu réponds toujours en français de manière professionnelle et structurée."""


def analyser_contrat(texte: str) -> str:
    """Analyse un contrat et extrait les points clés"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=f"""
        Analyse ce contrat d'assurance et extrais :
        1. Type de contrat
        2. Garanties principales
        3. Exclusions importantes
        4. Montant de la prime
        5. Points de vigilance
        
        Contrat :
        {texte}
        """
        ),
    ]

    # Streaming — affiche token par token
    print("Analyse en cours...\n")
    resultat = ""
    for chunk in llm.stream(messages):
        print(chunk.content, end="", flush=True)
        resultat += chunk.content
    print("\n")
    return resultat


def analyser_pdf(chemin_pdf: str) -> str:
    """Analyse directement un fichier PDF"""
    print(f"Lecture du PDF : {chemin_pdf}")
    texte = lire_pdf(chemin_pdf)
    print(f"Texte extrait : {len(texte)} caractères\n")
    return analyser_contrat(texte)


if __name__ == "__main__":
    # Test avec un PDF réel
    resultat = analyser_pdf("data/contrats/contrat_assurance_habitation.pdf")
    print(resultat)
