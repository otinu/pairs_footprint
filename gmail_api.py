from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# 独自ラベルのIDを別ファイルで管理
import my_label

SCOPES = "https://www.googleapis.com/auth/gmail.modify"
store = file.Storage("storage.json")
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build("gmail", "v1", http=creds.authorize(Http()))

user_id = "me"
label_id_one = "INBOX"
label_id_two = my_label.MyLabel.name

unread_msgs = (
    GMAIL.users()
    .messages()
    .list(userId=user_id, labelIds=[label_id_one, label_id_two])
    .execute()
)

mssg_list = unread_msgs["messages"]
m_id = mssg_list[0]["id"]  # 対象ラベルの最新メールだけ取得
message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()
mail_body = message["snippet"]

print(mail_body[6:12])