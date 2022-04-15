def timeInWords(h, m):
    
    words=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine","half"]

    if m==0:
        return words[h]+" o' clock"
    m=int(str(m).lstrip("0"))
    if m==1:
        return "one minute past "+words[h]
    if m==15 or m==30:
        return words[m]+" past "+words[h]
    if 1<=m<=30:
        return words[m]+" minutes past "+words[h]
    if m==45:
        return "quarter to "+words[h+1]
    if m==59:
        return words[60-m]+" minute to "+words[h+1]
    if 30<m<60:
        return words[60-m]+" minutes to "+words[h+1]

h = int(input().strip())
m = int(input().strip())
result = timeInWords(h, m)
print(result)
