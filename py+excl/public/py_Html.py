# encoding: utf-8
"""
@author: lileilei
@file: py_Html.py
@time: 2017/6/5 17:04
"""
import  os
titles='接口测试'
def title(titles):
	title='''<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>%s</title>

        <link href="../bootstrap/bootstrap.css" rel="stylesheet">
        <link href="../bootstrap/bootstrap-table.css" rel="stylesheet">
        <script src="../bootstrap/jquery-3.0.0.js" type="text/javascript"></script>
        <script src="../bootstrap/bootstrap.js"></script>
        <script src="../bootstrap/bootstrap-table.js"></script>
        <script src="../bootstrap/bootstrap-table-zh-CN.js"></script>
        		<style type="text/css">
            table{
                table-layout: fixed;border='2'cellspacing='1' cellpadding='1'

            }
            th:nth-child(1),th:nth-child(2),th:nth-child(3),th:nth-child(6),th:nth-child(9){
                width: 75px;
            }
            td{
                word-wrap:break-word
            }

		</style>

	</head>
	<body>
	'''%(titles)
	return title
connent='''
<div class="container">
<div>
<h1>接口测试的结果</h1>'''
def time(starttime,endtime,passge,fail):
	beijing='''
		<p><strong>开始时间:</strong> %s</p>
		<p><strong>结束时间:</strong> %s</p>
		<p><strong>耗时:</strong> %s</p>
		<p><strong>结果:</strong>
			<span >Pass: <strong >%s</strong>
			Fail: <strong >%s</strong>
			Pass_rate:<strong >%.2f%%</strong>
			        </span></p>                  
			    <p ><strong>测试详情如下</strong></p>  </div> '''%(starttime,endtime,(endtime-starttime),passge,fail,100*passge/(passge+fail))
	return beijing
shanghai='''


        <p>&nbsp;</p>
    <div class="table-responsive">
        <table class="table table-hover table-bordered" >
		<tr >
            <td ><strong>用例ID&nbsp;</strong></td>
            <td><strong>用例名字</strong></td>
            <td><strong>key</strong></td>
            <td><strong>请求内容</strong></td>
            <td><strong>url</strong></td>
            <td><strong>请求方式</strong></td>
            <td><strong>预期</strong></td>
            <td><strong>实际返回</strong></td>  
            <td><strong>结果</strong></td>
        </tr>
    '''
def passfail(tend):
    if tend =='pass':
        htl=' <td bgcolor="green">pass</td>'
    elif tend =='fail':
        htl=' <td bgcolor="fail">fail</td>'
    else:
        htl='<td bgcolor="#8b0000">error</td>'
    return htl
def ceshixiangqing(id,name,key,coneent,url,meth,yuqi,json,relust):
    xiangqing='''
        <tr>
            <td>%s</td>
            <td>%s</td>
       
            <td>%s</td>
            <td><p class="p1">%s</p>
           </td>
            <td><p>%s</p></td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
               %s
        </tr>
        
    '''%(id,name,key,coneent,url,meth,yuqi,json,passfail(relust))
    return xiangqing
weibu='''
	</table>
	</div>
	</div>
    </body>
    </html>'''
def relust(titles,starttime,endtime,passge,fail,id,name,key,coneent,url,meth,yuqi,json,relust):
    if type(id) ==list:
        relus=' '
        for i in range(len(id)):
            relus+=(ceshixiangqing(id[i],name,key,coneent[i],url[i],meth[i],yuqi[i],json[i],relust[i]))
        text=title(titles)+connent+time(starttime,endtime,passge,fail)+shanghai+relus+weibu
    else:
        text=title(titles)+connent+time(starttime,endtime,passge,fail)+shanghai+ceshixiangqing(id,name,key,coneent,url,meth,yuqi,json,relust)+weibu
    return text
def createHtml(filepath,titles,starttime,endtime,passge,fail,id,name,key,coneent,url,meth,yuqi,json,relusts):
	texts=relust(titles,starttime,endtime,passge,fail,id,name,key,coneent,url,meth,yuqi,json,relusts)
	with open(filepath,'wb') as f:
		f.write(texts.encode())
