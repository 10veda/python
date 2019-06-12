one = [""," one"," two"," three"," four"," five"," six"," seven"," eight"," nine"," ten"," eleven"," twelve"," thirteen"," fourteen"," fifteen"," sixteen"," seventeen"," eighteen"," nineteen"]; 
ten = ["",""," twenty"," thirty"," forty"," fifty"," sixty"," seventy"," eighty"," ninety"]; 
def t(n,s): 
    str=""; 
    if(n>19): 
        str+=ten[n//10]+one[n%10]; 
    else: 
        str+=one[n]; 
    if (n): 
        str+=s; 
    return str; 
def w(n): 
    out =""; 
    out +=t((n//10000000)," crore"); 
    out +=t(((n//100000)%100)," lakh"); 
    out +=t(((n//1000)%100)," thousand"); 
    out +=t(((n//100)%10)," hundred"); 
    if(n>100 and n%100): 
        out+="and"; 
    out+=t((n%100),""); 
    return out; 
n =int(input()); 
print(w(n)); 
  
