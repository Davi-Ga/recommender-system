from search import get_similarities

def calculate_item_similarities(dataset):
    similarities={}
    for item in dataset:
        similarity=get_similarities(dataset,item)
        similarities[item]=similarity
        
    return similarities

def get_item_recommendations(dataset,user):
    totals={}
    simSums={}
    item_similarities=calculate_item_similarities(dataset)
    
    for (item,rating) in dataset[user].items():
        for (similarity,item2) in item_similarities[item].items():
            if item2 in dataset[user]:
                continue
            totals.setdefault(item2,0)
            totals[item2]+=similarity*rating
            simSums.setdefault(item2,0)
            simSums[item2]+=similarity
    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings