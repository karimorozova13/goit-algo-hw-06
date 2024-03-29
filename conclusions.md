# Взаємодія між різними видами в екосистемі

### Breadth-First Search

Обходить граф рівень за рівнем, відштовхуючись від стартового вузла. Тому спочатку з Tree він спуститься до Bat, Bird, Beetle, а потім на рівень нижче: Grass. Тому ми і отримаємо результат:

           Tree
        /   |   \
    Bat   Bird  Beetle
            |
          Grass

[('Bat', 'Tree'), ('Tree', 'Bird'), ('Tree', 'Beetle'), ('Bird', 'Grass')]

### Depth-First Search

Обходить граф глибше, доки не досягне кінця одного гілля графа, а потім повертається та рухається іншим гіллям. Як ми бачимо, з Tree він іде спочатку до Bat, далі спускатись немає куди і повертається на початок. Потім відвідує Bird, звідти іде до Beetle, а звідти до Grass. Так, алгоритм відвідав усі вершини, опускаючись у глибину і маємо такий результат:

        Tree
        /  |
    Bat   Bird
            |
          Beetle
            |
          Grass

[('Bat', 'Tree'), ('Tree', 'Bird'), ('Bird', 'Beetle'), ('Beetle', 'Grass')]
