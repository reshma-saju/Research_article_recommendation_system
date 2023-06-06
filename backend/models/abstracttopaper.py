
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

class ArticleRecommender:
    def getRecommendation(self, ARTICLE_READ):
        #Input abstract

        RES_ARTICLES="D:\Mini_project\Research_article_recommendation_system\data\project_data.csv"
        # ARTICLE_READ=[1,10]
        NUM_RECOMMENDED_ARTICLES=5

        res_articles = pd.read_csv(RES_ARTICLES,encoding='utf-8',index_col=0)
        #drop all the unnamed columns
        res_articles.drop(res_articles.columns[res_articles.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        res_articles.head()

        res_ids = res_articles.index.tolist()
        res_ids

        res_articles = res_articles[['title','abstract']].dropna()
        #articles is a list of all articles
        articles = res_articles['abstract'].tolist()
        articles[0] #an uncleaned article

        def clean_text(document):
            document = re.sub('[^\w_\s-]', ' ',document)       #remove punctuation marks and other symbols
            tokens = nltk.word_tokenize(document)              #Tokenize sentences
            cleaned_article = ' '.join([stemmer.stem(item) for item in tokens])    #Stemming each token
            return cleaned_article

        cleaned_articles = list(map(clean_text, articles))
        cleaned_articles[0]  #a cleaned, tokenized and stemmed article

        user_articles = clean_text(ARTICLE_READ)
        user_articles

        #Generate tfidf maatrix model for entire corpus
        tfidf_matrix = TfidfVectorizer(stop_words='english', min_df=2) 
        # min_df : When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold
        article_tfidf_matrix = tfidf_matrix.fit_transform(cleaned_articles)
        article_tfidf_matrix #tfidf vector of an article

        #Generate tfidf matrix model for read articles
        user_article_tfidf_vector = tfidf_matrix.transform([user_articles])
        user_article_tfidf_vector

        user_article_tfidf_vector.toarray()

        articles_similarity_score=cosine_similarity(article_tfidf_matrix, user_article_tfidf_vector)

        articles_similarity_score

        recommended_articles_id = articles_similarity_score.flatten().argsort()[::-1]
        recommended_articles_id

        #Remove read articles from recommendations
        temp_final_id = [article_id for article_id in recommended_articles_id][:NUM_RECOMMENDED_ARTICLES]
        final_recommended_articles_id = [res_ids[i] for i in temp_final_id]
        final_recommended_articles_id

        print ('Recommendations ')
        print (res_articles.loc[final_recommended_articles_id]['title'])

        return res_articles.loc[final_recommended_articles_id]['title']
    
art = ArticleRecommender()
art.getRecommendation("""We discussed quantum deformations of D=4 Lorentz and Poincare algebras. In
        the case of Poincare algebra it is shown that almost all classical r-matrices
        of S. Zakrzewski classification correspond to twisted deformations of Abelian
        and Jordanian types. A part of twists corresponding to the r-matrices of
        Zakrzewski classification are given in explicit form.""")