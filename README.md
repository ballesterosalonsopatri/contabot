# 🤖 ContaBot — Asistente Contable con IA Generativa

ContaBot es una aplicación web basada en **IA Generativa** que responde en lenguaje natural a consultas sobre **contabilidad básica** (IVA, IRPF, facturación, balances, etc.).

Integra un **modelo de lenguaje (LLM)** de Hugging Face mediante **LangChain**, con persistencia de interacciones en una **base de datos PostgreSQL** en la nube. El proyecto sigue una arquitectura **moderna y escalable**, implementada con **Docker**, **Render** y prácticas propias de despliegue en producción.

---

## 🚀 Demo en producción

🔗 **Aplicación online:**  
[https://contabot-6rwr.onrender.com](https://contabot-6rwr.onrender.com)

Los usuarios pueden realizar consultas contables y obtener respuestas generadas por IA en tiempo real.  
Todas las interacciones se registran automáticamente en la base de datos.

---

## 🐳 Imagen de Docker

La aplicación se distribuye como una **imagen pública en Docker Hub**:

🔗 [https://hub.docker.com/r/ballesterosalonsopatri/contabot](https://hub.docker.com/r/ballesterosalonsopatri/contabot)

Render descarga la imagen directamente desde Docker Hub para su despliegue automatizado.

---

## 🧠 Stack tecnológico

| Capa | Tecnologías |
|------|--------------|
| Backend | Python, Flask |
| IA | Hugging Face Zephyr-7B, LangChain |
| Prompt Engineering | LangChain PromptTemplate |
| Base de datos | PostgreSQL (Render) |
| Frontend | HTML + Bootstrap |
| Infraestructura | Docker, Docker Hub, Render |

---

## 🧩 Arquitectura general

Usuario (Navegador)
│
▼
Frontend (Flask Template)
│
▼
API Flask (Python)
│
▼
LangChain PromptTemplate
│
▼
Hugging Face LLM (Zephyr 7B)
│
▼
Respuesta generada
│
▼
PostgreSQL (Render 🐘)
│
▼
Historial mostrado al usuario


---

## 🐘 Persistencia de datos

La base de datos **PostgreSQL** gestiona:

- Texto de la pregunta del usuario  
- Respuesta generada por el modelo  
- Fecha y hora de la interacción  

Este registro permite mantener un **histórico de consultas y análisis de comportamiento**, necesario para evaluación y mejora continua del modelo.

---
## 🔐 Variables de entorno

```bash
HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxxxxxxx
DATABASE_URL=postgresql://user:password@host:5432/database```
---

En producción, Render gestiona las variables de entorno de forma segura.
💻 Ejecución local con Docker
Para clonar y ejecutar el proyecto localmente:

docker build -t contabot .
docker run -p 8080:8080 --env-file .env contabot

🎯 Casos de uso
ContaBot está diseñado para apoyar a:

Estudiantes y docentes de contabilidad

Autónomos y profesionales fiscales

Administrativos y asesores contables

Usuarios que deseen entender conceptos tributarios sin tecnicismos

Consultas posibles:

IVA

IRPF

Registro de facturas

Balances

Gastos y cuentas

Todo mediante lenguaje natural, con respuestas generadas por IA.

📦 Funcionalidades destacadas
Interfaz web intuitiva y responsiva

Motor IA especializado en contabilidad española

Prompts optimizados para respuestas estructuradas y coherentes

Registro persistente de todas las conversaciones

Despliegue completo en la nube con Docker + Render

Integración modular y escalable, pensada para ampliaciones futuras (inferencia avanzada, analítica de datos, etc.)
