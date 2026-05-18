# Notes — Session 1 — 15 mai 2026
## Introduction to Cyber Security · Network Fundamentals · How The Web Works

---

## 1. La Cybersécurité — Vue d'ensemble

La cybersécurité se divise en deux grandes familles :

**Offensif** — tester et attaquer les systèmes pour trouver 
les failles avant les vrais attaquants. Les métiers : 
pentesteur, hacker éthique, red team.

**Défensif** — protéger, surveiller et répondre aux incidents. 
Les métiers : analyste SOC, administrateur sécurité, blue team.

---

## 2. Les Réseaux — Bases

Un **réseau** c'est un ensemble de machines connectées entre 
elles pour échanger des données.

**Internet** c'est un réseau de réseaux — des millions de 
réseaux locaux connectés entre eux à l'échelle mondiale.

Un **LAN** (Local Area Network) c'est un réseau local — 
par exemple toutes les machines connectées chez toi ou 
dans une entreprise.

Un **ISP** (Internet Service Provider) c'est ton fournisseur 
d'accès internet — Orange, Free, SFR. C'est lui qui te 
connecte à internet.

---

## 3. Les Adresses IP

Une **adresse IP** c'est l'identifiant unique d'une machine 
sur un réseau — comme une adresse postale pour les données.

**IPv4** — format classique en 4 nombres séparés par des points.
Exemple : 192.168.1.1
Limité à environ 4 milliards d'adresses.

**IPv6** — format plus récent en 8 groupes de 4 caractères 
hexadécimaux (chiffres 0-9 + lettres a-f).
Exemple : 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Créé car les adresses IPv4 commençaient à manquer.

---

## 4. Le DNS — Domain Name System

Le **DNS** c'est l'annuaire d'internet — il traduit un nom 
de domaine lisible (google.com) en adresse IP comprise 
par les machines (142.250.74.46).

**Les 3 types de serveurs DNS :**

**Recursive** — c'est le premier serveur contacté quand tu 
tapes une URL. Il fait les recherches pour toi et interroge 
les autres serveurs.

**Root** — le serveur racine. Il connaît les serveurs 
responsables de chaque extension (.com, .fr, .org).

**Authoritative** — le serveur final qui connaît l'adresse IP 
exacte du domaine recherché. C'est lui qui donne la réponse 
définitive.

**Les DNS Record Types — à approfondir**
Il existe plusieurs types d'enregistrements DNS selon 
ce qu'on cherche (adresse IP, mail, alias...). 
Ce point reste à clarifier lors d'une prochaine session.

---

## 5. HTTP et le Web

**HTTP** (HyperText Transfer Protocol) c'est le protocole 
qui permet la communication entre ton navigateur et 
un serveur web.

**Composition d'une URL :**
https://www.exemple.com/page?parametre=valeur
│       │               │    │
│       │               │    └─ Paramètres
│       │               └─ Chemin vers la ressource
│       └─ Nom de domaine
└─ Protocole (http ou https)

**Les codes de statut HTTP :**
- 200 — OK, la page existe et est renvoyée correctement
- 301 — Redirection permanente vers une autre URL
- 404 — Page introuvable
- 500 — Erreur serveur interne

**Les cookies — à approfondir**
Les cookies sont des petits fichiers stockés par le navigateur
pour retenir des informations (session, préférences...).
Leur fonctionnement précis avec les headers HTTP reste 
à clarifier lors d'une prochaine session.

---

## 6. Le Modèle OSI — à approfondir

Le **modèle OSI** (Open Systems Interconnection) est un modèle 
en 7 couches qui décrit comment les données transitent 
sur un réseau. Notion identifiée, à étudier en détail 
lors d'une prochaine session.

---

## 7. Packets et Frames — à approfondir

Les données sur un réseau ne voyagent pas en un seul bloc — 
elles sont découpées en **packets** (paquets).
Un **frame** (trame) c'est l'unité de données au niveau 
de la liaison réseau.
Fonctionnement précis à approfondir lors d'une prochaine session.

---

## Points à revoir avant la prochaine session
- DNS Record Types — A, CNAME, MX, TXT... à quoi sert chacun ?
- Cookies et headers HTTP — fonctionnement précis
- Modèle OSI — les 7 couches
- Packets et frames — comment les données voyagent
- IPv6 — logique du format hexadécimal

---