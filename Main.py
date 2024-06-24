from Parser import get_detail_from_url
from Get_links import *
#from Kusto_run import Execute_query,execute_rs_check

def main():  
  dump=[]
  results=get_Malpedia_data()+get_IBMXForce_data()+ get_Talos_data()+get_Sentinelone_data()+ get_Elastic_security_data()+get_Deepinstinct_data()+get_Esentire_data()+get_Aquase_data()+get_Splunk_data()+get_Fortinet_data()+get_Cyble_data()+get_Quick_heal_data()+get_ATT_data()+get_Asec_data()+get_Eset_data()+get_Pal_alto_data()+get_Proofpoint_data()+get_Google_data()+get_Volexity_data()+get_Yoroi_data()+get_Kaspersky_data()+get_hackhunting_data()+get_reliaquest_data()
  for feeds in results:
    try:
      url_data=get_detail_from_url(feeds)
      if url_data != None:
        dump.append(url_data)
      time.sleep(5)
    except:
      pass    

  f = open("dailyIOCs.txt", "w")
  for i in dump:
    f.write(str(i))
    f.write('\n')
    print(i)
    print("\n")
  f.close()

if __name__ == "__main__":
    main()