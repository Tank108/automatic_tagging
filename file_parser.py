import getpass
from keybert import KeyBERT
from tika import parser
from pprint import pprint
from keyphrase_vectorizers import KeyphraseTfidfVectorizer
from pathlib import Path


def content_parser(filepath, password=None):

    parsed_file = parser.from_file(filepath)
    content = parsed_file['content']
    meta = parsed_file['metadata']
    # pprint(meta)
    # print(content)
    return content


def keyword_extractor(content,num=10):
    kw = KeyBERT()
    keywords = kw.extract_keywords(content, vectorizer=KeyphraseTfidfVectorizer(), top_n=num)
    # pprint(keywords)
    return keywords


def text_tag_generator(filepath):
    content = content_parser(filepath)
    tags = keyword_extractor(content)
    print(tags)
    print(type(tags))
    return tags


def extension_finder(filepath):
    file_extension = Path(filepath).suffix
    return file_extension





# filepath = r'X:\Java\EICT-NB algorithm and its implementation.pdf'
# filepath = r'C:\Users\DELL\Documents\Image Classification using.pptx'
# filepath = r'C:\Users\DELL\Documents\SL.xlsx'
# filepath = 'https://economictimes.indiatimes.com/small-biz/sme-sector/how-shell-the-worlds-second-largest-oil-and-gas-company-wants-to-achieve-net-zero-emission-targets/articleshow/99657046.cms'

# tags = tag_generator(filepath)






