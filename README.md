# Tech_task Chatbot

This Chatbot is designed to answer customer queries based on an FAQ Database. It's a flask web application, using sentence transformers, and the Faiss library for efficient searching and retrieval of responses.



## Features
- **Natural Language Processing**: Utilizes Openai NLP models for processing the user input.
- **Fast and Accurate**: Uses the Faiss library for efficient indexing and searching of FAQ data.
- **Interactive Interface**: Provides a web-based user interface for interacting with the chatbot.
- **Dockerized Application**: The application is dockerized for ease of deployment and scaling.

## Setup and Installation
1. Clone the repository:
    ```
    git clone [https://github.com/DavidCabestany/chatbot_MiniLM](https://github.com/DavidCabestany/chatbot_MiniLM.git)
    cd chatbot_MiniLM/
    ```

2. Build the Docker image:
    ```
    docker build -t chatbot .
    ```

3. Run the Docker container:
    ```
    docker run -p 5005:5005 chatbot
    ```
    wait until appears a message like this:

   ```
        * Serving Flask app 'app'
        * Debug mode: on
   ```


5. Access the chatbot in your web browser at `http://127.0.0.1:5005`.

## Usage
Enter your query in the chat box and press enter or click the send button. The chatbot will respond with the most relevant answer from the FAQ list.

## License
This project is licensed under the GNU V3 License. See the [LICENSE](LICENSE) file for more information.
