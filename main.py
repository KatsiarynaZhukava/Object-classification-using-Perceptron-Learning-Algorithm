import random

class Object:
    def __init__(self, x, y, z, number_of_classes):
        self.x = x
        self.y = y
        self.z = z
        if number_of_classes > 0:
            self.object_class = random.randint(0, number_of_classes - 1)

    x = 0
    y = 0
    z = 0
    object_class = -1000


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


print("Enter the number of classes: ")
N = int(input())

print("Enter the number of objects: ")
number_of_objects = int(input())


objects = []
weights = []

d = [None] * N
c = Object(1, 1, 1, 0)


for i in range(number_of_objects):
    objects.append(Object(random.randint(-5, 5), random.randint(-5, 5), 1, N))
for i in range(N):
     weights.append(Object(0, 0, 0, 0))
corrected = True

iterations_counter = 0
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
    iterations_counter += 1

print("Finished")
for i in range(weights.__len__()):
    print("d[{}](x) = {} * x1 + {} * x2 + {}".format(i, weights[i].x, weights[i].y, weights[i].z))
