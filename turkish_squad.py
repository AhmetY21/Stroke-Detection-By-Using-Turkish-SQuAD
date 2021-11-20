
def q_a(text,questions,question_col = 'Sorular',output_cols = ['Sorular','Muhtemel Cevap','Güven Değeri']):
  temp = pd.DataFrame()
  temp
  for i in range(len(questions)):
    ans = nlp(question=questions.iloc[i][question_col], context=text)
    aq = ans['answer']
    ass = ans['score']
    temp1 = pd.DataFrame([questions.iloc[i]['Sorular'],aq,ass]).T
    temp1.columns = output_cols
    temp = pd.concat([temp,temp1],axis=0)
    
  return temp

