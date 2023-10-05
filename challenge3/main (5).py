def LinearSearchProduct(productlist, targetproduct):
    indices = []

    for index,product in enumerate(productlist):
        if product == targetproduct:
            indices.append(index)
    return indices 

products = ["apple", "banana", "orange", "apple", "grape"]
target = "apple"
result = LinearSearchProduct(products, target)
print(result) 