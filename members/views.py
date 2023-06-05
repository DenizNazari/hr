from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members1(request):
    return HttpResponse("Hello world!")

def members(request):
    template = loader.get_template('grpage.html')
    import cx_Oracle
    import platform
    print(platform.architecture())
    #craet connection

    con = cx_Oracle.connect("BeITHR/1qa2ws3ed@//192.168.0.220/ORACLE")
    print(con.version)
    cur = con.cursor()
    cur.execute("SELECT * FROM HR_SHOBELER")
    a=[row[1] for row in cur ]
    con.commit()
    return render(request, "grpage.html",context = {'a': a})