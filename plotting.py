
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import json
def load_data():
    file = open("points.json")
    data = json.load(file)
    file.close()
    
    file = open("category.txt")
    category =  int(file.readline())
    return data,category

if __name__ == "__main__":

    export,category = load_data()
    edges = None
    
    if category == 0:
        edges = [[1,5],[2,6],[3,7],[4,8],[3,4],[5,6],[6,7],[7,8],[5,8],[8,9],[7,10],[9,10]]
    elif category == 1:
        edges = [[1,5],[2,6],[3,7],[4,8],[5,6],[6,7],[7,8],[5,8],[8,9],[7,10],[9,10]]
    elif category == 2:
        edges = [[1,5],[2,6],[3,7],[4,8],[5,6],[6,7],[7,8],[5,8],[8,9],[7,10],[9,10],[11,12],[12,5],[13,14],[14,6]]
    elif category == 3:
        edges = [[1,6],[2,6],[3,6],[4,6],[5,6],[6,7],[8,9],[9,10],[8,11],[10,11],[11,12],[12,13],[10,13]]

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(export[0], export[1], export[2], 'gray')
    for edge in edges:
        ax.plot([export[0][edge[0]-1], export[0][edge[1]-1]], [export[1][edge[0]-1], export[1][edge[1]-1]],zs=[export[2][edge[0]-1],export[2][edge[1]-1]])
    plt.show()