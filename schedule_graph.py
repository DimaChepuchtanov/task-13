import random
from typing import Optional
import networkx as nx
import matplotlib.pyplot as plt


DEFAULT_TREE_COUNT = 7
DEFAULT_VERTEX_COUNT = 30


class ScheduleGraph:
    @staticmethod
    def genterate_random_number(count_of_number: int)-> list[int]:
        a = list()
        b = list()
        for i in range(count_of_number):
            b.clear()
            for j in range(count_of_number):
                b.append(random.randint(0,1))
            a.append(b) 
            

    
        
        return a





    @staticmethod
    def generate_random_forest(tree_count: Optional[int] = None,
                               vertex_count: Optional[int] = None) -> nx.Graph:
        leter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
        temp = vertex_count
        trees = [0]*tree_count
        graph = nx.Graph()
        if(tree_count == 1):
            trees[1] = vertex_count
        else:
            for i in range(0, tree_count):   #в цикле рандомно получаем кол-во узлов в дереве
                if(i == tree_count - 1):     #проверка на поледний элемент, чтоб присвоить ему остаток общей суммы узлов
                    if(temp == 0):
                        trees[i-1] -= 1      # тут чекаем чтоб не ноль был остаток если ноль то из предыдущего дерева вычитаем 1 и к последнему прибавляем её
                        trees[i] = 1
                    else:
                        trees[i] = temp
                    break
                else:
                    if(temp / 2 - 1 <= 2):
                        trees[i] = 2
                        temp -= 2
                        continue
                    trees[i] = random.randint(2, round(temp/2) - 1)
                    temp -= trees[i]
        print(trees)
        letters_for_trees = [0]*len(trees)
        s = 0
        for i in range(0, len(trees)):     # цикле присваиваем буквы вершинам тут думаю плюс минус поймёшь чё происходит
            new_letters = [0]*trees[i]
            for j in range(0, trees[i]):
                if(s <= 25):
                    new_letters[j] = leter[s]
                    s += 1
                else:
                    new_letters[j] = leter[s-26]+leter[s-26+1]
                    s += 1
            letters_for_trees[i] = new_letters
        print(letters_for_trees)
        for i in range(len(trees)):
            mass = ScheduleGraph.genterate_random_number(trees[i])
            names = letters_for_trees[i]
            first_point = names[0]
            last_point = names[-1]
            for j in range(len(mass)):
                flag = False
                graph.add_node(names[j])
                for z in range(len(mass)):
                    if mass[j][z] == 1 and j!=z and flag !=False:
                        flag = True
                        if z < len(mass):
                            graph.add_node(names[z])
                            graph.add_edge(j,z,weight = 1)
                        else:
                            flag = False                             
         
            ScheduleGraph.show_plot(graph)
                        
                        
        
        



    @staticmethod
    def show_plot(graph: nx.Graph) -> None:
        nx.draw_planar(graph,with_labels=True)
        plt.show()

def __usage_example():
    G = ScheduleGraph()
    G.generate_random_forest(DEFAULT_TREE_COUNT, DEFAULT_VERTEX_COUNT)


if __name__ == '__main__':
    __usage_example()
