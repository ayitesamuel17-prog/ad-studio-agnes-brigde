from flask import Flask, request, jsonify
import base64
import html
import json
import os
import random

app = Flask(__name__)


# ============================================================
# AD STUDIO V18.1
# REAL AGNES BRIDGE - FOUNDATION
# ============================================================

APP_NAME = "AD STUDIO"
VERSION = "V18.1"


# ============================================================
# HELPERS
# ============================================================

def esc(value):
    return html.escape(str(value or ""))


def make_hook(product, style):
    hooks = {
        "viral": [
            f"Tu connais déjà {product} ? Attends de voir ça.",
            f"Voici pourquoi tout le monde devrait découvrir {product}.",
            f"Et si {product} était exactement ce qu'il te fallait ?",
        ],
        "premium": [
            f"Découvrez {product} sous un autre regard.",
            f"L'élégance commence parfois avec {product}.",
            f"Une expérience pensée pour ceux qui exigent le meilleur.",
        ],
        "emotion": [
            f"Il y a des produits qu'on utilise. Et d'autres qu'on apprécie vraiment : {product}.",
            f"Parfois, le meilleur choix est aussi le plus simple.",
            f"Une petite chose peut changer toute une expérience.",
        ],
        "dynamic": [
            f"Stop. Regarde ce que {product} peut faire.",
            f"Nouveau jour, nouvelle énergie, nouveau {product}.",
            f"Rapide. Simple. Efficace. Voici {product}.",
        ],
    }

    return random.choice(hooks.get(style, hooks["viral"]))


def build_concepts(data):
    product = data.get("product_name") or "ce produit"
    description = data.get("description") or "Une solution pensée pour faciliter le quotidien."
    audience = data.get("audience") or "tout le monde"
    benefits = data.get("benefits") or "qualité, simplicité et efficacité"
    style = data.get("style") or "viral"

    concepts = [
        {
            "title": "HOOK MAGNÉTIQUE",
            "type": "Viral",
            "hook": make_hook(product, "viral"),
            "script": (
                f"Tu cherches quelque chose de simple et efficace ? "
                f"Découvre {product}. {description} "
                f"Pensé pour {audience}, avec comme principaux atouts : {benefits}. "
                f"Découvre-le dès maintenant."
            ),
            "scenes": [
                "Plan 1 — Gros plan dynamique sur le produit.",
                "Plan 2 — Présentation rapide du problème.",
                "Plan 3 — Le produit apparaît comme solution.",
                "Plan 4 — Démonstration / utilisation.",
                "Plan 5 — Produit + appel à l'action.",
            ],
            "voice": "Voix énergique, naturelle et confiante.",
            "cta": "Découvre-le maintenant."
        },
        {
            "title": "PROBLÈME → SOLUTION",
            "type": "Conversion",
            "hook": f"Tu rencontres encore ce problème ? Voici une solution.",
            "script": (
                f"Pendant longtemps, {audience} ont rencontré ce problème. "
                f"Voici {product}. {description} "
                f"Ses avantages : {benefits}. "
                f"Une solution simple, claire et accessible."
            ),
            "scenes": [
                "Plan 1 — Montrer le problème.",
                "Plan 2 — Expression de frustration.",
                "Plan 3 — Apparition du produit.",
                "Plan 4 — Utilisation du produit.",
                "Plan 5 — Résultat final + CTA.",
            ],
            "voice": "Voix persuasive, calme et rassurante.",
            "cta": "Passe à l'action."
        },
        {
            "title": "STORYTELLING",
            "type": "Émotion",
            "hook": "Tout commence par un petit besoin.",
            "script": (
                f"Une personne avait besoin d'une solution. "
                f"Elle découvre {product}. "
                f"En quelques instants, elle comprend ce qui le rend différent : "
                f"{benefits}. "
                f"C'est simple. C'est {product}."
            ),
            "scenes": [
                "Plan 1 — Situation quotidienne.",
                "Plan 2 — Le problème apparaît.",
                "Plan 3 — Découverte du produit.",
                "Plan 4 — Moment de satisfaction.",
                "Plan 5 — Plan final cinématique.",
            ],
            "voice": "Voix douce, émotionnelle et authentique.",
            "cta": "Découvre ton prochain indispensable."
        },
        {
            "title": "PREMIUM PRODUCT FILM",
            "type": "Premium",
            "hook": f"Voici {product}. Simplement remarquable.",
            "script": (
                f"Présentons {product} comme une expérience premium. "
                f"Lumière maîtrisée, détails précis, mouvements élégants. "
                f"{description} "
                f"Une attention particulière portée à chaque détail."
            ),
            "scenes": [
                "Plan 1 — Produit dans une lumière premium.",
                "Plan 2 — Macro sur les détails.",
                "Plan 3 — Rotation lente du produit.",
                "Plan 4 — Utilisation élégante.",
                "Plan 5 — Hero shot + logo + CTA.",
            ],
            "voice": "Voix premium, posée et profonde.",
            "cta": "Découvrez l'expérience."
        },
        {
            "title": "FORMAT SOCIAL VIRAL",
            "type": "TikTok / Reels",
            "hook": f"POV : tu viens de découvrir {product}.",
            "script": (
                f"POV : tu découvres {product} pour la première fois. "
                f"Tu comprends rapidement pourquoi il attire l'attention. "
                f"{description} "
                f"Et ses principaux avantages ? {benefits}. "
                f"Tu l'essaierais ?"
            ),
            "scenes": [
                "Plan 1 — Hook immédiat en moins de 2 secondes.",
                "Plan 2 — Produit très proche caméra.",
                "Plan 3 — Transition rapide.",
                "Plan 4 — Démonstration.",
                "Plan 5 — CTA avec mouvement caméra.",
            ],
            "voice": "Voix naturelle, jeune et spontanée.",
            "cta": "Enregistre cette vidéo et découvre le produit."
        },
    ]

    return concepts


