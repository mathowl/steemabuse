from datetime import datetime, timedelta
from beem.account import Account
from beem.amount import Amount
from beem.nodelist import NodeList



def memos_blacklist(user_c,m_days):
    
    """
    Given a steem-user and #days, returns memos in which the word blacklist appears.
    :param str user_c: steem user
    :param int m_days: number of days 
    :rtype: list str with memos containing blacklist
    """
    nodes = NodeList().get_nodes()
    stm = Steem(node=nodes)
    set_shared_steem_instance(stm)
    acc = Account(user_c,steem_instance=stm)
    
    stop_time = datetime.now()
    start_time = stop_time - timedelta(m_days)
    blist = []
    mem_memo = set()
    
    for mem in acc.history(start=start_time, stop=stop_time,only_ops=['transfer']):
        
        #make the text lower case
        newmem = mem['memo'].lower()
        # find memos which contain the word blacklist and only consider unique transaction senders
        if newmem.count('blacklist') > 0 and mem['from'] not in mem_memo  : 
                b_list = blist.append(mem['timestamp'] + '|' + mem['from'] + '|' +  mem['memo'] +' <br>') 
                mem_memo.add(mem['from'])
    return blist

