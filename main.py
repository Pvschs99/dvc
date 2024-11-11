import qrcode
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Sample digital card data with additional social media links
digital_card_data = {
    "name": "Parepalli Venkata Satya Chandra Shekar",
    "title": "CEO",
    "company": "Trinethra Solutions",
    "phone": "+917993516529",
    "email": "chandrashekarparepalli@gmail.com",
    "website": "https://trinethrasolutions.com",
    "whatsapp": "https://wa.me/7993516529",
    "instagram": "https://www.instagram.com/_pvschs_/profilecard/?igsh=ZGt6aGwydDN4Y2Nw",
    "linkedin": "https://www.linkedin.com/in/venkata-satya-chandra-shekar-parepalli-312b431b4/",
    "github": "https://github.com/Pvschs99/"
}

# Generate and save QR code for the digital card link
def generate_qr(data):
    qr = qrcode.make(data)
    qr.save("static/digital_card_qr.png")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route('/')
def display_card():
    return render_template('protfolio.html', card=digital_card_data)

@app.route('/about')
def aboutme():
    return render_template('aboutme.html', card=digital_card_data)

@app.route('/contact')
def contactinfo():
    return render_template('contactinfo.html', card=digital_card_data)

@app.route('/gallery')
def photo():
    return render_template('gallery.html', card=digital_card_data)

if __name__ == "__main__":
    generate_qr("http://192.168.29.36:5000/")  # Localhost link for development
    app.run(host="0.0.0.0", port=5000, debug=True)
