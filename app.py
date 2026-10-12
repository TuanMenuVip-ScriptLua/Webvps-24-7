from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Free 24/7</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: system-ui, -apple-system, sans-serif;
            text-align: center;
            padding: 40px 20px;
            background: #0f172a;
            color: white;
            margin: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: #1e293b;
            padding: 40px 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 400px;
            width: 100%;
        }
        h1 {
            color: #38bdf8;
            margin-bottom: 15px;
            font-size: 1.8rem;
        }
        p {
            color: #94a3b8;
            line-height: 1.6;
            margin: 8px 0;
        }
        .badge {
            display: inline-block;
            background: #22c55e;
            color: white;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Web đang chạy 24/7</h1>
        <p>Python 3.13 + Flask</p>
        <p>Deploy trên Render Free</p>
        <p>Không tốn pin điện thoại</p>
        <div class="badge">Online</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
