from flask import Flask, jsonify, request, render_template
from chatbot import match_query
import logging
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    # Log user input when types help
    logging.info(f'User input: {userText} -> Rule based answer +Press any button to view its answer.+')
    if userText.lower() == 'help':
        # return a list of questions when the user asks for help
        return jsonify([
            {
                'message': 'Below are relevant questions you might find insightful. <br>Press any button to view its answer. <br>Feel free to ask distinct questions as needed.',
                'questions': []
            },
            {
                'message': '<b>About General Queries:</b>',
                'questions': [
                    "Do you have a refund policy?", 
                    "What Leverage is Available?" ,
                ]
            },
            {
                'message': '<b>About The Challenge:</b> ',
                'questions': [
                    "Can I Reset My Challenge?",
                    "Do I Trade Live or Demo? ",
                    "How Do I Become a Funded Trader?" ,
                ]
            },
            {
                'message': '<b>About The Funded Account:</b> ',
                'questions': [
                    "Am I Required to Have a Verified Account?",
                    "Can I Scale My Account? ",
                    "How Can I Withdraw Profits?" ,
                ]
            },
        ])
        
    if userText.lower() == 'quit':
        return "You have chosen to end this conversation. Please close this chat window."
    else:
        response = match_query(userText)
        return str(response.replace('\n', '<br>'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
