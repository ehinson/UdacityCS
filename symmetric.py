# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(list):
    i = 0
    j = 0
    m = 0
    
    #row = list[i]
    col = []
   
    row_len = 0
    col_len = len(list)
    
    for item in list: # get row length
        for e in item:
            
            if item.index(e)>= m:
                m = item.index(e)
                row_len = m + 1
                
 
    if row_len != col_len: # check to see if rows and columns are the same length
        return False 
        
    while j < col_len and i < row_len: # go through rows and columns 
        col.append(list[j][i]) # build a column list to compare to the rows
        j += 1
        if j== col_len:
            if col == list[i]: # the full list
                i += 1
                col = []
                j = 0
              
            else: #j == col_len and col != list[i]:
                return False
            
            
            
    return True
print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False