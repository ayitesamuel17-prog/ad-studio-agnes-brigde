from flask import Flask, request, jsonify
import random

app = Flask(__name__)


def make_concepts(data):
    product = data.get("product_name") or "ce produit"
    description = data.get("description") or "Un produit pensé pour votre quotidien."
    audience = data.get("audience") or "tout le monde"
    benefits = data.get("benefits") or "qualité, simplicité et efficacité"
    style = data.get("style") or "viral"
    hook_type = data.get("hook") or "question"

    hooks = {
        "question": f"Tu connais déjà {product} ? Attends de voir ça.",
        "problem": f"Tu rencontres encore ce problème ? Voici {product}.",
        "surprise": f"Personne ne s'attend à ça avec {product}.",
        "direct": f"Voici {product}. Découvre pourquoi il mérite ton attention."
    }

    styles = {
        "viral": "Rythme rapide, plans courts, énergie sociale et hook immédiat.",
        "premium": "Lumière élégante, mouvements lents, détails précis et rendu haut de gamme.",
        "emotion": "Storytelling humain, ambiance chaleureuse et connexion émotionnelle.",
        "dynamic": "Mouvements de caméra dynamiques, transitions rapides et énergie moderne."
    }

    hook = hooks.get(hook_type, hooks["question"])
    direction = styles.get(style, styles["viral"])

    templates = [
        {
            "title": "HOOK MAGNÉTIQUE",
            "type": "Viral",
            "script": (
                f"{hook} {product} est présenté comme une solution "
                f"simple et intéressante. {description} "
                f"Ses principaux avantages : {benefits}."
            ),
            "cta": "Découvre-le maintenant."
        },
        {
            "title": "PROBLÈME → SOLUTION",
            "type": "Conversion",
            "script": (
                f"Montre d'abord une situation qui concerne {audience}. "
                f"Puis présente {product} comme la solution. "
                f"{description} Les avantages : {benefits}."
            ),
            "cta": "Passe à l'action."
        },
        {
            "title": "STORYTELLING",
            "type": "Émotion",
            "script": (
                f"Une personne rencontre un besoin dans sa vie quotidienne. "
                f"Elle découvre {product}. {description} "
                f"Elle comprend alors ce qui le rend intéressant : {benefits}."
            ),
            "cta": "Découvre ton prochain indispensable."
        },
        {
            "title": "PREMIUM PRODUCT FILM",
            "type": "Premium",
            "script": (
                f"Présente {product} dans un environnement élégant. "
                f"Plans rapprochés, détails du produit, lumière maîtrisée "
                f"et mouvements cinématiques. {description}"
            ),
            "cta": "Découvrez l'expérience."
        },
        {
            "title": "FORMAT SOCIAL VIRAL",
            "type": "TikTok / Reels",
            "script": (
                f"POV : tu viens de découvrir {product}. "
                f"Montre immédiatement le produit, puis une démonstration "
                f"rapide. {description} Avantages : {benefits}."
            ),
            "cta": "Enregistre et découvre le produit."
        }
    ]

    concepts = []

    for item in templates:
        concepts.append({
            "title": item["title"],
            "type": item["type"],
            "hook": hook,
            "direction": direction,
            "script": item["script"],
            "scenes": [
                "Plan 1 — Hook immédiat.",
                "Plan 2 — Présentation du produit.",
                "Plan 3 — Démonstration ou utilisation.",
                "Plan 4 — Gros plan sur le produit.",
                "Plan 5 — Produit + appel à l'action."
            ],
            "cta": item["cta"]
        })

    random.shuffle(concepts)
    return concepts


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
}

body {
    margin: 0;
    background: #070707;
    color: white;
    font-family: Arial, sans-serif;
}

.app {
    max-width: 1100px;
    margin: auto;
    padding: 20px;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0 30px;
}

.logo {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: 3px;
}

.version {
    color: #999;
    font-size: 11px;
    border: 1px solid #333;
    border-radius: 20px;
    padding: 7px 10px;
}

.hero {
    padding: 20px 0 35px;
}

.hero h1 {
    font-size: clamp(40px, 8vw, 75px);
    line-height: .9;
    margin: 0;
    letter-spacing: -4px;
}

.hero p {
    color: #999;
    max-width: 650px;
    line-height: 1.6;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
}

.card {
    background: #111;
    border: 1px solid #292929;
    border-radius: 20px;
    padding: 20px;
}

.full {
    grid-column: 1 / -1;
}

h2 {
    margin-top: 0;
    font-size: 18px;
}

.small {
    color: #888;
    font-size: 13px;
    line-height: 1.5;
}

label {
    display: block;
    margin-top: 16px;
    margin-bottom: 7px;
    color: #aaa;
    font-size: 12px;
}

input,
textarea,
select {
    width: 100%;
    background: #191919;
    color: white;
    border: 1px solid #333;
    border-radius: 12px;
    padding: 13px;
    outline: none;
}

textarea {
    min-height: 95px;
    resize: vertical;
}

