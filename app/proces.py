def count_classes(data):
    class_counts = {}
    classes = data['Clase']
    for c in classes:
        if c not in class_counts:
            class_counts[c] = 0
        class_counts[c] += 1
    return class_counts