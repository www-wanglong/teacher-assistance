import requests
import json

API_KEY = "lDBoO4AsSE1OYEGVZ5SNBqKk"
SECRET_KEY = "bzAESz7DIAye1Zz3YtLOGuFkx2DZYrBC"

def main(content):
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/yi_34b_chat?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
         "stream": True
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

def get_access_token():
    """s
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main("大家好，我们第一次观察的鸽子，我我上一周和我爸爸妈妈都去我我姥爷，我姥爷家时候那正好有个鸽子，然后然后然后呢我就给他放一一点玉米，然后然后呢还还有咖啡，谢谢大家。评价下小朋友这段观察鸽子的描述，100字以内。")
