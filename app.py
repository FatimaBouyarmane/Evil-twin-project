from flask import Flask, request, render_template, redirect, url_for
import joblib
import time
import csv

app = Flask(__name__)

# Chargement du modèle et des encodeurs
model = joblib.load("rf_model.pkl")
ua_encoder = joblib.load("ua_encoder.pkl")
target_encoder = joblib.load("target_encoder.pkl")

@app.route('/')
def index():
    # Démarrer le suivi de la session
    session_start = time.time()
    return render_template("login.html", session_start=session_start)

@app.route('/submit', methods=['POST'])
def submit():
    # Récupération des données du formulaire
    login = request.form.get("login", "")
    password = request.form.get("password", "")
    try:
        session_start = float(request.form.get("session_start", time.time()))
    except:
        session_start = time.time()
    session_duration = time.time() - session_start

    click_count = int(request.form.get("click_count", 1))

    # Récupération des headers
    ua = request.headers.get('User-Agent', '')

    # Encodage du User-Agent
    try:
        ua_encoded = ua_encoder.transform([ua])[0]
    except:
        ua_encoded = 0

    # Préparation des données pour la prédiction
    features = [[ua_encoded, session_duration, click_count]]

    # Prédiction
    prediction = model.predict(features)[0]
    device_type = target_encoder.inverse_transform([prediction])[0]

    # Sauvegarde dans le fichier CSV
    with open("logins.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([login, password, device_type, session_duration, click_count])

    # Redirection en fonction du type d'appareil
    if device_type.lower() == 'desktop':
        return redirect(url_for('desktop'))
    elif device_type.lower() == 'ios':
        return redirect(url_for('ios'))
    else:
        return "Type d'appareil non pris en charge."

@app.route('/desktop')
def desktop():
    return render_template("desktop.html")

@app.route('/ios')
def ios():
    return render_template("ios.html")

if __name__ == '__main__':
    app.run(debug=True)
