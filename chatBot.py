import json
from difflib import get_close_matches

#load konowledge base
def LNB(file_path: str) ->dict:
     with open(file_path,'r') as file:
           data: dict = json.load(file)
     return data

#save knowledge base
def SKB(file_path: str , data: dict):
      with open(file_path,'w') as file:
       json.dump(data,file, indent =2)

#find best match
def FBM(user_question :str, questions:list[str]) ->str| None:
      matches:list = get_close_matches(user_question , questions, n=1, cutoff=0.6)
      return matches[0] if matches else None
#get answer for the question
def GAFQ(question:str , knowledge_base: dict) -> str | None:
      for q in knowledge_base["questions"]:
            if q["question"]==question:
                  return  q["answer"]
def chat_bot():
  knowledge_base: dict=LNB('doc.json')

  while True:
        user_input: str = input('You: ')
        if user_input.lower()== 'quit':
           break
        best_match: str | None  =FBM(user_input, [q["question"]for q in knowledge_base["questions"] ])
        if best_match:
           answer: str =GAFQ(best_match ,knowledge_base)
           print(f'Bot: {answer}')
        else:
           print(f'Bot: I don\'t know the answer.can you teach me?')
           new_answer: str = input('Type the answer or "skip to skip:')
      
           if new_answer.lower() != 'skip':
              knowledge_base["questions"].append ( {"question": user_input , "answer": new_answer } )
              SKB('doc.json',knowledge_base)
              print('Bot: Thank You I learend a new response!')
if __name__ =='__main__':
     chat_bot()