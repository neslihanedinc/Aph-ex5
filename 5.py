def vowel_count(text):
    vowels=("aeiouAEIOU")
    vowel_count=0
    for char in text:
        if char in vowels:
            #char, "character" (karakter) kelimesinin kısaltmasıdır.
            vowel_count+=1
    return vowel_count
while True:
    try:
        user_input=input("Enter a sentence(or type 'exit' to quit): ")
        if user_input.lower=='exit':
            break
        else:
            result= vowel_count(user_input)
            print(f"Number of vowels of the text: {result}")
        
    except Exception as e:
        print(f"an error occured:{e}")



