def count_pairs(tokens):
   counts = {}
    for pair in zip(tokens,tokens[1:]):
        counts[pair] = counts.get(pair,0) + 1
    return counts
def merge(current_tokens,most_frequent_pair,new_token):
    new_token_list = []
    i = 0 
 while i < len(current_tokens):
        if current_tokens[i] == most_frequent_pair[0] and i < len(current_tokens)-1 and current_tokens[i+1] == most_frequent_pair[1]:    
            new_token_list.append(new_token)
            i += 2
        else:
            new_token_list.append(current_tokens[i])
            i += 1
    return new_token_list
