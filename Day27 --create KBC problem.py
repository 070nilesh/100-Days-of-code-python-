# create a program displaying questions to the users like KBC, use list datatype to store the questions and their correct answers, display the final amount the person is taking home after playing the game

question_list =["1.which country is delhi located in?","2.what is the capital of India?","3.where is qutub minar?","4.what is the capital of bihar?","5.who is the cricketer?", "6.The weight of diamonds is usually measured in what?", "7.who is the prime minister of pakistan?", "8.who is the bowler of cricket?", "9.what is the capital of bangladesh?", "10.where is new york?"]
first_option  = ["a.India","a.bihar","a.mumbai","a.madhubani","a.sania mirza","a.tola", "a.Imran khan", "a.murli vijay", "a.turkey", "a.UK"]
second_option =["b.america","b.punjab","b.delhi","b.noida","b.Ms dhoni", "b.carat", "b.banjir bhutto", "b.ishant sharma", "b.islamabad", "b.USA"]
third_option  = ["c.pakistan","c.delhi","c.himachal pradesh","c.patna","c.usain bolt", "c.Maund", "c.Nawaz sarif", "c.mickal clarke", "c.dhaka", "c.India"]
fourth_option =["d.Nepal","d.uttar pradesh","d.kanpur","d.MP","d.modi", "d.Troy", "d.modi", "d.virat kohli", "d.delhi", "d.pakistan"]

ans_key=["a","c","b","c","b", "b", "a", "b", "c", "b"]

a = 0
while a<len(question_list):
    print(question_list[a])
    print(first_option[a])
    print(second_option[a])
    print(third_option[a])
    print(fourth_option[a])

    user = input("Answer: ")
    if user == ans_key[a]:
        print("write answer")
    else:
        print("wrong answer")
        break
    a = a+1
