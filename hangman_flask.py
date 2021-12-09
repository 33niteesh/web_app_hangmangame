from flask import Flask,request
from flask.templating import render_template
import webbrowser as wb
import random
lis=['Aa Okkati Adakku','Pelli Neeku Sukham Naaku','Pellaniki Premalekha Priyuraliki Subhalekha','Pellante Noorella Panta','Pellam Chebithe Vinali','Pellam Chatu Mogudu','oka kshanam','kshanam','eega','lion','king','business men','krack','pelli choopulu']
str1=random.choice(lis)
li=[str(str1[f].lower()) for f in range(len(str1))]
l2=[]
for i in range(len(li)):
    if li[i]==" ":
        l2.append("   *   ")
    else:
        l2.append("_")
lif=[0,1,2,3,4,5]
hangman_flask = Flask(__name__)
@hangman_flask.route("/")
def game():
    return render_template('game.html')
@hangman_flask.route("/submit")
def submit():
    return render_template('submit.html')
@hangman_flask.route("/play")
def play():
        return render_template('play.html')
@hangman_flask.route("/press",methods=["POST"])
def press():
    if request.method=='POST':
        output=request.form["mn"]
    mn=output
    s=str(mn)
    if(s not in li):
        lif.remove(lif[-1])
        lifep=lif[-1]
        if(lif[-1]==0):
                return render_template('lose.html')
        else:
            return render_template('lowlife.html',lifep=lifep)
    if s in li:
        for i in range(len(l2)):
           if(li[i]==s):
               l2[i]=li[i]
    if(li==l2):
        return render_template('won.html')
        
    return render_template('press.html',pq=l2)
@hangman_flask.route("/moviename")
def moviename():
    moviename =li
    return render_template('moviename.html',movie=moviename)
if __name__ == '__main__':
    hangman_flask.run()