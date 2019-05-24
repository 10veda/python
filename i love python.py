def sms_encoding(data):
    s=data.split()
    for i,x in enumerate(s):
        if not all(y in 'aeiou' for y in x.lower()):
            s[i]=''.join([y for y in x if y.lower() not in 'aeiou'])
    return' '.join(s)
    
data="I love Python"
print(sms_encoding(data))
