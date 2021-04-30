def FakeSticker(to, spkg,sid, mids=[]): #DONE
    if clientMID in mids: mids.remove(clientMID)
    parsed_len = len(mids)//150+1
    result = '「 Mention Members 」\n'
    mention = '@MinzTeambot\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*150:(point+1)*150]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            client.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees}),'STKPKGID':spkg,'STKID':sid}, 7)
        result = ''

def FakeContact(to, tag, mids=[]): #DONE
    if clientMID in mids: mids.remove(clientMID)
    parsed_len = len(mids)//150+1
    result = '「 Mention Members 」\n'
    mention = '@MinzTeambot\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*150:(point+1)*150]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            client.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees}),'mid':tag}, 13)
        result = ''
        
 def FakeGift(to, mids=[]): #DONE
    if clientMID in mids: mids.remove(clientMID)
    parsed_len = len(mids)//150+1
    result = '「 Mention Members 」\n'
    mention = '@MinzTeambot\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*150:(point+1)*150]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            client.sendMessage2(to, result, {'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5','MENTION': json.dumps({'MENTIONEES': mentionees})}, 9)
        result = ''
