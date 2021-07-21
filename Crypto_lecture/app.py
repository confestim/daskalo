import subprocess
import os, re
from flask import render_template, Flask, request
from config import auth

app = Flask(__name__)

# environment variables (VERY SENSITIVE)
os.environ["WEB3_PRIVATE_KEY"]=auth["private_key"]
os.environ["WEB3_RPC_URL"]=auth["rpc_url"]
os.environ["WEB3_ADDRESS"] = auth["contract_address"]

# get balance on token
def get_token_balance():
    return subprocess.check_output(["web3", "balance","--erc20"]).decode("utf-8")

# get eth balance
def eth_balance():
    return subprocess.check_output(["web3", "balance"]).decode("utf-8")


@app.route('/', methods=['post','get'])
def index():
    try_again = None
    if request.meth od == "POST":
        address = request.form.get("address")
        if os.path.isfile("./log.txt"):
            f = open("log.txt","r")
            lines = f.readlines()
            
            if address in lines:
                print(request.remote_addr + " tried to cheat us!")
                f.close()    
                return render_template("nope.html")
            elif not bool(re.match(r"/^0x[a-fA-F0-9]{40}$/", f"{address}")):
                try_again = True
                return render_template("index.html", try_again=try_again)           
            else:
                f.close()    
                
                f = open("log.txt", "a")
                f.write(f"\n{address}")
                print(get_token_balance())
    return render_template("index.html", tokens=get_token_balance(), try_again=try_again)