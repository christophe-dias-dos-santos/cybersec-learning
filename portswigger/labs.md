# PortSwigger Web Security Academy — Labs
## portswigger.net · Créé par les auteurs de Burp Suite

---

## 📊 Progression globale
1 lab complété — Mai 2026

---

## ✅ Lab 1 — Path Traversal
**Catégorie : File Path Traversal**
**Statut : Complété**
**Outil utilisé : Burp Suite**

### Ce qu'est le Path Traversal
Le path traversal est une vulnérabilité web qui permet 
à un attaquant de manipuler un chemin de fichier dans 
une requête HTTP pour accéder à des fichiers sensibles 
qui ne devraient pas être accessibles.

Exemple concret, au lieu de demander :
/images/photo.jpg

On manipule le chemin pour remonter dans l'arborescence :
/../../../etc/passwd

Et on accède ainsi à des fichiers système sensibles 
comme les mots de passe.

### Comment j'ai résolu ce lab
L'objectif était d'accéder au fichier de mots de passe 
du serveur en manipulant le chemin d'une image dans 
la requête HTTP via Burp Suite.

J'ai intercepté la requête avec Burp Suite et modifié 
le paramètre du chemin de fichier pour remonter dans 
l'arborescence du serveur et accéder au fichier cible.

### Ce qui était intuitif
La logique de remonter dans l'arborescence des dossiers 
était intuitive, c'est le même principe que naviguer 
dans un système de fichiers Linux avec des chemins 
relatifs comme ../ pour remonter d'un niveau.

### Ce qui reste flou
La section Raw de Burp Suite — je vois les headers 
et le corps de la requête HTTP mais je ne comprends 
pas encore tout ce que j'y lis. Cela deviendra plus clair 
après avoir terminer le module "How The Web Works" sur TryHackMe.

### Lien avec OWASP Top 10
Le Path Traversal fait partie de la catégorie 
"Broken Access Control", la vulnérabilité numéro 1 
de l'OWASP Top 10 2021.

---

## 📝 Labs à venir
- SQL Injection
- Cross-Site Scripting (XSS)
- Authentication vulnerabilities
- Business logic vulnerabilities

---