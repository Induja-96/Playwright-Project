import json

import pytest
@pytest.mark.asyncio
# async def test_get_acc(api):
#     res  = await api.get("customers/12212/accounts",
#                   headers={"Accept": "application/json"}, )
#     print(await res.json())
#     body = await res.text()
#     print(body)
#     assert res.status == 200
#     accounts = json.loads(body)
#     for acc in accounts:
#         print("account id:" ,acc.get("id",acc.get("customerId")))
#         print("account type:",acc.get("type"))
#         print("balance:",acc.get("balance"))
        
# @pytest.mark.asyncio
# async def test_create_acc(api):
#     cust_id = 12212
#     from_acc_id = 18894
#     res  = await api.post("createAccount",
#                           params={
#                             "customerId": cust_id,
#                               "newAccountType" : 1,
#                               "fromAccountId": from_acc_id,
#                           },
#                   headers={"Accept": "application/json"}, )
#     body = await res.json()
#     print(body)
#     #{'id': 95484, 'customerId': 12212, 'type': 'SAVINGS', 'balance': 0}       
    
  
@pytest.mark.asyncio
async def test_get_acc(api_git):
    user_name = "Induja-96"
    repo = "Playwright-Project"
    res =await api_git.get(f"repos/{user_name}/{repo}")
    data =await res.json()
    #print(data)
    # print(f"name of the repo is {data['name']}")
    # print(f"Private : {data['private']}")     
    # print(f" default branch {data['default_branch']}")
    
    # get comments
    resp = await api_git.get(f"repos/{user_name}/{repo}/commits")
    data = await resp.json()
    print(data)
    # get branch
    resp = await api_git.get(f"repos/{user_name}/{repo}/branches")
    if resp.ok:
        branches = await resp.json()
        print(branches)
        for branch in branches:
            print("-" ,branch['name'])