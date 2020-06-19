import os 
from flask import Flask

app = Flask(__name__)
port = int(os.getenv('PORT', 5500))

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/api/sample', methods=['GET'])
def smp():
    return "Hello World"
			
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=True)
	
	
	
	
	
	
	
