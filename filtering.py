
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

def confidence_interval(x,min_well=0.8,min_good=0.5,min_medium=0.2):
  if x>min_well:
    return 10
  elif min_well>x>min_good:
    return 5
  elif min_good>x>min_medium:
    return 2
  else:
    return 0.1

def hack_4_treat(text,questions,question_col = 'Sorular',drop_1 = 'Grup',drop_2 = 'Grup_Aciklama'):
  text = text
  que = questions
  temp = q_a(text,que)
  
  temp = temp.merge(que,how='left',on= question_col).drop([drop_1,drop_2],axis=1)


  return temp

def threshold_checker(x,y,high=1,low=0):
  z=0
  if x.isnumeric():
    x=int(x)
    if high:
      if x>y:
        #print("Hastanın değeri beklenilenin üstünde")
        z=1
      else:
        pass
    if low:
      if x<y:
        #print("Hastanın değeri beklenilenin altında")
        z=1
      else:
        pass
    else:
      pass
  return z

def var_control(x,keyword='var'):
  if keyword in x:
    y=1
  else:
    y=0

  return y

def use_control(x,keyword='kullanıyor'):
  if keyword in x:
    y=1
  else:
    y=0

  return y

def is_positive(x,label_col = 'label'):
  senti = sa(x)
  if senti[0][label_col] =='negative':
    return 1
  else:
    return 0

def confidence_checker(df,confidence_level_col='Güven Değeri'):
  df = df[~(df[confidence_level_col] < 0.2)]
  return df

def manuel(df): # This function will be revisited
  df['YoDa'] = df[['X_Var','X_Use','Esik_deger_sikintisi']].apply(lambda x:x[0]|x[1]|x[2],axis=1)
  df = df[df['YoDa']==1]
  return df

def Risk_Score(df,onem='Onem',max_val=12):
  actual_sum = df[onem].sum()

  if actual_sum > max_val:
    print('Riskli')
  else:
    print('Risksiz')

def old_school(df):
  df['X_Var'] = df['Muhtemel Cevap'].apply(lambda x:var_control(x))
  df['X_Use'] = df['Muhtemel Cevap'].apply(lambda x:use_control(x))
  df['Esik_deger_sikintisi'] = df[['Muhtemel Cevap','Esik_deger']].apply(lambda x:threshold_checker(x[0],x[1]),axis=1)

  return df

def ad_hoc_filter(df):
  df = confidence_checker(df)
  df = manuel(df)
  return df