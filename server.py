from flask import Flask, request, jsonify

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
            body {
                margin: 0;
                background: #080808;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            .container {
                max-width: 700px;
                margin: auto;
                padding: 50px 20px;
            }

            h1 {
                font-size: 42px;
                margin-bottom: 10px;
            }

            p {
                color: #aaa;
                line-height: 1.6;
            }

            .box {
                margin-top: 30px;
                padding: 30px;
                border: 1px solid #292929;
                border-radius: 20px;
                background: #111;
            }

            input, textarea, button {
                width: 100%;
                box-sizing: border-box;
                margin-top: 12px;
                padding: 14px;
                border-radius: 10px;
                border: 1px solid #333;
                background: #1a1a1a;
                color: white;
            }

            button {
                background: white;
                color: black;
                font-weight: bold;
                cursor: pointer;
            }

            #result {
                margin-top: 25px;
                text-align: left;
                white-space: pre-wrap;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>AD STUDIO</h1>

            <p>
                Transforme les informations d'un produit
                en concepts publicitaires.
            </p>

            <div class="box">

                <input
                    id="product"
                    type="text"
                    placeholder="Nom du produit"
                >

                <textarea
                    id="description"
                    placeholder="Description du produit"
                ></textarea>

                <textarea
                    id="benefits"
                    placeholder="Avantages du produit"
                ></textarea>

                <button onclick="generate()">
                    GENERER LA PUBLICITE
                </button>

                <div id="result"></div>

            </div>

        </div>

        <script>
            async function generate() {

                const product =
                    document.getElementById("product").value;

                const description =
                    document.getElementById("description").value;

                const benefits =
                    document.getElementById("benefits").value;

                const result =
                    document.getElementById("result");

                result.textContent = "Génération en cours...";

                try {

                    const response = await fetch(
                        "/api/generate",
                        {
                            method: "POST",
                            headers: {
                                "Content-Type":
                                    "application/json"
                            },
                            body: JSON.stringify({
                                product_name: product,
                                description: description,
                                benefits: benefits
                            })
                        }
                    );

                    const data =
                        await response.json();

                    result.textContent =
                        data.text || data.error;

                } catch (error) {

                    result.textContent =
                        "Erreur : " + error.message;

                }
            }
        </script>

    </body>
    </html>
    """


@app.route("/api/generate", methods=["POST"])
def generate():

    data = request.get_json() or {}

    product = data.get("product_name", "ce produit")
    description = data.get(
        "description",
        "Un produit de qualité."
    )
    benefits = data.get(
        "benefits",
        "qualité, simplicité et efficacité"
    )

    text = (
        "PUBLICITE AD STUDIO\n\n"
        "PRODUIT : " + product + "\n\n"
        "HOOK :\n"
        "Découvrez " + product + " !\n\n"
        "DESCRIPTION :\n"
        + description +
        "\n\n"
        "AVANTAGES :\n"
        + benefits +
        "\n\n"
        "CTA :\n"
        "Découvrez-le maintenant."
    )

    return jsonify({
        "success": True,
        "text": text
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
