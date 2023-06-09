
import numpy
import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from nltk.stem.snowball import SnowballStemmer
import nltk
stemmer = SnowballStemmer("english")
stemmer = SnowballStemmer("english")

# class ArticleRecommender:


def getRecommendation(ARTICLE_READ):
    # Input abstract

    RES_ARTICLES = "./data/project_data.csv"
    # ARTICLE_READ=[1,10]
    NUM_RECOMMENDED_ARTICLES = 5

    res_articles = pd.read_csv(RES_ARTICLES, encoding='utf-8', index_col=0)
    # drop all the unnamed columns
    res_articles.drop(res_articles.columns[res_articles.columns.str.contains(
        'unnamed', case=False)], axis=1, inplace=True)
    res_articles.head()

    res_ids = res_articles.index.tolist()

    res_articles = res_articles[['title', 'abstract']].dropna()
    # articles is a list of all articles
    articles = res_articles['abstract'].tolist()

    def clean_text(document):
        # remove punctuation marks and other symbols
        document = re.sub('[^\w_\s-]', ' ', document)
        tokens = nltk.word_tokenize(document)  # Tokenize sentences
        cleaned_article = ' '.join([stemmer.stem(item)
                                   for item in tokens])  # Stemming each token
        return cleaned_article

    cleaned_articles = list(map(clean_text, articles))

    user_articles = clean_text(ARTICLE_READ)
    # Generate tfidf maatrix model for entire corpus
    tfidf_matrix = TfidfVectorizer(stop_words='english', min_df=2)
    # min_df : When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold
    article_tfidf_matrix = tfidf_matrix.fit_transform(cleaned_articles)

    # Generate tfidf matrix model for read articles
    user_article_tfidf_vector = tfidf_matrix.transform([user_articles])
    user_article_tfidf_vector.toarray()

    articles_similarity_score = cosine_similarity(
        article_tfidf_matrix, user_article_tfidf_vector)

    recommended_articles_id = articles_similarity_score.flatten().argsort()[
        ::-1]

    # Remove read articles from recommendations
    temp_final_id = [
        article_id for article_id in recommended_articles_id][:NUM_RECOMMENDED_ARTICLES]
    final_recommended_articles_id = [res_ids[i] for i in temp_final_id]

    # print ('Recommendations ')
    # print (res_articles.loc[final_recommended_articles_id])
    # print(final_recommended_articles_id)
    titles = res_articles.loc[final_recommended_articles_id]['title']
    for i, val in enumerate(final_recommended_articles_id):
        if len(str(val)) < 10:
            num_str = str(val)
            whole_part, decimal_part = num_str.split('.')

            whole_part = whole_part.rjust(4, '0')
            decimal_part = decimal_part.ljust(4, '0')

            final_recommended_articles_id[i] = whole_part + '.' + decimal_part
    return dict(zip(final_recommended_articles_id, titles))

# art = ArticleRecommender()
# art.getRecommendation("""We discussed quantum deformations of D=4 Lorentz and Poincare algebras. In
#         the case of Poincare algebra it is shown that almost all classical r-matrices
#         of S. Zakrzewski classification correspond to twisted deformations of Abelian
#         and Jordanian types. A part of twists corresponding to the r-matrices of
#         Zakrzewski classification are given in explicit form.""")
