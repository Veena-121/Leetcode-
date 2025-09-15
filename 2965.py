from collections import defaultdict
class sol:
    def find(self,grid):
        
        n= len(grid)
        count = defaultdict(int)
        
        for row in grid:
            for i in row:
                count[i] +=1
        r=m=0
        for i in range(1,n*n+1):
            if count.get(i,0)==2:
                r=i
            elif count.get(i,0)==0:
                m=i
        return[r,m]
    
def main():
    m=sol()
    print(m.find([[1,2],[2,3]]))
    
if __name__ =="__main__":
    main()