import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
  Dict = {}
  res = []
  for i in range(len(employee)):
    ID = employee['id'][i]
    name = employee['name'][i]
    Manager = employee['managerId'][i]

    if (Manager not in Dict):
      Dict[Manager] = 0
    Dict[Manager] +=1 

  for key, values in Dict.items():
    if values >= 5:
      res.append([key, values])

  DF = pd.DataFrame(res, columns=['id', 'count'])
  finalDF = employee[(employee['id']).isin(DF['id'])]
  print(Dict)
  
  return pd.DataFrame(finalDF['name'])
  # DF2= employee.groupby(['managerId']).agg(count= ('managerId', 'count')).reset_index()
  # DF2 = DF2[DF2['count']>=5]
  # DF = employee[(employee['id'].isin(DF2['managerId']))]

  # return DF[['name']]
    

    