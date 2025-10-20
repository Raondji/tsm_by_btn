from flask import Flask, render_template, request, jsonify
import pandas as pd
from fix_tsm_itpd import run_hybrid_model  # gunakan model kamu langsung

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    # baca CSV dan langsung jalankan model Python
    df = pd.read_csv(file, delimiter=';')
    result_df = run_hybrid_model(df)

    # ubah hasil ke JSON untuk dikirim ke frontend
    result = result_df.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
