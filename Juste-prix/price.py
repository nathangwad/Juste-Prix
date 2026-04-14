import random

def nouvelle_partie(vies=5, max_val=100):
    """Initialise une nouvelle partie avec l'état complet du jeu."""
    return {
        'nombre': random.randint(1, max_val),
        'essaie': 0,
        'score': 2000,
        'limite_max': vies,
        'max_val': max_val,
        'historique': []
    }

def verifier_guess(guess, etat):
    """
    Vérifie la proposition du joueur et met à jour l'état du jeu.
    """
    etat['essaie'] += 1
    etat['score'] = max(0, etat['score'] - 100)
    restant = etat['limite_max'] - etat['essaie']
    n = etat['nombre']

    if guess == n:
        etat['historique'].append({'guess': guess, 'statut': 'gagne'})
        return {
            'message': f"Gagné en {etat['essaie']} essai(s) ! C'était {n}.",
            'fini': True,
            'gagne': True
        }

    elif etat['essaie'] >= etat['limite_max']:
        etat['historique'].append({'guess': guess, 'statut': 'perdu'})
        return {
            'message': f"Perdu ! La réponse était {n}.",
            'fini': True,
            'gagne': False
        }

    elif guess < n:
        etat['historique'].append({'guess': guess, 'statut': 'plus'})
        return {
            'message': f"C'est plus ! Il reste {restant} essai(s).",
            'fini': False,
            'gagne': False
        }

    else:
        etat['historique'].append({'guess': guess, 'statut': 'moins'})
        return {
            'message': f"C'est moins ! Il reste {restant} essai(s).",
            'fini': False,
            'gagne': False
        }