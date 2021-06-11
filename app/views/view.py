from flask import Flask, render_template, redirect, url_for, request, abort
from app.controllers import UrunleriGetir, UrununOzellikleriniGetir
from app.models import Urun

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def Index():
    urunler = UrunleriGetir()
    return render_template("index.html", urunler = urunler)

@app.route("/", methods = ["GET", "POST"])
def UrununBilgileriniGoster():
    urunler = UrunleriGetir()
    secilenUrun = request.form.get("urunSecimi")
    urununOzellikleri = UrununOzellikleriniGetir(secilenUrun)
    return render_template("index.html", urununOzellikleri = urununOzellikleri, urunler = urunler)



if __name__ == "__main__":
    app.run(debug = True)