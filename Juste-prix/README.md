# Le Juste Prix 🎯

Un jeu de devinette web en Python / Flask. Trouve un nombre aléatoire en un minimum d'essais — avant d'épuiser toutes tes vies.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?style=flat-square)
![Licence](https://img.shields.io/badge/Licence-MIT-green?style=flat-square)

---

## Aperçu

| Écran de configuration | Écran de jeu |
|:---:|:---:|
| Choix du nombre de vies et de la plage | Saisie libre, historique et score en temps réel |

---

## Fonctionnalités

- **Configurable** : choix du nombre de vies (5 / 10 / 15) et de la plage (1–50, 1–100, 1–500, 1–1000).
- **Score dynamique** : commence à 2000 pts, perd 100 pts à chaque essai raté. Plancher à 0.
- **Record de session** : le meilleur score est conservé tant que le navigateur reste ouvert.
- **Historique des essais** : chaque proposition est listée avec sa direction (↑ trop petit / ↓ trop grand).
- **Validation des saisies** : protection contre les lettres, les nombres hors-plage et les sessions corrompues.
- **Design épuré** : interface noir & blanc, CSS séparé, aucune dépendance front-end.

---

## Prérequis

- Python 3.8+
- pip

---

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/<ton-pseudo>/juste-prix.git
cd juste-prix

# 2. (Recommandé) Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install flask
```

---

## Lancement

```bash
python route.py
```

Ouvre ensuite ton navigateur à l'adresse : **http://127.0.0.1:8080**

---

## Structure du projet

```
juste-prix/
├── route.py            # Application Flask : routes, sessions, logique HTTP
├── price.py            # Logique métier : nouvelle_partie(), verifier_guess()
├── static/
│   └── style.css       # Feuille de style (séparée du HTML)
├── templates/
│   └── index.html      # Interface Jinja2
└── README.md
```

---

## Comment jouer ?

1. Sélectionne ton nombre de **vies** et la **plage de nombres**.
2. Clique sur **Démarrer**.
3. Entre un nombre et clique sur **Proposer**.
4. Suis les indices : ↑ (trop petit) ou ↓ (trop grand).
5. Trouve le bon nombre avant d'épuiser tes vies !

> **Astuce** : utilise une recherche par dichotomie (toujours tester la valeur du milieu) pour maximiser ton score.

---

## Système de score

| Événement | Points |
|-----------|--------|
| Départ de partie | 2000 pts |
| Mauvais essai | −100 pts |
| Score plancher | 0 pt |

Un **record de session** est affiché en permanence. Bats ton propre score !

---

## Sécurité (avant de déployer)

La `secret_key` présente dans `route.py` est un placeholder. Avant tout déploiement :

```python
# route.py
import os
app.secret_key = os.environ.get('SECRET_KEY', 'change-moi')
```

Puis définis la variable d'environnement :

```bash
export SECRET_KEY="une-chaine-aleatoire-longue-et-secrete"
```

---

## Idées d'améliorations

- [ ] Leaderboard persistant (base de données SQLite)
- [ ] Mode multijoueur en temps réel (WebSockets)
- [ ] Niveau de difficulté "chrono" avec timer
- [ ] Internationalisation (i18n) EN / FR / ES

---

## Licence

MIT — libre d'utilisation, de modification et de distribution.