with open('sample.txt','r') as file:
    print(file.readline())

with open('sample.txt','w')  as f:
    print(f.writelines("Hello Everyone"))

