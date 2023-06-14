final_recommended_articles_id=[704.0032,704.005]
for i, val in enumerate(final_recommended_articles_id):
    if len(str(val)) < 10:
        integer_part = int(val)
        decimal_part = int((val - integer_part) * 10000)
        formatted_num = "{:04d}.{:04d}".format(integer_part, decimal_part)
        final_recommended_articles_id[i] = formatted_num
    print(final_recommended_articles_id)