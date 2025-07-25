from app import create_app, db
import os

app = create_app()


# Optional: Flask CLI context for shell
@app.shell_context_processor
def make_shell_context():
    return {"db": db}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
