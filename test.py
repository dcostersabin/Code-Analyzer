class Testing:
    
    def setup(params):
        a = list()
        for i in range(params):
            for j in range(params + 1):
                a.append(i + j)
        return a
    
    
    if __name__ == "__main__":
        setup(100)