input:focus,
textarea:focus,
select:focus {
    border-color: white;
}

.upload {
    margin-top: 18px;
    min-height: 190px;
    border: 2px dashed #333;
    border-radius: 17px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
    cursor: pointer;
}

.upload:hover {
    border-color: white;
}

.upload-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

#file {
    display: none;
}

#preview {
    display: none;
    width: 100%;
    max-height: 300px;
    object-fit: contain;
    margin-top: 15px;
    border-radius: 15px;
    background: #050505;
}

.options {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9px;
}

.option {
    background: #181818;
    border: 1px solid #303030;
    padding: 14px;
    border-radius: 13px;
    cursor: pointer;
}

.option.active {
    border-color: white;
    background: #242424;
}

.option strong {
    display: block;
}

.option span {
    display: block;
    margin-top: 5px;
    color: #888;
    font-size: 11px;
}

.primary {
    width: 100%;
    border: 0;
    background: white;
    color: black;
    font-weight: 900;
    padding: 17px;
    border-radius: 14px;
    cursor: pointer;
    margin-top: 20px;
}

.primary:hover {
    background: #ddd;
}

.results {
    margin-top: 0;
}

.concept {
    border: 1px solid #303030;
    background: #151515;
    border-radius: 17px;
    padding: 18px;
    margin-top: 12px;
}

.concept-title {
    display: flex;
    justify-content: space-between;
    gap: 10px;
}

.badge {
    color: #aaa;
    border: 1px solid #333;
    border-radius: 20px;
    padding: 5px 9px;
    font-size: 10px;
    white-space: nowrap;
}

.hook {
    margin-top: 15px;
    font-weight: bold;
}

.label {
    color: #777;
    text-transform: uppercase;
    font-size: 10px;
    letter-spacing: 1px;
    margin-top: 15px;
    margin-bottom: 6px;
}

.scene {
    background: #1d1d1d;
    padding: 9px;
    border-radius: 9px;
    margin-top: 5px;
    color: #bbb;
    font-size: 12px;
}

.prompt {
    background: #080808;
    border: 1px solid #292929;
    padding: 12px;
    border-radius: 10px;
    color: #aaa;
    font-size: 12px;
    white-space: pre-wrap;
}

@media(max-width: 750px) {
    .grid {
        grid-template-columns: 1fr;
    }

    .full {
        grid-column: auto;
    }

    .options {
        grid-template-columns: 1fr;
    }
}
</style>
</head>

<body>

<div class="app">

<header>
    <div class="logo">AD STUDIO</div>
    <div class="version">V19</div>
</header>

<section class="hero">
    <h1>FROM PRODUCT<br>TO AD.</h1>
    <p>
        Transforme un produit en concepts publicitaires
        prêts à être développés pour TikTok, Instagram,
        WhatsApp et autres réseaux.
    </p>
</section>

<div class="grid">

<section class="card">

<h2>01 — PRODUCT</h2>

<div class="small">
Importe ton produit et décris-le.
</div>

<label class="upload" for="file">
    <div class="upload-icon">＋</div>
    <strong>Importer une photo</strong>
    <span class="small">JPG · PNG · WEBP</span>
</label>

<input id="file" type="file" accept="image/*">

<img id="preview">

<label>Nom du produit</label>
<input id="product" placeholder="Ex : Oroma">

<label>Description</label>
<textarea id="description"
placeholder="Décris ton produit..."></textarea>

<label>Public cible</label>
<input id="audience"
placeholder="Ex : étudiants, familles, travailleurs...">

<label>Avantages</label>
<textarea id="benefits"
placeholder="Ex : naturel, frais, local, abordable..."></textarea>

</section>


<section class="card">

<h2>02 — CREATIVE BRAIN</h2>

<div class="small">
Choisis la direction créative.
</div>

<label>Style publicitaire</label>

<div class="options" id="styles">

<div class="option active" data-value="viral">
<strong>🔥 Viral</strong>
<span>Rapide et accrocheur</span>
</div>

<div class="option" data-value="premium">
<strong>💎 Premium</strong>
<span>Élégant et haut de gamme</span>
</div>

<div class="option" data-value="emotion">
<strong>❤️ Émotion</strong>
<span>Storytelling humain</span>
</div>

<div class="option" data-value="dynamic">
<strong>⚡ Dynamique</strong>
<span>Énergique et moderne</span>
</div>

</div>

<label>Type de Hook</label>

<div class="options" id="hooks">

<div class="option active" data-value="question">
<strong>Question</strong>
<span>Curiosité immédiate</span>
</div>

<div class="option" data-value="problem">
<strong>Problème</strong>
<span>Problème → solution</span>
</div>

<div class="option" data-value="surprise">
<strong>Surprise</strong>
<span>Effet inattendu</span>
</div>

<div class="option" data-value="direct">
<strong>Direct</strong>
<span>Produit immédiatement</span>
</div>

</div>

<label>Plateforme</label>

