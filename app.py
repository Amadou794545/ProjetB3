from flask import Flask, render_template, request, redirect, url_for, flash, session
from ne_pas_ouvrir import Motdepasse
from ne_pas_ouvrir.serveur_socket import run_socket_server

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route('/', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if password == Motdepasse.P1:
            session['username'] = username
            return redirect(url_for('P2'))
        else:
            flash('Mot de passe incorrect. tu veux un indice?', 'danger')

    return render_template('P1.html')


# Scraping d'un site web
@app.route('/P2', methods=['GET', 'POST'])
def P2():
    if 'username' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', 'warning')
        return redirect(url_for(''))

    if request.method == 'POST':
        password = request.form['password']

        if password == Motdepasse.P2:
            return redirect(url_for('P3'))
        else:
            flash('code incorrect. tu veux un indice?', 'danger')

    return render_template('P2.html')


# se connecter à un serveur socket
@app.route('/P3', methods=['GET', 'POST'])
def P3():
    run_socket_server()
    if 'username' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', 'warning')
        return redirect(url_for(''))

    if request.method == 'POST':
        password = request.form['password']

        if password == Motdepasse.P3:
            return redirect(url_for('P4'))
        else:
            flash('code incorrect. tu veux un indice?', 'danger')

    return render_template('P3.html', username=session['username'])


# correlation
@app.route('/P4', methods=['GET', 'POST'])
def P4():
    if 'username' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', 'warning')
        return redirect(url_for(''))

    if request.method == 'POST':
        password = request.form['password']
        password2 = request.form['password2']
        password3 = request.form['password3']

        if password in Motdepasse.P4 and password2 in Motdepasse.P4 and password3 in Motdepasse.P4:
            return redirect(url_for('P5'))
        else:
            flash('code incorrect. tu veux un indice?', 'danger')

    return render_template('P4.html', username=session['username'])


# Modele de ML
from flask import redirect, url_for


@app.route('/P5', methods=['GET', 'POST'])
def P5():
    if 'username' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', 'warning')
        return redirect(url_for('login'))  # Redirige vers la page de connexion si non connecté

    if request.method == 'POST':
        password = request.form.get('password', '').strip()

        try:
            password_int = int(password)

            if Motdepasse.P5(password_int):  # Vérification avec votre fonction
                # Redirection vers le site Turbo
                return redirect(
                    "https://www.turbo.fr/audi/actualites-auto/audi-sport-quattro-600000-euros-pour-soffrir-cette-icone-des-annees-80-196995",
                    code=302)
            else:
                flash('Code incorrect. Tu veux un indice ?', 'danger')

        except ValueError:
            flash('Le mot de passe doit être un nombre valide.', 'danger')

    return render_template('P5.html', username=session.get('username'))


if __name__ == '__main__':
    app.run(debug=True)
