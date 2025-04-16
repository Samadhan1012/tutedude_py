list = []
five_elements = []
for i in range(1,11):
    list.append(i)

print(f"Orignal list: {list}")
five_elements = list[:5]
print(f"Extracted first five elements: {five_elements}")
five_elements.reverse()
print(f"Reversed extracted elements: {five_elements}")
