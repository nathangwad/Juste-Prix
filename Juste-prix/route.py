from flask import Flask, render_template, request, session
from price import nouvelle_partie, verifier_guess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        # --- Démarrer une nouvelle partie configurée ---
        if 'configurer' in request.form:
            try:
                vies = int(request.form.get('vies', 5))
                max_val = int(request.form.get('max_val', 100))
            except ValueError:
                return render_template('index.html', afficher_config=True, erreur="Paramètres invalides.")

            session['etat'] = nouvelle_partie(vies, max_val)
            return render_template(
                'index.html',
                message=f'Devine un nombre entre 1 et {max_val} !',
                fini=False,
                etat=session['etat'],
                meilleur_score=session.get('meilleur_score', None)
            )

        elif 'rejouer' in request.form:
            session.pop('etat', None)
            return render_template(
                'index.html',
                afficher_config=True,
                meilleur_score=session.get('meilleur_score', None)
            )

        elif 'guess' in request.form:
            if 'etat' not in session:
                return render_template('index.html', afficher_config=True)

            try:
                guess = int(request.form['guess'])
            except ValueError:
                return render_template(
                    'index.html',
                    message='Entrez un nombre valide !',
                    fini=False,
                    etat=session.get('etat'),
                    meilleur_score=session.get('meilleur_score', None)
                )

            etat = session['etat']

            if not (1 <= guess <= etat['max_val']):
                return render_template(
                    'index.html',
                    message=f'Entrez un nombre entre 1 et {etat["max_val"]} !',
                    fini=False,
                    etat=etat,
                    meilleur_score=session.get('meilleur_score', None)
                )

            resultat = verifier_guess(guess, etat)
            session['etat'] = etat
            session.modified = True

            if resultat['fini'] and resultat['gagne']:
                meilleur = session.get('meilleur_score', None)
                if meilleur is None or etat['score'] > meilleur:
                    session['meilleur_score'] = etat['score']

            return render_template(
                'index.html',
                message=resultat['message'],
                fini=resultat['fini'],
                gagne=resultat.get('gagne', False),
                etat=etat,
                meilleur_score=session.get('meilleur_score', None)
            )

    # --- Requête GET ---
    if 'etat' not in session:
        return render_template(
            'index.html',
            afficher_config=True,
            meilleur_score=session.get('meilleur_score', None)
        )

    return render_template(
        'index.html',
        message='Trouve le bon nombre !',
        fini=False,
        etat=session['etat'],
        meilleur_score=session.get('meilleur_score', None)
    )

if __name__ == '__main__':
    app.run(debug=True, port=8080)
