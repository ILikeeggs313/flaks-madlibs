from flask import request, render_template, Flask
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickensarecool'

app.debug = True
debug = DebugToolbarExtension(app)

@app.route('/list')
def list_stories():
    """show list of available stories"""
    return render_template('story-list.html',
    stories = stories.values())

@app.route('/home')
def question_series():
    """Generate form to ask questions about the story itself."""
    story_id = request.args['story_id']
    story = stories[story_id]

    prompts = story.prompts

    return render_template('question.html',prompts = prompts,
    story_id = story_id, title = story.title)

@app.route('/story')
def show_story():
    """show the story."""
    story_id = request.args['story_id']
    story = stories[story_id]

    text = story.generate(request.args)
    return render_template('story.html', text = text, title = story.title)



