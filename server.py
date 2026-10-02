from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AD Studio</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: #080808;
    color: white;
    min-height: 100vh;
}

.container {
    width: 100%;
    max-width: 900px;
    margin: auto;
    padding: 24px 18px 50px;
}

.header {
    text-align: center;
    padding: 25px 0 35px;
}

.logo {
    font-size: 32px;
    font-weight: 900;
    letter-spacing: 3px;
}

.subtitle {
    margin-top: 8px;
    color: #999;
    font-size: 14px;
}

.card {
    background: #111;
    border: 1px solid #252525;
    border-radius: 22px;
    padding: 22px;
    margin-bottom: 20px;
}

.card h2 {
    font-size: 19px;
    margin-bottom: 8px;
}

.card p {
    color: #999;
    font-size: 13px;
    margin-bottom: 18px;
}

.upload {
    border: 2px dashed #444;
    border-radius: 18px;
    padding: 35px 15px;
    text-align: center;
    cursor: pointer;
}

.upload:hover {
    border-color: white;
}

.upload-icon {
    font-size: 38px;
    margin-bottom: 10px;
}

input[type="file"] {
    display: none;
}

.preview {
    display: none;
    width: 100%;
    max-height: 300px;
    object-fit: contain;
    border-radius: 15px;
    margin-top: 15px;
    background: #050505;
}

.options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.option {
    background: #181818;
    border: 1px solid #303030;
    border-radius: 15px;
    padding: 16px;
    cursor: pointer;
    transition: 0.2s;
}

.option:hover {
    border-color: white;
}

.option.active {
    border-color: white;
    background: #222;
}

.option strong {
    display: block;
    margin-bottom: 5px;
}

.option span {
    color: #999;
    font-size: 12px;
}

.generate {
    width: 100%;
    border: none;
    border-radius: 16px;
    padding: 17px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    background: white;
    color: black;
    margin-top: 10px;
}

.generate:active {
    transform: scale(0.98);
}

.results {
    display: none;
}

.ad {
    background: #181818;
    border: 1px solid #292929;
    border-radius: 18px;
    padding: 18px;
    margin-top: 12px;
}

.ad-number {
    font-size: 12px;
    color: #999;
    margin-bottom: 7px;
}

.ad h3 {
    margin-bottom: 7px;
}

.ad p {
    margin: 0;
}

@media (max-width: 600px) {
    .options {
        grid-template-columns: 1fr;
    }

    .logo {
        font-size: 27px;
    }
}
</style>
</head>

<body>

<div class="container">

    <div class="header">
        <div class="logo">AD STUDIO</div>
        <div class="subtitle">
            Transforme un produit en publicité.
        </div>
    </div>

    <div class="card">

        <h2>1. Ton produit</h2>

        <p>
            Importe une photo claire du produit que tu veux promouvoir.
        </p>

        <label class="upload" for="product">
            <div class="upload-icon">＋</div>
            <strong>Importer le produit</strong>
            <p>Photo JPG, PNG ou WEBP</p>
        </label>

        <input id="product" type="file" accept="image/*">

        <img id="preview" class="preview">

    </div>


    <div class="card">

        <h2>2. Style de publicité</h2>

        <p>Choisis l'ambiance de ta publicité.</p>

        <div class="options">

            <div class="option active">
                <strong>🔥 Viral</strong>
                <span>Accroche rapide pour les réseaux sociaux.</span>
            </div>

            <div class="option">
                <strong>💎 Premium</strong>
                <span>Élégant, propre et haut de gamme.</span>
            </div>

            <div class="option">
                <strong>❤️ Émotion</strong>
                <span>Une publicité basée sur l'histoire.</span>
            </div>

            <div class="option">
                <strong>⚡ Dynamique</strong>
                <span>Énergique et moderne.</span>
            </div>

        </div>

    </div>


    <div class="card">

        <h2>3. Ton Hook</h2>

        <p>La première phrase qui doit attirer l'attention.</p>

        <div class="options">

            <div class="option active">
                <strong>Question</strong>
                <span>« Vous cherchez quelque chose de différent ? »</span>
            </div>

            <div class="option">
                <strong>Problème</strong>
                <span>Présenter un problème puis la solution.</span>
            </div>

            <div class="option">
                <strong>Surprise</strong>
                <span>Créer immédiatement la curiosité.</span>
            </div>

            <div class="option">
                <strong>Direct</strong>
                <span>Présenter directement le produit.</span>
            </div>

        </div>

    </div>


    <div class="card">

        <button class="generate" onclick="generateAds()">
            ✨ Générer mes 5 publicités
        </button>

    </div>


    <div id="results" class="card results">

        <h2>Vos 5 concepts</h2>

        <div class="ad">
            <div class="ad-number">PUBLICITÉ 01</div>
            <h3>Le Hook puissant</h3>
            <p>Une introduction courte qui attire immédiatement l'attention.</p>
        </div>

        <div class="ad">
            <div class="ad-number">PUBLICITÉ 02</div>
            <h3>Le problème → solution</h3>
            <p>Montrer le besoin puis présenter naturellement le produit.</p>
        </div>

        <div class="ad">
            <div class="ad-number">PUBLICITÉ 03</div>
            <h3>Le storytelling</h3>
            <p>Une petite histoire autour du produit et de son utilisateur.</p>
        </div>

        <div class="ad">
            <div class="ad-number">PUBLICITÉ 04</div>
            <h3>Le produit premium</h3>
            <p>Une présentation visuelle élégante et professionnelle.</p>
        </div>

        <div class="ad">
            <div class="ad-number">PUBLICITÉ 05</div>
            <h3>Le format viral</h3>
            <p>Une publicité courte pensée pour TikTok, Instagram et WhatsApp.</p>
        </div>

    </div>

</div>


<script>

const input = document.getElementById("product");
const preview = document.getElementById("preview");

input.addEventListener("change", function() {

    const file = this.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }

});


document.querySelectorAll(".options").forEach(group => {

    group.querySelectorAll(".option").forEach(option => {

        option.addEventListener("click", function() {

            group.querySelectorAll(".option")
                .forEach(x => x.classList.remove("active"));

            this.classList.add("active");

        });

    });

});


function generateAds() {

    const results = document.getElementById("results");

    results.style.display = "block";

    results.scrollIntoView({
        behavior: "smooth"
    });

}

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
