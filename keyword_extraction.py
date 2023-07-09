#
# from pprint import pprint
# import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# nltk.download('wordnet')
#
# from nltk.stem import WordNetLemmatizer
# import pymongo as pm
#
# client = pm.MongoClient('localhost',27017)
#
# db = client['youtube']
#
# coll = db['metadata']
#
#
#
# ##  lemmetization
# lemmetizer = WordNetLemmatizer()
#
#
# def lemmetize_string(string):
#     tokens = nltk.word_tokenize(string)
#     lemmetized_tokens = [lemmetizer.lemmatize(token) for token in tokens]
#     return " ".join(lemmetized_tokens)
#
#
# lemm = [lemmetize_string(i) for i in preprocessed]
#
# print(list(lemm[1]))
#
# ##keyword extraction
#
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# stop_words = set(stopwords.words("english"))
#
#
#
# # Tokenizing text
#
# #
# # for (i,j) in itertools.zip_longest(cur,lemm_preprocess):
# #     primarykey = i['primarykey']
# #     tag = nltk.pos_tag(j)
# #
# #     keywords = []
# #     count = 0
# #     while count<len(tag):
# #         if (tag[count][1]== "JJ" or tag[count][1]=="RB"):
# #             keywords.append(tag[count][0])
# #         count = count + 1
# #         keywords[count] =','.join(keywords)
# #
# #         coll.update_one({'primarykey':primarykey},{'$set':{'keyword':keywords}})
# #
#
# import itertools
#
# cur = list(coll.find({},{'primarykey':1}))
#
# for i, j in itertools.zip_longest(cur, lemm):
#     if j is None:
#         continue
#     primarykey = i['primarykey']
#     tag = nltk.pos_tag(list(j))
#     print(list(j))
#
#     keywords = []
#     for word, pos_tag in tag:
#         if pos_tag == "JJ" or pos_tag == "RB":
#
#             keywords.append(word)
#
#     keyword_string = ','.join(keywords)
#     coll.update_one({'primarykey': primarykey}, {'$set': {'keyword': keyword_string}})
#
