class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
def find_max_area(lst,n):
    # find the maximum area under given historgram with n bars
    
    s = Stack() # empty stack
    max_area = 0 # initalize max area
    i=0
    while i < n:
        # if this bar is higher than the bar on top stack, push it to stack
        if s.isEmpty() or lst[s.peek()-1] <= lst[i] :
            i += 1
            s.push(i)
        else :
            tp = s.peek()-1
            s.pop()
            area_with_top = lst[tp] * (i if s.isEmpty() else i - s.peek())
            
            if max_area < area_with_top:
                max_area = area_with_top
                
    while s.isEmpty() == False:
        tp = s.peek()-1
        s.pop()
        area_with_top = lst[tp] * (i if s.isEmpty() else (i -s.peek()))
        
        if max_area < area_with_top:
            max_area = area_with_top        
        
        
    return max_area


if __name__ == '__main__':
    with open('./Input','r') as f:
        with open('Output','w+') as f2:
            data = f.readlines()
            for row in data:
                input_ = list(map(int,row.split(',')))
                output = find_max_area(input_,len(input_))
                f2.write(str(output)+'\n')