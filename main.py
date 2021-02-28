import random
from matplotlib import pyplot as plt

MAX_VALUE = 10
COLORS = ['#f4ff01', '#75ff01', '#01f4ff', '#0175ff', '#b901ff', '#ff01c6', '#ff0147', '#ff3a01', '#ffb901', '#c6ff01',
          '#fd947d', '#fcff9b', '#b9ff9b', '#9bffce', '#9bfeff', '#9bc2ff', '#bca2ff', '#f3b3ff', '#7b172d', '#152d64']


class Object:
    def __init__(self, x, y, z, class_number):
        self.x = x
        self.y = y
        self.z = z
        self.object_class = class_number

    x = 0
    y = 0
    z = 0
    object_class = -1000


def draw(objects):
    temp_points_x = []
    temp_points_y = []
    for i in range(N):
        temp_points_x.clear()
        temp_points_y.clear()
        for j in range(objects.__len__()):
            if (objects[j].object_class == i):
                temp_points_x.append(objects[j].x)
                temp_points_y.append(objects[j].y)
        plt.scatter(temp_points_x, temp_points_y, s=1, color=COLORS[i])
    else:
        plt.title("Perceptron method", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=9)
    plt.show()


def count_d(weight, X):
    return weight.x * X.x + weight.y * X.y + weight.z * X.z


def decrease_weight(weight, X, c):
    weight.x -= c.x * X.x
    weight.y -= c.y * X.y
    weight.z -= c.z * X.z
    return weight


def increase_weight(weight, X, c):
    weight.x += c.x * X.x
    weight.y += c.y * X.y
    weight.z += c.z * X.z
    return weight


def find_max(d):
    max = d[0]
    class_number = 0
    for i in range(d.__len__()):
        if d[i] > max:
            max = d[i]
            class_number = i
    return class_number


print("Check the sample?\n1. Yes\n2. No")
answer = int(input())
if answer == 1:
    N = 3
    number_of_objects = 3
    objects = [Object(0, 0, 1, 0), Object(1, 1, 1, 1), Object(-1, 1, 1, 2)]
elif answer == 2:
    print("Enter the number of classes: ")
    N = int(input())
    number_of_objects = N
    objects = []
    for i in range(number_of_objects):
        objects.append(Object(random.randint(-MAX_VALUE, MAX_VALUE), random.randint(-MAX_VALUE, MAX_VALUE), 1, i))

d = [None] * N
c = Object(1, 1, 1, 0)

weights = []
for i in range(N):
    weights.append(Object(0, 0, 0, 0))
corrected = True

while corrected:
    corrected = False
    for i in range(number_of_objects):
        for j in range(N):
            d[j] = count_d(weights[j], objects[i])
        need_to_increase_weight = False
        for j in range(N):
            if (j != objects[i].object_class) & (d[j] >= d[objects[i].object_class]):
                weights[j] = decrease_weight(weights[j], objects[i], c)
                need_to_increase_weight = True
        if need_to_increase_weight:
            corrected = True
            increase_weight(weights[objects[i].object_class], objects[i], c)

print("Finished")
for i in range(weights.__len__()):
    print("d[{}](x) = {} * x1 + {} * x2 + {}".format(i, weights[i].x, weights[i].y, weights[i].z))

number_of_test_objects = random.randint(1000, 2000)
test_objects = []
for i in range(number_of_test_objects):
    test_objects.append(Object(random.uniform(-MAX_VALUE, MAX_VALUE), random.uniform(-MAX_VALUE, MAX_VALUE), 1, i))

for i in range(number_of_test_objects):
    for j in range(N):
        d[j] = count_d(weights[j], test_objects[i])
    class_number = find_max(d)
    test_objects[i].object_class = class_number
draw(test_objects)
