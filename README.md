# RegenWise Technical Test: Irrigation Smart-Pipeline 💧

Bienvenue dans l'évaluation technique de RegenWise !

Ce repository contient un prototype de notre **Smart Irrigation Engine**. Notre mission est de transformer le désert en zones vertes en optimisant chaque goutte d'eau. Ce pipeline traite les données de capteurs au sol pour calculer les besoins précis en irrigation.

## 🎯 La Mission

Le code actuel est fonctionnel mais a été écrit dans l'urgence. Il respecte une **architecture en 3 couches** (Entities → Logic/Use Cases → Infrastructure) mais contient plusieurs défauts de conception, des goulots d'étranglement de performance et des bugs de logique métier.

Ta mission est d'améliorer ce pipeline pour le rendre **scalable et fiable**.

### Attentes :
1.  **Qualité du code & Structure** : Respecte l'architecture en 3 couches. Refactorise si nécessaire.
2.  **Logique & Correction de Bugs** : Identifie et corrige les erreurs de logique (vérifie les données et les tests).
3.  **Scalabilité** : L'implémentation actuelle est séquentielle. Propose ou implémente des améliorations pour gérer des millions de relevés.
4.  **Nouvelle Fonctionnalité** : Implémente un agrégat pour fournir le **besoin total en eau par jour et par Localisation** (les métadonnées des Noeuds contiennent la localisation).
5.  **Tests** : Améliore la suite de tests pour couvrir les cas aux limites.

## 🧠 Usage de l'IA

Chez RegenWise, l'IA est une alliée. **L'usage de Copilot, ChatGPT, Claude, etc., est autorisé et encouragé.**

Cependant, tu restes le "Pilote" :
- Explique dans un fichier `FEEDBACK.md` comment tu as utilisé l'IA.
- Quelles suggestions as-tu acceptées ? Quelles ont été rejetées et pourquoi ?
- Comment as-tu vérifié le code généré ?

## 🛠 Setup

### Prérequis
- Python 3.10+
- `make`

### Installation
```bash
make install
```

### Lancer le pipeline
```bash
make run
```

### Lancer les tests
```bash
make test
```
