from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize the Porter Stemmer
ps = PorterStemmer()

# Function to preprocess text (lowercase and stemming)
def preprocess(text):
    text = text.lower()
    stemmed_text = [ps.stem(word) for word in text.split()]
    return " ".join(stemmed_text)

# Function to load the CSV, preprocess, and compute similarity matrix dynamically
def load_data_and_compute_similarity():
    # Load the dataset
    a = pd.read_csv("punjab_ticketed_places.csv")

    # Debugging: Print the DataFrame and its columns
    print("DataFrame:\n", a.head())  # Print first few rows
    print("DataFrame columns:", a.columns.tolist())  # Print column names

    # Check if 'id' and 'description' columns exist
    if 'id' not in a.columns or 'description' not in a.columns:
        raise ValueError("The required columns 'id' or 'description' are not present in the CSV file.")

    # Ensure the 'id' column is of type string
    a['id'] = a['id'].astype(str)

    # Preprocess the descriptions
    a['description'] = a['description'].apply(preprocess)

    # Convert descriptions into vectors using CountVectorizer
    cv = CountVectorizer(max_features=500, stop_words='english')
    vector = cv.fit_transform(a['description']).toarray()

    # Compute cosine similarity between descriptions
    similarity = cosine_similarity(vector)

    return a, similarity

# Mock function to simulate fetching user order history from MongoDB
def get_user_orders(user_id):
    # This is a placeholder. Replace with actual MongoDB query logic.
    user_orders = ["Golden Temple", "Jallianwala Bagh"]  # Example data
    return user_orders

# Define the recommendation function
def get_recommendations(user_id, place=None):
    a, similarity = load_data_and_compute_similarity()
    user_orders = get_user_orders(user_id)

    if place:
        place = place.lower()
        try:
            index = a[a['monumentName'].str.lower() == place].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            recommended_ids = [a.iloc[i[0]]['id'] for i in distances[1:6]]  # Get top 5 recommendations
            return recommended_ids
        except IndexError:
            return []

    recommendations = []
    for ordered_place in user_orders:
        try:
            index = a[a['monumentName'].str.lower() == ordered_place.lower()].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            recommended_ids = [a.iloc[i[0]]['id'] for i in distances[1:3]]  # Get top 2 recommendations
            recommendations.extend(recommended_ids)
        except IndexError:
            continue
    return list(set(recommendations))

# API route for recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data.get('user_id')
    place = data.get('place')
    
    if not user_id:
        return jsonify({"error": "Please provide a user ID."}), 400
    
    try:
        recommendations = get_recommendations(user_id, place)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

    if recommendations:
        return jsonify({"user_id": user_id, "recommendations": recommendations}), 200
    else:
        return jsonify({"error": "No recommendations found."}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
