import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)

faqs_dir = 'faqs'
topics = []

# Load the FAQ files and build the index
for dirpath, dirnames, filenames in os.walk(faqs_dir):
    for filename in filenames:
        with open(os.path.join(dirpath, filename), 'r', encoding='latin-1', errors='ignore') as file:
            lines = file.readlines()
            question = lines[0].strip()  # First line is the question
            answer = '\n'.join(line.strip() for line in lines[1:])  # Remaining lines are the answer, joined with line breaks
            topic = {'question': question, 'answer': answer}
            topics.append(topic)
            embedding = model.encode([question])[0]
            index.add(np.array([embedding]))


import logging

# Set up logging
logging.basicConfig(filename='UX_monitoring.log', level=logging.INFO)

def match_query(query, threshold=0.99):
    # Log the user's query
    logging.info(f'User query: {query}')

    embeddings = model.encode([query])
    embeddings = embeddings.reshape(1, -1)
    D, I = index.search(embeddings, 1)
    best_match_index = I[0][0]
    best_match_distance = D[0][0]
    
    # If the distance is below the threshold, return the best match
    if best_match_distance < threshold:
        best_match = topics[best_match_index]

        # Log the best match
        logging.info(f'Best match: {best_match["question"]}')

        return best_match['answer']
    else:
        # If no match is found within the threshold, log this and ask the user to rephrase the question
        logging.info('No good match found.')
        return "I'm sorry, I didn't understand that. Could you rephrase your question?"
