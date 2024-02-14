from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

global global_df
global_df = None

@app.route('/')
def index():
    return render_template('index.html', display=False)


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and file.filename.endswith('.csv'):
            global global_df
            global_df = pd.read_csv(file)
            # Process your CSV file here, e.g., print the DataFrame
            print(global_df)
            return render_template('index.html', is_file=True, file_name=file.filename)
        else:
            return render_template('index.html', is_file=False)
        
@app.route('/table')
def show_table():

    # Convert DataFrame to HTML
    df_html = global_df.to_html(classes='table table-striped', index=False)

    # Pass the HTML to the template
    return render_template('table.html', table=df_html)
        
if __name__ == '__main__':
    app.run(debug=True)