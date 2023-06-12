from gensim.models import HdpModel, LdaModel
from gensim.corpora import Dictionary
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def getTopics(paragraph):
    tokenized_paragraph = paragraph.lower().split()
    dictionary = Dictionary([tokenized_paragraph])
    bow_corpus = [dictionary.doc2bow(tokenized_paragraph)]
    hdp_model = HdpModel(corpus=bow_corpus, id2word=dictionary)
    hdp_topics = hdp_model.show_topics()
    lda_model = LdaModel(corpus=bow_corpus, id2word=dictionary, num_topics=5)
    lda_topics = lda_model.show_topics()
    def remove_stop_words(text):
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text)
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        filtered_text = ' '.join(filtered_tokens)
        
        return filtered_text
    def remove_numbers_dots_plus(string):
        pattern = r"[^a-zA-Z\s]"
        cleaned_string = re.sub(pattern, "", string)
        cleaned_string = remove_stop_words(cleaned_string)
        return cleaned_string

    new_hdp=[]
    new_lda=[]

    for val, topic in enumerate(hdp_topics):
        topic_words = topic[1]
        sentence= remove_numbers_dots_plus(topic_words)
        new_hdp.append(sentence)
        if val==10:
            break

    for topic in lda_topics:
        topic_words = topic[1]
        sentence= remove_numbers_dots_plus(topic_words)
        new_lda.append(sentence)

    return new_hdp, new_lda

