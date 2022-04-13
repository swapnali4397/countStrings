def countStrings(self, n):
     MOD = 10**9 + 7
	    a=[0 for i in range(n)]
	    b=[0 for i in range(n)]
	    a[0] = b[0] = 1
	    for i in range(1,n):
	        a[i] = (a[i-1]%MOD + b[i-1]%MOD )%MOD
	        b[i] = a[i-1] %MOD
     
     return (a[n-1]%MOD + b[n-1]%MOD )%MOD;
 
 
print(countStrings(3))

