from nltk.tokenize import sent_tokenize
import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx


def getSummary(text):
    sentences = sent_tokenize(text)
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(sentence_vectors)
    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)
    num_sentences = 3
    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary_sentences = [sentence for _,
                         sentence in ranked_sentences[:num_sentences]]
    return ' '.join(summary_sentences)
