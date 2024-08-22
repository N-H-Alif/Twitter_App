from flask import Flask, render_template, request, redirect, url_for, flash
import tweepy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Twitter API credentials
API_KEY = 'ucyOyPkIZ6bpLou9fPrAUVL1f'
API_SECRET_KEY = 'V5kZeVkrFOblnmx0gUzy9cw3Y7c4ahtGOyo8yIUSxLYz1HO8cg'
ACCESS_TOKEN = '134377901-4hDkW68Tf0vG95MDSbl35HJYKbkZKZX2OGGSX7iJ'
ACCESS_TOKEN_SECRET = 'aUsHVHDVRGx8E4wC210rh1G2OEjpw7GyHGfyzZUX7wa1w'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to extract tweet ID from URL
def extract_tweet_id(url):
    return url.split('/')[-1]

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tweet_url = request.form['tweet_url']
        tweet_id = extract_tweet_id(tweet_url)

        try:
            # Like the tweet
            api.create_favorite(tweet_id)
            # Retweet the tweet
            api.retweet(tweet_id)
            flash('Successfully liked and retweeted the tweet!', 'success')
        except tweepy.TweepError as e:
            flash(f'Error: {e}', 'danger')
        
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
