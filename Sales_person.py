import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  # DF = pd.merge(orders, company, on= ['com_id'], how = 'left')
  # DF = DF[(DF['name']== 'RED')]
  # print(DF)
  # return sales_person[['name']][(~sales_person['sales_id'].isin(DF['sales_id']))]

  Dict = {}
  res= []
  result =[]
  R_company_id = company['com_id'][(company['name'] == 'RED')].tolist()
  for i in range(len(orders)):
    
    com_id = orders['com_id'][i]
    sales_id = orders['sales_id'][i]
    if com_id not in Dict:
      Dict[com_id] = []
    Dict[com_id].append(sales_id)

  for key, values in Dict.items():
    if key in R_company_id:
      # res.extend(values)
      for items in values:
        res.append(items)

  DF = pd.DataFrame(res, columns= ['sales_id'])  
  print(res)


  return sales_person[['name']][(~sales_person['sales_id'].isin(DF['sales_id']))]
 
    