<select id="platform">
<option>TikTok</option>
<option>Instagram Reels</option>
<option>WhatsApp</option>
<option>YouTube Shorts</option>
</select>

<label>Format</label>

<select id="format">
<option>9:16 — Vertical</option>
<option>1:1 — Carré</option>
<option>16:9 — Horizontal</option>
</select>

<label>Durée</label>

<select id="duration">
<option>5 secondes</option>
<option>8 secondes</option>
<option>10 secondes</option>
<option>15 secondes</option>
</select>

<button class="primary" onclick="generate()">
✨ GÉNÉRER 5 PUBLICITÉS
</button>

</section>


<section class="card full">

<h2>03 — CREATIVE OUTPUT</h2>

<div id="results">
    <div class="small">
    Tes 5 concepts publicitaires apparaîtront ici.
    </div>
</div>

</section>

</div>

</div>


<script>

let selectedStyle = "viral";
let selectedHook = "question";


document.getElementById("file").addEventListener(
    "change",
    function() {

        const file = this.files[0];

        if (!file) {
            return;
        }

        const preview =
            document.getElementById("preview");

        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }
);


document.querySelectorAll("#styles .option").forEach(
    function(option) {

        option.addEventListener(
            "click",
            function() {

                document.querySelectorAll(
                    "#styles .option"
                ).forEach(
                    function(item) {
                        item.classList.remove("active");
                    }
                );

                this.classList.add("active");
                selectedStyle = this.dataset.value;
            }
        );
    }
);


document.querySelectorAll("#hooks .option").forEach(
    function(option) {

        option.addEventListener(
            "click",
            function() {

                document.querySelectorAll(
                    "#hooks .option"
                ).forEach(
                    function(item) {
                        item.classList.remove("active");
                    }
                );

                this.classList.add("active");
                selectedHook = this.dataset.value;
            }
        );
    }
);


async function generate() {

    const product =
        document.getElementById("product").value;

    const description =
        document.getElementById("description").value;

    const audience =
        document.getElementById("audience").value;

    const benefits =
        document.getElementById("benefits").value;

    const platform =
        document.getElementById("platform").value;

    const format =
        document.getElementById("format").value;

    const duration =
        document.getElementById("duration").value;

    const results =
        document.getElementById("results");

    results.innerHTML =
        "<p>🧠 Creative Brain génère 5 concepts...</p>";

    try {

        const response = await fetch(
            "/api/generate",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    product_name: product,
                    description: description,
                    audience: audience,
                    benefits: benefits,
                    style: selectedStyle,
                    hook: selectedHook,
                    platform: platform,
                    format: format,
                    duration: duration
                })
            }
        );

        const data = await response.json();

        if (!data.success) {
            throw new Error(data.error);
        }

        results.innerHTML = "";

        data.concepts.forEach(
            function(item, index) {

                let scenes = "";

                item.scenes.forEach(
                    function(scene) {
                        scenes +=
                            "<div class='scene'>" +
                            scene +
                            "</div>";
                    }
                );

                const prompt =
                    "Create a " +
                    duration +
                    " advertising video in " +
                    format +
                    " format for " +
                    platform +
                    ".\\n\\n" +
                    "PRODUCT: " +
                    product +
                    "\\n\\n" +
                    "HOOK: " +
                    item.hook +
                    "\\n\\n" +
                    "VISUAL STYLE: " +
                    item.direction +
                    "\\n\\n" +
                    "SCRIPT: " +
                    item.script +
                    "\\n\\n" +
                    "IMPORTANT: Preserve the exact physical " +
                    "appearance of the reference product. " +
                    "Do not deform, redesign or invent it.";

                results.innerHTML +=
                    "<div class='concept'>" +

                    "<div class='concept-title'>" +
                    "<h3>" +
                    (index + 1) +
                    ". " +
                    item.title +
                    "</h3>" +
                    "<span class='badge'>" +
                    item.type +
                    "</span>" +
                    "</div>" +

                    "<div class='hook'>" +
                    item.hook +
                    "</div>" +

                    "<div class='label'>Direction</div>" +
                    "<div class='small'>" +
                    item.direction +
                    "</div>" +

                    "<div class='label'>Script</div>" +
                    "<div class='small'>" +
                    item.script +
                    "</div>" +

                    "<div class='label'>Scènes</div>" +
                    scenes +

                    "<div class='label'>CTA</div>" +
                    "<div class='small'>" +
                    item.cta +
                    "</div>" +

                    "<div class='label'>Prompt vidéo IA</div>" +
                    "<div class='prompt'>" +
                    prompt +
                    "</div>" +

                    "</div>";
            }
        );

    } catch (error) {

        results.innerHTML =
            "<p>Erreur : " +
            error.message +
            "</p>";
    }
}

</script>

</body>
</html>
"""


@app.route("/api/generate", methods=["POST"])
def generate():

    data = request.get_json() or {}

    concepts = make_concepts(data)

    return jsonify({
        "success": True,
        "concepts": concepts
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
