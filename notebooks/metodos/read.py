import re
from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize


def get_text(file):
    """Reads a file and returns the text,
    stripping HTML tags and white space.
    """
    text = open(file).read()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


# la funcion la podemos definir en el notebook y usar directamente
def freq_words(url, n):
    """_summary_

    Args:
        url (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    req = request.urlopen(url)
    html = req.read().decode('utf8')
    raw = BeautifulSoup(html, 'html.parser')
    text = raw.get_text()
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    fd = nltk.FreqDist(tokens)
    return [t for (t, _) in fd.most_common(n)]
