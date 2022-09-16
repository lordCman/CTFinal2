from flask import request
from werkzeug.security import check_password_hash
from app import app
from app.models import User, db, Post, BetSlip
from app.apiauthhelper import token_required

@app.route('/signup', methods=["POST"])
def apiSignMeUp():
    data = request.json
     
    username = data['username']
    email = data['email']
    password = data['password']

    # add user to database
    user = User(username, email, password)

    # add instance to our db
    db.session.add(user)
    db.session.commit()
    return {
        'status': 'ok',
        'message': f"Successfully created user {username}"
    }


@app.route('/login', methods=['POST'])
def apiLogMeIn():
    data = request.json

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username = username).first()
    if user:
        if check_password_hash(user.password, password):
            return {
                'status': 'ok',
                'message': 'You have successfully logged in',
                'data': user.to_dict(),
            }
        return {
            'status': 'not ok',
            'message': 'incorrect password'
        }
    return {
        'status': 'not ok',
        'message': 'invalid username'
    }


@app.route('/createBet', methods=['POST'])
@token_required
def makeSlip(user):
    data = request.json
    
    teamWon = data['teamToWin'],
    odds = data['odds']

    bet = BetSlip(teamWon, odds, user.id)
    bet.save()

    return {
        'status': 'ok',
        'message': "bet was made"
    }




@app.route('/posts/create', methods=["POST"])
@token_required
def createPostAPI(user):
    data = request.json # this is coming from POST request Body

    caption = data['caption']

    post = Post(caption, user.id)
    post.save()

    return {
        'status': 'ok',
        'message': "Post was successfully created."
    }

@app.route('/posts')
def getPost():
    posts = Post.query.all()
    my_posts= [p.to_dict() for p in posts]
    return {'status': 'ok', 'message': 'here are the posts', 'posts': my_posts}

# @app.route('getMyBets')
# def myBets():
    