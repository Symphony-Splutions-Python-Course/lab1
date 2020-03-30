def spiralPrint(m, n, a):
    k = 0
    l = 0

    while (k < m and l < n):       
        # Printaj go prviot red od ostanati redovi  
        for i in range(l, n) : 
            print(a[k][i], end = " ") 
              
        k += 1
  
        # Printaj ja poslednata kolona od ostanati koloni
        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
              
        n -= 1
  
        # Printaj go posledniot red od ostanati redovi 
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
              
            m -= 1
          
        # Printaj ja prvata kolona od ostanati koloni 
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
              
            l += 1

if __name__ == '__main__':
    m = int(input('broj na redovi, m = '))
    n = int(input('broj na koloni, n = '))
    matrix = []
# inicijaliziraj broj na redovi
    for i in range(0,m):
        matrix += [0]
# inicijaliziraj ja matricata
    for i in range (0,m):
        matrix[i] = [0]*n
    for i in range (0,m):
        for j in range (0,n):
            print ('vnesi vo red: ',i+1,' kolona: ',j+1)
            matrix[i][j] = input()
    red=m
    kolona=n
    spiralPrint(red,kolona,matrix)