import requests,json
import pandas as pd
data={
    # 'fajhh': '34379',
    # 'jhxn': '2020-2021-1-2',
    'xq': 0,
    'jc': 0
}
headers={
    'Cookie': ''
}
if __name__ == '__main__':
    a=requests.post('http://jwxt.imu.edu.cn/student/courseSelect/freeCourse/courseList',headers=headers,data=data).text
    a=json.loads(a)
    b=json.loads(a['rwRxkZlList'])
    list_bei=[]
    list_nan=[]
    list_sum=[]
    df_nor = pd.DataFrame(columns=['课程名','课程号','课序号','校区','上课时间','教师','开设院系','课余量','总量'])
    df_sou=pd.DataFrame(columns=['课程名','课程号','课序号','校区','上课时间','教师','开设院系','课余量','总量'])
    df=pd.DataFrame(columns=['课程名','课程号','课序号','校区','上课时间','教师','开设院系','课余量','总量'])
    df_nor_n=0
    df_sou_n=0
    df_n=0
    for item in b:
        df.loc[df_n] = [item['kcm'],item['kch'],item['kxh'],item['kkxqm'],'星期%s第%s-%s节'%(item['skxq'],item['skjc'],int(item['skjc'])+int(item['cxjc'])-1)if item['skxq'] else "无",item['skjs'],item['kkxsjc'],item['bkskyl'],item['bkskrl']]
        df_n+=1
        if item['kkxqm']=='北校区':
            df_nor.loc[df_nor_n] = [item['kcm'], item['kch'], item['kxh'], item['kkxqm'],'星期%s第%s-%s节'%(item['skxq'],item['skjc'],int(item['skjc'])+int(item['cxjc'])-1)if item['skxq'] else "无", item['skjs'],item['kkxsjc'], item['bkskyl'],item['bkskrl']]
            df_nor_n += 1
        else:
            df_sou.loc[df_sou_n] = [item['kcm'], item['kch'], item['kxh'], item['kkxqm'],'星期%s第%s-%s节'%(item['skxq'],item['skjc'],int(item['skjc'])+int(item['cxjc'])-1)if item['skxq'] else "无",item['skjs'],item['kkxsjc'], item['bkskyl'],item['bkskrl']]
            df_sou_n += 1
    write = pd.ExcelWriter('./output.xlsx')
    df.to_excel(excel_writer=write, sheet_name='总计',index=False)
    df_nor.to_excel(excel_writer=write, sheet_name='北区',index=False)
    df_sou.to_excel(excel_writer=write, sheet_name='南区', index=False)
    write.save()
    write.close()
    print('finish')