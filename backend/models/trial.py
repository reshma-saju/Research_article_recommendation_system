final_recommended_articles_id=[704.0032,704.005]
for i, val in enumerate(final_recommended_articles_id):
    if len(str(val)) < 10:
        formatted_num = "{:08.4f}".format(val)
        final_recommended_articles_id[i] = formatted_num
    print(final_recommended_articles_id)