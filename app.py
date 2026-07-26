from flask import Flask, render_template, request
from src.document_processing import extract_text, split_text
from src.chatbot import create_vector_store, get_answer
from src.utils import save_uploaded_file

app = Flask(__name__)

index = None
chunks = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    global index, chunks

    file = request.files["pdf"]

    file_path = save_uploaded_file(file)

    text = extract_text(file_path)

    chunks = split_text(text)

    index, chunks = create_vector_store(chunks)

    return render_template(
        "index.html",
        answer="✅ PDF uploaded successfully! Now ask a question."
    )


@app.route("/ask", methods=["POST"])
def ask():
    global index, chunks

    question = request.form["question"]

    if index is None:
        return render_template(
            "index.html",
            answer="Please upload a PDF first."
        )

    answer = get_answer(question, index, chunks)

    return render_template(
        "index.html",
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)