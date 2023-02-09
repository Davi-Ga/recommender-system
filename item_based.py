from search import get_similarities

def calculate_item_similarities(dataset):
    similarities={}
    for item in dataset:
        similarity=get_similarities(dataset,item)
        similarities[item]=similarity
        
    return similarities