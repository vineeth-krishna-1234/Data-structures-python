import urllib.request
api_url="https://random-word-api.herokuapp.com/word?number=1"
actual_word=urllib.request.urlopen(api_url).read().decode("utf-8").strip('"][')
output=["_" for i in range(len(actual_word))]
tries=0
while True:
    
    user_guess=input("Enter your guess:")
    tries+=1
    for i in range(len(actual_word)):
        if actual_word[i]==user_guess:
            output[i]=user_guess
    
    print("".join(output))
    if "_" not in output:
        print(f"volia!!! you took {tries} tries")
            