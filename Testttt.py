import json
import requests


######## FOR JIFFY ########
#base_url = self.orang_base
#app_category = self.project_appgroup
#app_name = self.release_app
#jiffy_headers = self.get_server_call_headers()
#jiffy_headers['Content-type'] = "application/json"
###########################


# ######## FOR LOCAL ########
 api_token = 'd6dc1ddf-78f3-458a-a460-c441a09b1fbd'
 jiffy_headers = {
     'Authorization' : f'Token {api_token}',
     'Content-type' : 'application/json'
 }
 base_url = 'https://saasvaap.demo3.jiffy.ai'
 app_category = 'Saasvaap Project'
 app_name = 'Saasvaap Budget Planning Process'
 ###########################


query_url = f"{base_url}/docube/mangrove/data/query/sql"

def get_tableValues(query_string):
    insert_data = {
        'query': query_string,
        'appGroup' : app_category,
        'app': app_name
    }
    response_string = requests.post(query_url, data=json.dumps(
        insert_data), verify=False, headers=jiffy_headers, timeout=100)
    # print(f'{insert_data}\n{response_string.text}')
    return json.loads(response_string.text)
uuid =''
mainuuid =''
table_name = 'Request_Table_copy'
table_name1 = 'Request_Table'

query_string = "select [UUID],[Log_Report] from {{"+table_name+"}} where [UUID] = '"+uuid+"'"
table_data = get_tableValues(query_string)

table_data = table_data['result'][0]
log_report = table_data.get('Log_Report','')

log_report = json.loads(str(log_report))
for item in log_report:
    item['DELETE_RECORD_FLAG'] = 'true'

query_string1 = "select [UUID],[Log_Report] from {{"+table_name1+"}} where [UUID] = '"+mainuuid+"'"
table_data1 = get_tableValues(query_string1)

table_data1 = table_data1['result'][0]
new_log = table_data1.get('Log_Report','')

new_log = json.loads(str(new_log))


new_log = new_log+log_report

data = {
    'UUID' : uuid,
    'Log_Report' : new_log
}

update_data = [data]

#insertUrlInvProcQ = '{0}/docube/api/jiffytable/path/{1}/{2}/{3}/upsert/'.format(
  #  self.orang_base, self.project_appgroup, self.release_app, table_name)
#response_string = requests.post(insertUrlInvProcQ, data=json.dumps(update_data), verify=False, headers=jiffy_headers, timeout=100)

print(table_data1)