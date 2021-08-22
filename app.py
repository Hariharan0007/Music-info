from flask import Flask,render_template,request,jsonify
import requests,json


app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    return render_template('hometemp.html')

@app.route('/searchname',methods=["GET","POST"])
def searchname():
    srurl="https://www.theaudiodb.com/api/v1/json/1/search.php?s="
    fullurl=request.form.get('Name')
    print(fullurl)
    #fullurl="coldplay"
    dburl=srurl + fullurl
    db=requests.get(dburl)
    nm=db.json()
    for i in nm:
        key=i
        break
    arname=nm[key]
    srurl1="https://theaudiodb.com/api/v1/json/1/discography.php?s="
    fullurl1=fullurl
    print(fullurl1)
    dburl1=srurl1 + fullurl1
    db1=requests.get(dburl1)
    nm1=db1.json()
    for i in nm1:
        key1=i
        break
    disname=nm1[key1]
    return render_template('searchname.html',name=arname,disco=disname)



    """
    #print(len(arname))
    print(arname)
    keyvalues=[]
    val=1
    for i in range(len(arname)):
        for k in arname[i]:
            print("{% if k.",k,"!=None %}<tr><th>",k,"</th><td>{{k.",k,"}}</td></tr>{% endif %}")
            #keyvalues.append(k)
        #break
    print(len(keyvalues))
    """




@app.route('/artistdata',methods=["GET","POST"])
def artistdata():
    srurl="https://theaudiodb.com/api/v1/json/1/artist.php?i="
    fullurl=request.form.get('Name')
    print(fullurl)
    dburl=srurl + fullurl
    db=requests.get(dburl)
    nm=db.json()
    for i in nm:
        key=i
        break
    ardata=nm[key]
    """
    for i in range(len(ardata)):
        for k in ardata[i]:
            print("{% if k.",k,"!=None %}<tr><th>",k,"</th><td>{{k.",k,"}}</td></tr>{% endif %}")
    """
    for i in range(len(ardata)):
        for k in ardata[i]:
            print(k)
            if k=="strArtist":
                fullurl1=ardata[i][k]
                break
    srurl1="https://theaudiodb.com/api/v1/json/1/discography.php?s="
    dburl1=srurl1 + fullurl1
    db1=requests.get(dburl1)
    nm1=db1.json()
    for i in nm1:
        key1=i
        break
    disname=nm1[key1]
    return render_template('searchname.html',name=ardata,disco=disname)


@app.route('/albumarid',methods=["GET","POST"])
def albumarid():
    srurl="https://theaudiodb.com/api/v1/json/1/album.php?i="
    fullurl=request.form.get('Name')
    print(fullurl)
    dburl=srurl + fullurl
    db=requests.get(dburl)
    nm=db.json()
    for i in nm:
        key=i
        break
    aldata=nm[key]
    """
    for i in range(len(aldata)):
        for k in aldata[i]:
            print("{% if k.",k,"!=None %}<tr><th>",k,"</th><td>{{k.",k,"}}</td></tr>{% endif %}")
        break
    """
    """
    for i in range(len(aldata)):
        for k in aldata[i]:
            if k=="idAlbum":
                print("<button class=\"btn btn-primary btn-lg\"><input type=\"submit\" Name='Name' Name=\"",aldata[i][k],"\" value=\"",aldata[i][k],"\"></button>")
    """
    return render_template('albumaralid.html',data=aldata)

@app.route('/albumalid',methods=["GET","POST"])
def albumalid():
    srurl="https://theaudiodb.com/api/v1/json/1/album.php?m="
    fullurl=request.form.get('Name')
    print(fullurl)
    dburl=srurl + fullurl
    db=requests.get(dburl)
    nm=db.json()
    for i in nm:
        key=i
        break
    aldata=nm[key]
    """
    for i in range(len(aldata)):
        for k in aldata[i]:
            print("{% if k.",k,"!=None %}<tr><th>",k,"</th><td>{{k.",k,"}}</td></tr>{% endif %}")
    """
    return render_template('albumaralid.html',data=aldata)


@app.route('/trackalid',methods=["GET","POST"])
def trackalid():
    srurl="https://theaudiodb.com/api/v1/json/1/track.php?m="
    fullurl=request.form.get('Name')
    print(fullurl)
    dburl=srurl + fullurl
    db=requests.get(dburl)
    nm=db.json()
    for i in nm:
        key=i
        break
    trackdata=nm[key]
    """
    for i in range(len(trackdata)):
        for k in trackdata[i]:
            print("{% if k.",k,"!=None %}<tr><th>",k,"</th><td>{{k.",k,"}}</td></tr>{% endif %}")
        break
    """
    """
    for i in range(len(trackdata)):
        for k in trackdata[i]:
            if k=="idTrack":
                print("<button class=\"btn btn-primary btn-lg\"><input type=\"submit\" Name='Name' Name=\"",trackdata[i][k],"\" value=\"",trackdata[i][k],"\"></button>")
    """
    return render_template('trackalid.html',data=trackdata,alid=fullurl)
    #return "Hello"


@app.route('/tracktid',methods=["GET","POST"])
def tracktid():
    srurl="https://theaudiodb.com/api/v1/json/1/track.php?h="
    fullurl=request.form.get('Name')
    print(fullurl)
    dburl=srurl + fullurl
    db=requests.get(dburl)
    nm=db.json()
    for i in nm:
        key=i
        break
    trackdata=nm[key]
    """
    for i in range(len(trackdata)):
        for k in trackdata[i]:
            print("{% if k.",k,"!=None %}<tr><th>",k,"</th><td>{{k.",k,"}}</td></tr>{% endif %}")
        break
    """
    return render_template('tracktrid.html',data=trackdata,trid=fullurl)


@app.route('/musicalid',methods=["GET","POST"])
def musicalid():
    srurl="https://theaudiodb.com/api/v1/json/1/mvid.php?i="
    fullurl=request.form.get('Name')
    print(fullurl)
    dburl=srurl + fullurl
    db=requests.get(dburl)
    nm=db.json()
    for i in nm:
        key=i
        break
    mscdata=nm[key]
    for i in range(len(mscdata)):
        for k in mscdata[i]:
            if k=="strTrack":
                tname=mscdata[i][k]
            if k=="strMusicVid":
                print("<a href=\"",mscdata[i][k],"\"><button class=\"btn btn-secondary btn-lg\">",tname,"</button></a>")
    return render_template('music.html',data=mscdata)


if __name__=='__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)