student_data={"id1":{"studentname":"Sara","grade":"V","subject intregation":"english, math, science"},
              "id2":{"studentname":"Josh","grade":"V","subject intregation":"english, math, science"},
              "id3":{"studentname":"David","grade":"V","subject intregation":"english, math, science"},
              "id4":{"studentname":"Sara","grade":"V","subject intregation":"english, math, science"}}
result={}
seen_keys=[]
for student_id,details in student_data.items():
    unique_keys={details["studentname"],details["grade"],details["subject intregation"]}
    
    if unique_keys not in seen_keys:
        
        seen_keys.append(unique_keys)
        result[student_id]=details
for k,v in result.items():
    print(k,":",v)
        

