def count_pairs(tokens):
   counts = {}
    for pair in zip(tokens,tokens[1:]):
        counts[pair] = counts.get(pair,0) + 1
    return counts
def merge(current_tokens,most_frequent_pair,new_token):
    new_token_list = []
    i = 0 
