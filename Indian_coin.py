import numpy as np
def count(deno_, n_notes, n): 
    dynamic_array=np.zeros((n+1,n_notes))
    for i in range(n_notes): 
        dynamic_array[0][i] = 1
    for i in range(1, n+1): 
        for j in range(n_notes): 
            x = dynamic_array[i - deno_[j]][j] if i-deno_[j] >= 0 else 0
            y = dynamic_array[i][j-1] if j >= 1 else 0
            dynamic_array[i][j] = x + y 
    return int(dynamic_array[n][n_notes-1]) 
  
denominations = [10, 20, 50,100,200,500,1000,2000] 
no_of_notes=len(denominations) 
total=2000
print(count(denominations, no_of_notes, total)) 
