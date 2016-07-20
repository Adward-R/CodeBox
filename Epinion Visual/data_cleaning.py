import codecs
from math import log2

GENRE_NUM = 18
genre_dict = {"Action": 0,
              "Adventure": 1,
              "Animation": 2,
              "Children's": 3,
              "Comedy": 4,
              "Crime": 5,
              "Documentary": 6,
              "Drama": 7,
              "Fantasy": 8,
              "Film-Noir": 9,
              "Horror": 10,
              "Musical": 11,
              "Mystery": 12,
              "Romance": 13,
              "Sci-Fi": 14,
              "Thriller": 15,
              "War": 16,
              "Western": 17
              }
genre_list = [g for g in sorted(genre_dict.keys(), key=lambda x: genre_dict[x])]
age_dict = {1: 1, 18: 2, 25: 3, 35: 4, 45: 5, 50: 6, 56: 7}

def movie_genre_stat():
    years = {}
    with codecs.open('./data/movies.txt', encoding='latin-1') as fin:
        for line in fin:
            year = int(line.split("::")[1][-5:-1])
            genre_lst = line.split("::")[2][0:-1].split("|")
            if year not in years.keys():
                years[year] = [0] * GENRE_NUM
            for genre in genre_lst:
                years[year][genre_dict[genre]] += 1

    with codecs.open('./data/movie_genre_stat.csv', 'w') as fout:
        fout.write("Year")
        for g in genre_list:
            fout.write(',' + str(g))
        for y in sorted(years.keys()):
            fout.write('\n' + str(y % 1900))
            for g in years[y]:
                fout.write(',' + str(g))
'''
movieID - GenreList - RateList - (UserList) - AgeList
'''
decades = ['before 50s', '50s', '60s', '70s', '80s', '90s'] #2000 for latest

def readMovieDecade(): #movie -> decade
    """
    :rtype: List[List[int]]
    """
    movieDacade = []
    for i in range(3953):
        movieDacade.append([])
    with codecs.open('./data/movies.txt', encoding='latin-1') as fin:
        for line in fin:
            movieId = int(line.split("::")[0])
            year = int(line.split("::")[1][-5:-1])
            movieDacade[movieId] = int(max(year - 1941, 0) / 10)
    return movieDacade

def readMovieInfo(): #movie -> List[genre]
    """
    :rtype: List[List[int]]
    """
    movieIndex = []
    for i in range(3953):
        movieIndex.append([])
    with codecs.open('./data/movies.txt', encoding='latin-1') as fin:
        for line in fin:
            movieId = int(line.split("::")[0])
            genre_lst = line.split("::")[2][0:-1].split("|")
            for genre in genre_lst:
                movieIndex[movieId].append(genre_dict[genre])
    return movieIndex

def readUserInfo(): #user -> age_period
    """
    :rtype: List[int]
    """
    userIndex = [0]
    with codecs.open('./data/users.txt', encoding='latin-1') as fin:
        for line in fin:
            userIndex.append(int(line.split("::")[2]))
    return userIndex

movieDecade = readMovieDecade()
movieIndex = readMovieInfo()
userIndex = readUserInfo()

clusterJson = []
for age in age_dict:
    clusterJson.append({"values": [], "total": 0})
    for i in range(6):
        clusterJson[-1]["values"].append({"ele": 0, "type": decades[i]})

mat = []
for i in range(GENRE_NUM):
    mat.append([])
    for j in range(3):
        mat[-1].append([0] * 8)

with codecs.open('./data/ratings.txt', encoding='latin-1') as fin:
    for line in fin:
        userId, movieId, rating = line.split("::")[0:3]
        userAge = userIndex[int(userId)]
        gen_lst = movieIndex[int(movieId)]
        rate = 0
        if int(rating) == 3:
            rate = 1
        elif int(rating) > 3:
            rate = 2
            #clusterJson[age_dict[userAge]-1]["total"] += 1
            clusterJson[age_dict[userAge]-1]["values"][movieDecade[int(movieId)]]["ele"] += 1

        for g in gen_lst:
            mat[g][rate][0] += 1
            mat[g][rate][age_dict[userAge]] += 1

for cir in clusterJson:
    #cir["total"] = log2(cir["total"])
    totalNum = 0
    for dictt in cir["values"]:
        dictt["ele"] = log2(dictt["ele"])
        totalNum += dictt["ele"]
    cir["total"] = totalNum

with codecs.open('./data/cluster_jiarui.json', 'w') as fout:
    fout.write(str(clusterJson).replace("'", '"'))

donut = []
stackedBar = []
for g in mat:
    stackedBar.append([])
    for r in g:
        donut.append(r[1:])
        stackedBar[-1].append(r[0])

with codecs.open('./data/donut_jiarui.json', 'w') as fout:
    fout.write(str(donut))

with codecs.open('./data/stacked_bar_jiarui.json', 'w') as fout:
    fout.write(str(stackedBar))

