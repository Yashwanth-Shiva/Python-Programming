#Referred from JOVIAN pythondsa.com course
def BinarySearch(arr,query):
    low,high=0,len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        result=test_location(arr,mid,query)
        if result=="found":
            return mid
        elif result=="left":
            high=mid-1
        elif result=="right":
            low=mid+1
    return -1

def test_location(arr,mid,query):
    if arr[mid]==query:
        if mid-1>=0 and arr[mid-1]==query:
            return "left"
        else:
            return "found"
    elif arr[mid]<query:
        return "left"
    else:
        return "right"

tests=[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}]


for test in tests:
    print(test["input"]["cards"],test["input"]["query"])
    print(BinarySearch(test["input"]["cards"],test["input"]["query"]))
