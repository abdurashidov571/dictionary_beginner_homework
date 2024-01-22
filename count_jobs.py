def count_jobs(data:list, job:str) -> int:
    k=0
    for i in data:
        if i['job']==job:
          k+=1
    return k
data=[
  {
    'name': 'John', 
    'job': 'Developer'
  }, 
  {
    'name': 'Mary', 
    'job': 'Developer'
  }
  ]
job = 'Developer'
print(count_jobs(data,job))