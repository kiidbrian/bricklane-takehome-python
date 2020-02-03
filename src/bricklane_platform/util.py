import csv
from StringIO import StringIO


def group_by(items, key_func):
    result = {}
    for item in items:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


def generate_csv(fieldnames, data):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow(row)

    return output.getvalue()
