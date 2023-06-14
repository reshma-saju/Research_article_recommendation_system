from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# title_read="""Matter-Wave Bright Solitons with a Finite Background in Spinor
#   Bose-Einstein Condensates
# """


def title_getRecommendation(title_read):

    RES_ARTICLES = ".\data\project_data.csv"
    # ARTICLE_READ=[1,10]
    num_recommendations = 5

    res_articles = pd.read_csv(RES_ARTICLES, encoding='utf-8', index_col=0)
    # drop all the unnamed columns
    res_articles.drop(res_articles.columns[res_articles.columns.str.contains(
        'unnamed', case=False)], axis=1, inplace=True)
    res_articles.head()
    res_ids = res_articles.index.tolist()

    res_articles = res_articles[['title', 'abstract']].dropna()
    # articles is a list of all articles
    titles = res_articles['title'].tolist()
    titles = [title_read]+titles
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(titles)
    # Choose the desired number of components
    lsa_model = TruncatedSVD(n_components=100)
    lsa_matrix = lsa_model.fit_transform(tfidf_matrix)
    similarity_matrix = cosine_similarity(lsa_matrix)
    input_text_index = 0  # Index of the input text
    similar_text_indices = similarity_matrix[input_text_index].argsort(
    )[-(num_recommendations+1):][::-1][1:]  # Exclude the input text
    ref_indices = similar_text_indices
    similar_text_indices = [res_ids[i-2] for i in similar_text_indices]
    recommended_texts = [titles[idx-1] for idx in ref_indices]
    for i, val in enumerate(similar_text_indices):
        if len(str(val)) < 10:
            num_str = str(val)
            whole_part, decimal_part = num_str.split('.')

            whole_part = whole_part.rjust(4, '0')
            decimal_part = decimal_part.ljust(4, '0')

            similar_text_indices[i] = whole_part + '.' + decimal_part
    # results is in print(recommended_texts)
    return dict(zip(similar_text_indices, recommended_texts))
