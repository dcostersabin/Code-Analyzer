class Testing:

    def setup(params):
       a = list()
       for i in range(params):
       for j in range(params + 1):
       print(i + j)
       a.append(i + j)
     
    if __name__ == "__main__":
        setup(100)
