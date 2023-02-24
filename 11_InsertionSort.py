# creating a function for insertion  
def insertion_sort(alist):  
  
        # Outer loop to traverse through 1 to len(alist)  
        for i in range(1, len(alist)):  
  
            value = alist[i]  
  
            # Move elements of alist[0..i-1], that are  
            # greater than value, to one position ahead  
            # of their current position  
            j = i - 1  
            while j >= 0 and value < alist[j]:  
                alist[j + 1] = alist[j]  
                j -= 1  
            alist[j + 1] = value  
        return alist  
            # Driver code to test above  
  
alist = [54,26,93,17,77,31,44,55,20]  
insertion_sort(alist)
  
print(alist)  