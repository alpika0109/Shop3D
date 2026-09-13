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
def train(text,vocab_size,verbose=False):
    tokens = list(text.encode("utf-8"))
    num_merges = vocab_size - 256
    new_minted_token = 256
    merges = {}
    for i in range(num_merges):
        pair_counts = count_pairs(tokens)
        if not pair_counts:
            break 
        most_frequent_pair = max(pair_counts,key=pair_counts.get)
        most_frequent_pair_str = "".join([chr(x) for x in most_frequent_pair])
        new_tokens = merge(tokens,most_frequent_pair,new_minted_token)
        if verbose:
            print(f"Most Frequent Pair: {most_frequent_pair} == \"{most_frequent_pair_str}\" --> ({new_minted_token}) Occurs {pair_counts[most_frequent_pair]} times ")
        merges[new_minted_token] = most_frequent_pair
        tokens = new_tokens
        new_minted_token += 1

    return tokens,merges
def decode(tokens,merges):
    decoded_list = []
    for tkn in tokens:
        memo = []
        decoded_list.extend(decode_token(tkn,merges,memo))
    return decoded_list
