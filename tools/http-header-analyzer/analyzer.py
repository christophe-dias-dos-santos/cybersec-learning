# analyzer.py
import requests
import sys

# Dictionnaire des headers de sécurité à vérifier
# Pour chaque header : description + pourquoi c'est important
HEADERS_SECURITE = {
    "Strict-Transport-Security": {
        "description": "Force le navigateur à utiliser HTTPS",
        "importance": "CRITIQUE"
    },
    "Content-Security-Policy": {
        "description": "Contrôle les ressources que le navigateur peut charger",
        "importance": "HAUTE"
    },
    "X-Frame-Options": {
        "description": "Empêche le site d'être intégré dans un iframe (protection clickjacking)",
        "importance": "HAUTE"
    },
    "X-Content-Type-Options": {
        "description": "Empêche le navigateur de deviner le type MIME",
        "importance": "MOYENNE"
    },
    "Referrer-Policy": {
        "description": "Contrôle les informations envoyées dans l'en-tête Referer",
        "importance": "MOYENNE"
    },
    "Permissions-Policy": {
        "description": "Contrôle l'accès aux APIs du navigateur (caméra, micro, etc.)",
        "importance": "MOYENNE"
    },
    "X-XSS-Protection": {
        "description": "Filtre XSS dans les anciens navigateurs",
        "importance": "FAIBLE"
    },
    "Server": {
        "description": "Révèle le logiciel serveur (peut exposer des infos sensibles)",
        "importance": "INFO"
    },
}


def analyser_headers(url):
    # Ajoute https:// si l'URL ne commence pas par http
    if not url.startswith("http"):
        url = "https://" + url

    print(f"\n{'='*60}")
    print(f"  Analyse de : {url}")
    print(f"{'='*60}\n")

    try:
        # On fait une requête GET avec un timeout de 10 secondes
        # verify=True = on vérifie le certificat SSL
        reponse = requests.get(url, timeout=10, verify=True)
        headers_recus = reponse.headers

        print(f"  Code HTTP    : {reponse.status_code}")
        print(f"  Protocole    : {'HTTPS' if url.startswith('https') else 'HTTP'}\n")

    except requests.exceptions.SSLError:
        print("  ERREUR : Certificat SSL invalide ou expiré")
        return
    except requests.exceptions.ConnectionError:
        print("  ERREUR : Impossible de se connecter au serveur")
        return
    except requests.exceptions.Timeout:
        print("  ERREUR : Le serveur met trop de temps à répondre")
        return

    presents = []
    absents = []

    # On parcourt chaque header de sécurité qu'on veut vérifier
    for header, infos in HEADERS_SECURITE.items():
        if header.lower() in [h.lower() for h in headers_recus]:
            # Récupère la valeur réelle du header (insensible à la casse)
            valeur = headers_recus.get(header, "")
            presents.append((header, valeur, infos))
        else:
            absents.append((header, infos))

    # Affichage des headers PRÉSENTS
    print(f"  ✅ HEADERS PRÉSENTS ({len(presents)})")
    print(f"  {'-'*56}")
    for header, valeur, infos in presents:
        print(f"  [{infos['importance']}] {header}")
        print(f"      → {infos['description']}")
        # On tronque la valeur si elle est trop longue
        if len(valeur) > 80:
            valeur = valeur[:77] + "..."
        print(f"      Valeur : {valeur}\n")

    # Affichage des headers ABSENTS
    print(f"\n  ❌ HEADERS ABSENTS ({len(absents)})")
    print(f"  {'-'*56}")
    for header, infos in absents:
        print(f"  [{infos['importance']}] {header}")
        print(f"      → {infos['description']}\n")

    # Score de sécurité basique (on ignore "Server" et "X-XSS-Protection")
    headers_importants = [
        h for h in HEADERS_SECURITE
        if HEADERS_SECURITE[h]["importance"] not in ["INFO", "FAIBLE"]
    ]
    headers_presents_importants = [
        h for h, _, _ in presents
        if HEADERS_SECURITE[h]["importance"] not in ["INFO", "FAIBLE"]
    ]
    score = len(headers_presents_importants) / len(headers_importants) * 100

    print(f"{'='*60}")
    print(f"  Score de sécurité : {score:.0f}% ({len(headers_presents_importants)}/{len(headers_importants)} headers critiques présents)")
    print(f"{'='*60}\n")


def main():
    # Si l'utilisateur passe une URL en argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        # Sinon on la demande en interactif
        url = input("Entrez l'URL à analyser (ex: google.com) : ").strip()

    analyser_headers(url)


if __name__ == "__main__":
    main()