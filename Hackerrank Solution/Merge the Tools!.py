def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        list1=[]
        #spliting the string into n/k substrings
        s=string[i:i+k]
        for j in s:
          #Removing the duplicates characters 
            if j not in list1:
                list1.append(j)
        #Joining and printing list1 characters
        print("".join(list1))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
