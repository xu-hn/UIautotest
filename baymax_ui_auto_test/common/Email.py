# -*- coding: utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(**kwargs):
    '''
    :param f: 附件路径
    :param to_addr:发给的人 []
    :return:
    '''
    from_addr = kwargs["mail_user"]
    password = kwargs["mail_pass"]
    # to_addr = "ashikun@126.com"
    smtp_server = kwargs["mail_host"]

    msg = MIMEMultipart()

    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('来自<%s>UI测试' % from_addr)
    msg['To'] = _format_addr(' <%s>' % kwargs["to_addr"])
    msg['Subject'] = Header(kwargs["header_msg"], 'utf-8').encode()
    msg.attach(MIMEText(kwargs["attach"], 'plain', 'utf-8'))

    if kwargs.get("report", "0") != "0":
        part = MIMEApplication(open(kwargs["report"], 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', kwargs["report_name"]))
        part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', kwargs["report_name"]))
        msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server, kwargs["port"])
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, kwargs["to_addr"], msg.as_string())
    server.quit()


def send():
    to_addr = ['jinbo.guo@inforefiner.com','kexin.zhang@inforefiner.com' ,'zhiming.wang@inforefiner.com', 'qian.feng@inforefiner.com', "haonan.xu@inforefiner.com"]
    # to_addr = ['bingjie.gu@inforefiner.com', "anchong.wang@inforefiner.com"]
    mail_host = "smtp.163.com"
    mail_user = "ruifan_test@163.com"
    mail_pass = "ruifantest2018"
    port = "465"
    header_msg = "Baymax_ui_自动化测试报告"
    attach = "Dear all:\n   附件中是本次Baymax_UI自动化执行的详细报告，有问题请随时联系！"
    report = PATH("../Report/Report.xlsx")
    send_mail(to_addr=to_addr, mail_host=mail_host, mail_user=mail_user, port=port, mail_pass=mail_pass, header_msg=header_msg, report=report, attach=attach, report_name="ui测试报告.xlsx")



if __name__ == "__main__":
    send()