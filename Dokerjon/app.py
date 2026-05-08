from flask import Flask, render_template_string

app = Flask(__name__)

# HTML va CSS bitta joyda
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            padding: 50px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 { color: #2496ed; }
        p { color: #555; font-size: 1.2em; }
        .status { color: green; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Docker & Flask</h1>
        <p>Ilova muvaffaqiyatli ishga tushdi!</p>
        <p class="status">Manzil: 0.0.0.0 (Hamma uchun ochiq)</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    # host='0.0.0.0' - bu konteyner tashqarisidan ulanish imkonini beradi
    app.run(debug=True, host='0.0.0.0', port=5000)