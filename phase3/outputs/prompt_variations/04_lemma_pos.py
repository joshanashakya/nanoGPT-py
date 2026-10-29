import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

sample = state_union.raw("1993-Clinton.txt")[:1002]

# 1. POS tagging
big = {}
# 2. Button-3: Change the CLF references
big[2] = -32.7  # Tagging (default: Change)
big[3] = 1.0
big[1] = -32.7  # POS tagging
big[4] = 1.0
big[7] = -32.7  # Works of 32-bit Button-3.txt,
big[4] = -36.81  # Hoy-long
big[5:55] = 0.01  # Swap petal (default: Change)
big[4] = -36.81  # Works (with no things)
big[5:55] = -32.47
big[2] = -35.81  # Works 1.0

# 3. Powerswarm Clwave 2005 from the notebook:
# gold wiwo-closed bank up of a cloyte 2.


# Since the WordNet references are the CLF BlDam 2005