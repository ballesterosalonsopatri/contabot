import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

# --------------------
# CARGA VARIABLES ENTORNO
# --------------------
load_dotenv()

app = Flask(__name__)

# --------------------
# CONFIGURACIÓN BD
# --------------------
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --------------------
# MODELO BD
# --------------------
class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.Text, nullable=False)
    ai_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# --------------------
# CONFIGURACIÓN LLM (CORRECTA)
# --------------------
llm_base = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    task="conversational",
    temperature=0.4,
    max_new_tokens=300
)

llm = ChatHuggingFace(llm=llm_base)

# --------------------
# PROMPT CONTABILIDAD
# --------------------
template = """
Eres un asistente especializado en contabilidad básica para España.

Instrucciones:
- Explica con lenguaje claro y ejemplos prácticos
- Estructura: definición → ejemplo → recursos gratuitos
- SIEMPRE aclara que no proporcionas asesoría fiscal profesional

Pregunta: {pregunta}

Respuesta:
"""

prompt = PromptTemplate(
    input_variables=["pregunta"],
    template=template,
)

# --------------------
# RUTAS
# --------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    respuesta = None

    if request.method == 'POST':
        user_query = request.form.get('query')

        if user_query:
            chain = prompt | llm
            resultado = chain.invoke({"pregunta": user_query})
            respuesta = resultado.content

            nueva = Interaction(
                user_input=user_query,
                ai_response=respuesta
            )
            db.session.add(nueva)
            db.session.commit()

    historial = Interaction.query.order_by(
        Interaction.timestamp.desc()
    ).limit(5).all()

    return render_template(
        'index.html',
        respuesta=respuesta,
        historial=historial
    )

# --------------------
# MAIN
# --------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8080, debug=True)
