raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", 
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]
result = [int(summ.split(':')[-1])for summ in raw_transactions if summ.startswith("SUCCES") and int(summ.split(':')[-1]) > 0]
print(result)
