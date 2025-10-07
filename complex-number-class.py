class complexNumber:
    def __init__(self,real=0.0,imag=0.0):
        self.real = real
        self.imag = imag
       

    def __str__(self):  ## Magic Method /dunder method (double underscore method)

        if(self.real==0):
            return f"{self.imag}i"
        elif(self.imag<0):
            s= f"({self.real}{self.imag}i)"

        else:
            s = f"({self.real}+{self.imag}i)"
        return(s)
    
    def __add__(self,other):
        resultReal = 0
        resultImag = 0
        resultReal = self.real + other.real
        resultImag = self.imag + other.imag
        ans = complexNumber(resultReal,resultImag)
        return ans
    
    def __sub__(self,other):
        resultReal = 0
        resultImag = 0
        resultReal = self.real - other.real
        resultImag = self.imag - other.imag
        ans = complexNumber(resultReal,resultImag)
        return ans
    
    def __mul__(self,other):
        resultReal = 0
        resultImag = 0
        resultReal = self.real * other.real - self.imag * other.imag
        resultImag = self.real * other.imag + other.real * self.imag
        ans = complexNumber(resultReal,resultImag)
        return ans
    
    def __truediv__(self,other):
        resultReal = 0
        resultImag = 0
        den = other.real**2 + other.imag**2
        ans = self * complexNumber(other.real/den,(-1*other.imag)/den)
        return ans
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
 
        
        

    def conjugate(self):
        return complexNumber(self.real,-1*self.imag)

# cn = complexNumber(5,4)
# cn.conjugate()
# print(cn)
c1 = complexNumber(3,4)
c2 = complexNumber(4,5)
print(c1==c2)
# print(c1.conjugate())
        