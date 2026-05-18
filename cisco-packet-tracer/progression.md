# Cisco Packet Tracer — Progression
## Compte NetAcad créé · Packet Tracer installé · Mai 2026

---

## Lab 1 — Premier réseau LAN avec routeur
**Date :** 17 Mai 2026
**Statut :** Complété

### Topologie créée
1 routeur (Cisco 1941) · 1 switch (2960-24TT) · 3 PC

### Ce que j'ai fait
Création d'une topologie réseau avec un routeur, 
un switch et trois PC connectés. Configuration 
des adresses IP statiques sur les PC via l'interface 
graphique de Packet Tracer.

PC0 : 192.168.1.50 — Masque 255.255.255.0
Gateway : 192.168.1.254

### Problème rencontré et résolu
Le routeur ne communiquait pas avec le switch. 
En cherchant sur internet j'ai compris que les 
interfaces des routeurs Cisco sont désactivées 
par défaut pour des raisons de sécurité.

J'ai utilisé le CLI du routeur pour activer 
l'interface avec la commande :

Router>enable
Router#configure terminal
Router(config)#interface GigabitEthernet0/0
Router(config-if)#ip address 192.168.1.254 255.255.255.0
Router(config-if)#no shutdown

### Ce que j'ai appris
Sur un routeur Cisco, toutes les interfaces sont 
désactivées par défaut. La commande "no shutdown" 
permet de les activer manuellement. Sans cette 
commande, le routeur ne peut pas communiquer 
avec le reste du réseau.

### Ce qui reste à approfondir
Comprendre le rôle complet du routeur vs le switch.
Configurer les adresses IP directement en CLI.
Tester la connectivité avec la commande ping.

---