

<body>

<h1>Online Ticket Booking System with Recommender Model</h1>

<p>
    This project was created as part of a hackathon, aimed at developing a web-based ticket booking system for historical places. The system integrates a recommender model to suggest places for users to visit, based on their most highly rated places. 
    The recommendations are generated using Natural Language Processing (NLP) to analyze the descriptions of places and find similarities between them.
</p>

<h2>Features</h2>
<ul>
    <li><strong>Online Ticket Booking:</strong> Users can book tickets for historical places through an interactive chatbot.</li>
    <li><strong>Recommender System:</strong> The system suggests new places based on the user's highest-rated places from an API.</li>
    <li><strong>NLP for Recommendations:</strong> NLP techniques are used to preprocess text, remove stopwords, and analyze descriptions of places to suggest similar ones.</li>
    <li><strong>Cosine Similarity for Matching:</strong> Cosine Similarity is used to compare places based on the descriptions, providing recommendations of the most similar places.</li>
</ul>

<h2>How It Works</h2>

<h3>1. Natural Language Processing (NLP)</h3>
<p>
    To make accurate recommendations, the project uses NLP to preprocess the descriptions of each historical place:
</p>
<ul>
    <li><strong>Stemming:</strong> Each place's description is converted to lowercase, and stemming is applied using NLTK's PorterStemmer to reduce words to their base form (e.g., "running" becomes "run").</li>
    <li><strong>Stopword Removal:</strong> Common words such as "is", "am", "are", etc., are removed using the stopwords list from the <code>sklearn</code> library. This helps focus on the most meaningful words for recommendations.</li>
</ul>

<h3>2. Feature Extraction</h3>
<p>
    After preprocessing the text, the project uses the <code>CountVectorizer</code> from <code>sklearn</code> to extract the 500 most frequent words from the place descriptions. These words are then used to create vectors for each description, representing the importance of each word in the description. 
</p>

<h3>3. Similarity Calculation</h3>
<ul>
    <li><strong>Vectorization:</strong> Each preprocessed description is transformed into a vector using word counts, creating a unique vector for every place.</li>
    <li><strong>Cosine Similarity:</strong> The system calculates Cosine Similarity between these vectors to determine how similar each place is to another. This is used to recommend the most similar places based on the user's preferences.</li>
    <li><strong>Recommendations:</strong> Based on the user’s most-rated places from the API, the system suggests the top 7 most similar places by sorting them based on similarity scores.</li>
</ul>

<h2>API Workflow</h2>
<ol>
    <li><strong>User Input:</strong> The user interacts with the chatbot for ticket booking or place recommendations.</li>
    <li><strong>Recommendations:</strong> The system analyzes the descriptions of places using NLP and suggests the most similar ones.</li>
    <li><strong>Booking Confirmation:</strong> The user can choose from the recommended places and proceed to book tickets through the chatbot.</li>
</ol>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Flask:</strong> Backend framework used to handle API requests and serve the recommendation logic.</li>
    <li><strong>NLTK:</strong> Used for text preprocessing, including stemming.</li>
    <li><strong>scikit-learn:</strong> Used for <code>CountVectorizer</code> to extract frequent words and for calculating <code>Cosine Similarity</code>.</li>
    <li><strong>Pandas:</strong> Used for data manipulation, including loading the CSV dataset.</li>
    <li><strong>MongoDB:</strong> Placeholder used to simulate fetching user data.</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yashgoyal-16/Place-Recomender
cd ticket-booking-system
        </code></pre>
    </li>
    <li>Install dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Run the Flask app:
        <pre><code>python app.py</code></pre>
    </li>
    <li>Make a POST request to get recommendations using Postman or <code>curl</code>:
        <pre><code>curl -X POST http://127.0.0.1:5000/recommend -H "Content-Type: application/json" -d '{"user_id": "12345", "place": "Golden Temple"}'
        </code></pre>
    </li>
</ol>

<h2>Hackathon Experience</h2>
<p>
    In this hackathon, I worked on integrating machine learning and NLP techniques to enhance the user experience for booking tickets to historical places. I built a recommendation model using <strong>CountVectorizer</strong> and <strong>Cosine Similarity</strong> to suggest places based on the user's preferences, helping users discover new and similar places.
</p>


</body>
</html>
