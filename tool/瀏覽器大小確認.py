from flask import Flask, render_template_string
import webbrowser
from threading import Timer

app = Flask(__name__)

# HTML -
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title當前的瀏覽器大小</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .size-display {
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .size {
            font-size: 24px;
            color: #333;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="size-display">
        <h2>當前的瀏覽器大小</h2>
        <div id="size" class="size">
            Width: <span id="width">0</span>px<br>
            Height: <span id="height">0</span>px
        </div>
    </div>

    <script>
        function updateSize() {
            document.getElementById('width').textContent = window.innerWidth;
            document.getElementById('height').textContent = window.innerHeight;
        }

        // Update size immediately
        updateSize();

        // Update size when window is resized
        window.addEventListener('resize', updateSize);
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Open browser after a short delay
    Timer(1.5, open_browser).start()
    # Run the Flask app
    app.run()