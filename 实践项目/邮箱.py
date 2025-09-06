import sys
def email_is_valid(email: str) -> bool:
    """
    验证邮箱格式是否正确
    """
    if email[0]in ['.','@'] or email[-1] in ['.','@']:
       return False
    if email.count('@')!=1:
        return False
    index_at=email.find('@')
    if email[index_at+1]=='.'or email[index_at-1]=='.':
        return False
    if email[index_at+1:].count('.')==0:
        return False
    return True
for line in sys.stdin.readlines():
    email=line.strip()
    if email_is_valid(email):
        print("YES")
    else:
        print("NO")