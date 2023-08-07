import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity


def title_getRecommendation(input_title):

    # Load dataset
    data = pd.read_csv('.\data\project_data.csv')
    titles = data['title']

    # Text preprocessing and creating a document-term matrix
    vectorizer = TfidfVectorizer(
        stop_words='english', max_df=0.8, min_df=2, ngram_range=(1, 2))
    X = vectorizer.fit_transform(titles)

    # Apply Latent Semantic Analysis (LSA)
    num_topics = 32  # Experiment with different numbers
    lsa_model = TruncatedSVD(n_components=num_topics)
    lsa_topic_matrix = lsa_model.fit_transform(X)

    # Normalize LSA topic matrix
    from sklearn.preprocessing import normalize
    lsa_topic_matrix = normalize(lsa_topic_matrix)

    # Function to get recommendations
    num_recommendations = 5
    input_vector = vectorizer.transform([input_title])
    input_topic = lsa_model.transform(input_vector)
    input_topic = normalize(input_topic)

    similarities = cosine_similarity(input_topic, lsa_topic_matrix)

    similar_indices = similarities.argsort(
    )[0][-num_recommendations-1:-1][::-1]
    similar_text_indices = []
    for index in similar_indices:
        similar_text_indices.append(data['id'][index])
    for i, val in enumerate(similar_text_indices):
        if len(str(val)) < 10:
            num_str = str(val)
            whole_part, decimal_part = num_str.split('.')

            whole_part = whole_part.rjust(4, '0')
            decimal_part = decimal_part.ljust(4, '0')

            similar_text_indices[i]=whole_part + '.' + decimal_part

    recommendations = {}
    j=0
    for index in similar_text_indices:
        recommendations[index] = data['title'][similar_indices[j]]
        j+=1

    # Test the recommendation syste
    return recommendations