# ============================================================
# MAIN PAGE
# ============================================================

@app.route("/")
def home():

    page = r"""
<!DOCTYPE html>
<html lang="fr">

<head>

<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>AD Studio V18.1</title>

<style>

:root {
    --bg: #070707;
    --panel: #101010;
    --panel2: #151515;
    --border: #292929;
    --text: #ffffff;
    --muted: #929292;
    --soft: #1e1e1e;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family:
        Inter,
        Arial,
        Helvetica,
        sans-serif;
}

button,
input,
textarea,
select {
    font: inherit;
}

button {
    cursor: pointer;
}

.app {
    width: 100%;
    max-width: 1180px;
    margin: auto;
    padding: 18px;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 4px 24px;
}

.brand {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: 3px;
}

.version {
    font-size: 11px;
    color: #888;
    border: 1px solid #292929;
    padding: 7px 10px;
    border-radius: 30px;
}

.hero {
    padding: 25px 0 30px;
}

.hero h1 {
    margin: 0;
    font-size: clamp(32px, 7vw, 65px);
    line-height: .95;
    letter-spacing: -3px;
}

.hero p {
    max-width: 650px;
    color: var(--muted);
    line-height: 1.6;
    margin-top: 17px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
}

.card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 20px;
}

.card h2 {
    margin: 0 0 7px;
    font-size: 18px;
}

.small {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.5;
}

.full {
    grid-column: 1 / -1;
}

.upload {
    margin-top: 17px;
    min-height: 270px;
    border: 2px dashed #3a3a3a;
    border-radius: 18px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
}

.upload:hover {
    border-color: #fff;
}

.upload-icon {
    font-size: 46px;
    margin-bottom: 10px;
}

input[type=file] {
    display: none;
}

.preview {
    width: 100%;
    max-height: 330px;
    object-fit: contain;
    margin-top: 15px;
    border-radius: 15px;
    display: none;
    background: #050505;
}

label.title {
    display: block;
    margin-top: 15px;
    margin-bottom: 7px;
    font-size: 12px;
    color: #aaa;
}

input[type=text],
textarea,
select {
    width: 100%;
    color: white;
    background: #181818;
    border: 1px solid #303030;
    border-radius: 13px;
    padding: 13px;
    outline: none;
}

textarea {
    min-height: 110px;
    resize: vertical;
}

input:focus,
textarea:focus,
select:focus {
    border-color: #777;
}

.options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-top: 15px;
}

.option {
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #303030;
    background: #171717;
}

.option.active {
    border-color: #fff;
    background: #222;
}

.option strong {
    display: block;
    margin-bottom: 5px;
}

.option span {
    font-size: 11px;
    color: #999;
}

.action {
    margin-top: 20px;
}

.primary {
    width: 100%;
    border: 0;
    border-radius: 16px;
    padding: 17px;
    background: white;
    color: black;
    font-weight: 900;
    font-size: 15px;
}

.secondary {
    border: 1px solid #333;
    background: #171717;
    color: white;
    padding: 12px 16px;
    border-radius: 12px;
}

.loading {
    display: none;
    text-align: center;
    color: #aaa;
    padding: 25px;
}

.results {
    display: none;
    margin-top: 18px;
}

.concept {
    border: 1px solid #2d2d2d;
    background: #141414;
    border-radius: 18px;
    padding: 18px;
    margin-top: 12px;
}

.concept-top {
    display: flex;
    justify-content: space-between;
    gap: 10px;
}

.badge {
    font-size: 10px;
    border: 1px solid #3a3a3a;
    padding: 6px 9px;
    border-radius: 20px;
    color: #aaa;
}

.concept h3 {
    margin: 0;
}

.hook {
    margin-top: 15px;
    font-weight: 800;
}

.section-label {
    color: #888;
    text-transform: uppercase;
    font-size: 10px;
    letter-spacing: 1px;
    margin-top: 15px;
    margin-bottom: 6px;
}

.scene {
    background: #1a1a1a;
    border-radius: 10px;
    padding: 10px;
    margin-top: 5px;
    font-size: 12px;
    color: #ccc;
}

.prompt {
    white-space: pre-wrap;
    background: #080808;
    border: 1px solid #292929;
    padding: 13px;
    border-radius: 12px;
    font-size: 12px;
    color: #bbb;
}

.empty {
    color: #777;
    text-align: center;
    padding: 25px;
}

.footer {
    text-align: center;
    color: #555;
    padding: 35px 0 20px;
    font-size: 11px;
}

@media(max-width: 760px) {

    .grid {
        grid-template-columns: 1fr;
    }

    .full {
        grid-column: auto;
    }

    .options {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 42px;
    }

}

</style>

</head>


<body>

<div class="app">

<header>

<div class="brand">AD STUDIO</div>

<div class="version">
V18.1
</div>

</header>


<section class="hero">

<h1>
FROM PRODUCT<br>
TO AD.
</h1>

<p>
Transforme une simple photo de produit en concepts
publicitaires structurés pour TikTok, Instagram, WhatsApp
et autres réseaux sociaux.
</p>

</section>


<div class="grid">


<!-- PRODUCT -->

<section class="card">

<h2>01 — PRODUCT</h2>

<div class="small">
Importe ton produit et donne quelques informations
à Creative Brain.
</div>

<label class="upload" for="product">

<div class="upload-icon">＋</div>

<strong>Importer le produit</strong>

<div class="small">
JPG · PNG · WEBP
</div>

</label>

<input
id="product"
type="file"
accept="image/*"
>

<img
id="preview"
class="preview"
>

<label class="title">
Nom du produit
</label>

<input
id="productName"
type="text"
placeholder="Ex : Oroma"
>

<label class="title">
Description
</label>

<textarea
id="description"
placeholder="Décris brièvement le produit..."
></textarea>

<label class="title">
Public cible
</label>

<input
id="audience"
type="text"
placeholder="Ex : étudiants, familles, travailleurs..."
>

<label class="title">
Avantages / arguments de vente
</label>

<textarea
id="benefits"
placeholder="Ex : naturel, frais, local, abordable..."
></textarea>

</section>


<!-- CREATIVE BRAIN -->

<section class="card">

<h2>02 — CREATIVE BRAIN</h2>

<div class="small">
Construis la direction créative de ta publicité.
</div>


<label class="title">
Style publicitaire
</label>

<div
class="options"
id="styles"
>

<div
class="option active"
data-value="viral"
>
<strong>🔥 Viral</strong>
<span>Rapide, accrocheur, social.</span>
</div>

<div
class="option"
data-value="premium"
>
<strong>💎 Premium</strong>
<span>Élégant et haut de gamme.</span>
</div>

<div
class="option"
data-value="emotion"
>
<strong>❤️ Émotion</strong>
<span>Storytelling et connexion.</span>
</div>

<div
class="option"
data-value="dynamic"
>
<strong>⚡ Dynamique</strong>
<span>Énergique et moderne.</span>
</div>

</div>


<label class="title">
Type de Hook
</label>

<div
class="options"
id="hooks"
>

<div
class="option active"
data-value="question"
>
<strong>Question</strong>
<span>Créer une curiosité immédiate.</span>
</div>

<div
class="option"
data-value="problem"
>
<strong>Problème</strong>
<span>Problème puis solution.</span>
</div>

<div
class="option"
data-value="surprise"
>
<strong>Surprise</strong>
<span>Créer un effet inattendu.</span>
</div>

<div
class="option"
data-value="direct"
>
<strong>Direct</strong>
<span>Présenter immédiatement le produit.</span>
</div>

</div>


<label class="title">
Plateforme
</label>

<select id="platform">

<option value="tiktok">
TikTok
</option>

<option value="instagram">
Instagram Reels
</option>

<option value="whatsapp">
WhatsApp
</option>

<option value="youtube">
YouTube Shorts
</option>

</select>


<label class="title">
Format
</label>

<select id="format">

<option value="9:16">
9:16 — Vertical
</option>

<option value="1:1">
1:1 — Carré
</option>

<option value="16:9">
16:9 — Horizontal
</option>

</select>


<label class="title">
Durée
</label>

<select id="duration">

<option value="5">
5 secondes
</option>

<option value="8">
8 secondes
</option>

<option value="10">
10 secondes
</option>

<option value="12">
12 secondes
</option>

</select>


<div class="action">

<button
class="primary"
onclick="generate()"
>
✨ GÉNÉRER 5 PUBLICITÉS
</button>

</div>

</section>


<!-- VIDEO BUILDER -->

<section class="card full">

<h2>03 — VIDEO BUILDER</h2>

<div class="small">
Après génération, chaque concept devient un plan
vidéo exploitable par un générateur IA.
</div>

<div
id="builder"
class="empty"
>
Tes concepts apparaîtront ici.
</div>

</section>


<!-- RESULTS -->

<section
id="results"
class="card full results"
>

<h2>04 — CREATIVE OUTPUT</h2>

<div class="small">
Cinq directions publicitaires générées à partir de ton brief.
</div>

<div id="concepts"></div>

</section>


</div>


<div class="footer">
AD STUDIO V18.1 · Creative Advertising Workspace
</div>

</div>


<script>

let selectedStyle = "viral";
let selectedHook = "question";


// ------------------------------------------------------------
// IMAGE PREVIEW
// ------------------------------------------------------------

const fileInput =
document.getElementById("product");

const preview =
document.getElementById("preview");

fileInput.addEventListener(
"change",
function() {

const file = this.files[0];

if (!file) return;

preview.src =
URL.createObjectURL(file);

preview.style.display =
"block";

}
);


// ------------------------------------------------------------
// OPTION SELECTORS
// ------------------------------------------------------------

document
.querySelectorAll("#styles .option")
.forEach(option => {

option.addEventListener(
"click",
function() {

document
.querySelectorAll("#styles .option")
.forEach(x =>
x.classList.remove("active")
);

this.classList.add("active");

selectedStyle =
this.dataset.value;

}
);

});


document
.querySelectorAll("#hooks .option")
.forEach(option => {

option.addEventListener(
"click",
function() {

document
.querySelectorAll("#hooks .option")
.forEach(x =>
x.classList.remove("active")
);

this.classList.add("active");

selectedHook =
this.dataset.value;

}
);

});


// ------------------------------------------------------------
// GENERATE
// ------------------------------------------------------------

async function generate() {

const product =
document.getElementById(
"productName"
).value.trim();

const description =
document.getElementById(
"description"
).value.trim();

const audience =
document.getElementById(
"audience"
).value.trim();

const benefits =
document.getElementById(
"benefits"
).value.trim();

const platform =
document.getElementById(
"platform"
).value;

const format =
document.getElementById(
"format"
).value;

const duration =
document.getElementById(
"duration"
).value;


const results =
document.getElementById(
"results"
);

const concepts =
document.getElementById(
"concepts"
);

const builder =
document.getElementById(
"builder"
);


builder.innerHTML =
"<div class='loading' style='display:block'>🧠 Creative Brain travaille...</div>";

results.style.display =
"block";

concepts.innerHTML =
"<div class='loading' style='display:block'>Génération des concepts...</div>";

results.scrollIntoView({
behavior: "smooth"
});


try {

const response =
await fetch(
"/api/generate",
{
method: "POST",

headers: {
"Content-Type":
"application/json"
},

body: JSON.stringify({

product_name:
product,

description:
description,

audience:
audience,

benefits:
benefits,

style:
selectedStyle,

hook:
selectedHook,

platform:
platform,

format:
format,

duration:
duration

})

}
);


const data =
await response.json();


if (!data.success) {

throw new Error(
data.error ||
"Erreur de génération."
);

}


renderConcepts(
data.concepts,
platform,
format,
duration
);


builder.innerHTML = `

<div style="
margin-top:18px;
display:grid;
grid-template-columns:
repeat(auto-fit,minmax(180px,1fr));
gap:10px;
">

<div class="concept">
<strong>FORMAT</strong>
<div class="small">${format}</div>
</div>

<div class="concept">
<strong>DURÉE</strong>
<div class="small">${duration}s</div>
</div>

<div class="concept">
<strong>PLATEFORME</strong>
<div class="small">${platform}</div>
</div>

<div class="concept">
<strong>STYLE</strong>
<div class="small">${selectedStyle}</div>
</div>

</div>

`;

}

catch(error) {

concepts.innerHTML =
"<div class='empty'>Une erreur est survenue : "
+ error.message
+ "</div>";

}

}


// ------------------------------------------------------------
// RENDER CONCEPTS
// ------------------------------------------------------------

function renderConcepts(
items,
platform,
format,
duration
) {

const container =
document.getElementById(
"concepts"
);

container.innerHTML = "";


items.forEach(
(item, index) => {

const scenes =
item.scenes
.map(
scene =>
`<div class="scene">${escapeHtml(scene)}</div>`
)
.join("");


const prompt =
`
Create a ${duration}-second ${format} advertising video
for ${platform}.

PRODUCT:
${item.title}

HOOK:
${item.hook}

VISUAL DIRECTION:
${item.script}

SCENES:
${item.scenes.join("\n")}

VOICE:
${item.voice}

CTA:
${item.cta}

Important:
Preserve the exact physical appearance of the product
from the reference image. Do not redesign, deform,
rename or invent the product.
`;


container.innerHTML += `
