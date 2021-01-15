from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from django.core.mail import EmailMessage
from datetime import datetime
from datetime import timedelta
# Create your views here.
def rf(c,r):
	d={}
	for i,j in enumerate(c.description):
		d[j[0]]=r[i]
	return d
def getuser(request):
    usr=None
    if request.session.has_key('usr'):
        usr=request.session['usr']
    return usr
# class bike:
#     def __init__(s,Id,Name,rate):
#         self.id=id#         self.Name=Name
#         self.rate=rate

def index(request):
    # if not getuser(request):
    #     return HttpResponse('/login/',request)
    temp1=loader.get_template('index.html')
    
    return HttpResponse(temp1.render({},request))
def about(request):
    temp1=loader.get_template('about.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))
def bike(request): #,bike=None):
    c=connection.cursor()
    # if request.method=='POST':
    temp1=loader.get_template('bike.html')
    c.execute(f"select * from bikelist")
    dl=c.fetchall()   
    c.execute(f"select * from booking")
    bl=c.fetchall() 
    myDate =datetime.today() + timedelta(days=1)
    d=myDate.strftime("%m/%d/%Y")
    print(d)
    print('bike list',dl)
    return HttpResponse(temp1.render({'dl':dl,'loggeduser':getuser(request)},request))
def booking(request,regno):
    temp1=loader.get_template('booking.html')
    c=connection.cursor()
    c.cursor.row_factory=rf
    stat=""
    if request.method=='POST':
        b=request.POST['bike']
        pd=request.POST['pdate']
        dd=request.POST['ddate']
        n=request.POST['name']
        em=request.POST['email']
        pno=request.POST['phone']
        uid=request.POST['uid']
        # pd=datetime.strptime(pd,"%m-%d")
        print(pd)
        c.execute("select * from booking")
        bok=c.fetchall()


        if 'reg' in request.POST:

            c.execute(f"select  * from booking where '{pd}' between pdate and ddate")
            s1=c.fetchall()
            print(s1)
            c.execute(f"select  * from booking where '{dd}' between pdate and ddate")
            s2=c.fetchall()
            print(s2)
            s3=len(bok)

            for i in range(s3):

                print(bok[i]['bike'])

                if bok[i]['bike']==b:
                    if s1==[] and s2==[]:
                        r=None
                        try: 
                            c.execute(f"insert into booking('uid','bike','pdate','ddate','bname','bemail','bpno') values ('{uid}','{b}','{pd}','{dd}','{n}','{em}','{pno}')")
                            r=c.lastrowid
                            c.close()
                        except Exception  as ex:
                            print('booking iunsert error :',str(ex))
                            stat="error in booking.!"
                        print(r,'ewrer')
                        if r: 
                            try:
                                        
                                msgbody=f'Hello {n},\n\nWelcome to Bike rental\
                                     \nbooking comforming.' 
                                email = EmailMessage('bike rental', msgbody, to=(em,))
                                email.send()
                                return HttpResponseRedirect("/",request)
                            except Exception as e:
                                print('booking mail error:',str(e))
                                stat="booking taken..but..Unable to send mail to your id"
                        else:
                            stat="Unable to book this bike..!.."
                    else:
                        stat="cant book"
                else:
                    stat="bike not available"

            
            

    return HttpResponse(temp1.render({'msg':stat,'regn':regno,'loggeduser':getuser(request)},request))

def contact(request):
    temp1=loader.get_template('contact.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))
def service(request):
    temp1=loader.get_template('service.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))
def team(request):
    temp1=loader.get_template('team.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))
def blog_home(request):
    temp1=loader.get_template('blog_home.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))
def blog_single(request):
    temp1=loader.get_template('blog_single.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))
def elements(request):
    temp1=loader.get_template('elements.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))
def newuser(request):
    status=''
    temp1=loader.get_template('newuser.html')
    c=connection.cursor()
    if request.method=='POST':
        maill=request.POST['email']
        pas=request.POST['psw']
        name=request.POST['nam']
        if 'reg' in request.POST:
            c.execute(f"insert into logind('name','mail','pass')values('{name}','{maill}','{pas}')")
            r=c.fetchall()
    return HttpResponse(temp1.render({},request))

def admins(request):
    stat=""
    err=""
    temp1=loader.get_template('admins.html')
    c=connection.cursor()
    upload_file_url=''
    if request.method=='POST' and "myfile" in request.FILES:
        myfile=request.FILES['myfile']
        print(myfile,request.FILES)
        fs=FileSystemStorage()
        fname='mysite/static/img/'+myfile.name
        if fs.exists(fname):
            fs.delete(fname)
        filename=fs.save(fname,myfile)
        upload_file_url="/static/img/"+myfile.name

        regno=request.POST['regno']
        engno=request.POST['engno']
        rent=request.POST['rent']
        model=request.POST['model']
        desc=request.POST['desc']
        colour=request.POST['colour']

        if 'reg' in request.POST:
            c.execute(f'select * from bikelist where regno="{regno}" or engno="{engno}" LIMIT 1')
            err=c.fetchone()
            if err:
                stat="Invalid entry..this bike already is in store..!"
            else:
                c.execute(f"insert into bikelist('regno','engno','rent','model','desc','colour','image')values('{regno}','{engno}','{rent}','{model}','{desc}','{colour}','{upload_file_url}')")
                r=c.fetchall()
                c.close()
                if r:
                    return HttpResponseRedirect("/",request)
                else:
                    status='invalid'

        print(filename,'url',upload_file_url)

    return HttpResponse(temp1.render({'msg':stat,'url':upload_file_url},request))

def loggin(request):
    status=''
    temp1=loader.get_template('loggin.html')
    c=connection.cursor()
    if request.method=='POST':
        q=request.POST['b1']
        user=request.POST['name']
        p=request.POST['password']
        if q=='user':
            try:
                if 'log' in request.POST:
                    c.execute(f"select * from logind where mail='{user}' and pass='{p}' limit 1")
                    r=c.fetchone()
                    print(r)
                    w=r[1]
                    print(w)
                    e=r[0]
                    c.close()
                    if r:
                        request.session['usr']={'user':user,'name':w,'id':e}
                        return HttpResponseRedirect("/bike/",request)
                    else:
                        status='invalid'
            except Exception as e:
                status="no such username or password"
        else:
            if 'log' in request.POST:
                c.execute(f"select * from admins where mail='{user}' and pass='{p}' limit 1")
                r=c.fetchone()

                c.close()
                if r:
                    request.session['usr']=user
                    return HttpResponseRedirect("/admins/",request)
                else:
                    status='invalid'


    return HttpResponse(temp1.render({'msg':status},request))
def logout(request):
    if request.session.has_key('usr'):
        del request.session['usr']
    return HttpResponseRedirect("/",request)
def paymen(request):
    temp1=loader.get_template('payment.html')
    return HttpResponse(temp1.render({'loggeduser':getuser(request)},request))