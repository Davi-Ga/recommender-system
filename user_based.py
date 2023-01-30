from .search import euclidian_distance

## Função que retorna os filmes recomendados para um usuário
def get_user_recommendation(dataset,user):
    total={}
    sum_similarity={}
    ##Loop que irá percorrer o dataset e verificar se o item está presente no dataset do usuário 1 e 2
    for otheruser in dataset:
        ##Caso o usuário seja o mesmo, a função irá ignorar
        if otheruser==user:
            continue
        ##Caso contrário, a função irá calcular a similaridade entre os usuários
        similarity=euclidian_distance(dataset,user,otheruser)
        
        ##Caso a similaridade seja 0, a função irá ignorar
        if similarity == 0:
            continue
        
        ##Caso contrário, a função irá calcular a nota total e a similaridade total para cada item
        for item in dataset[otheruser]:
            ##Caso o item não esteja presente no dataset do usuário, a função irá definir o valor como 0
            if item not in dataset[user]:
                total.setdefault(item,0)
                ##A nota total será a nota do outro usuário multiplicada pela similaridade
                total[item]+=dataset[otheruser][item]*similarity
                ##A similaridade total será a similaridade
                sum_similarity.setdefault(item,0)
                sum_similarity[item]+=similarity
    ##Calcula a média ponderada para cada item e retorna a lista de recomendações
    recommendations=[(total/sum_similarity[item],item) for item,total in total.items()]
    recommendations.sort()
    recommendations.reverse()
    
    return recommendations

## Função que imprime as recomendações de um usuário
def print_user_recommendation(recommendations,min_score):
    for movie in recommendations:
        if movie[0] >= min_score:
            print(movie[1])