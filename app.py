import plotly.express as px
import sys
import plotly
import json
sys.path.append('../')
from torpedo import startingPoint as sp
from radar import dataCleaner as dc

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    dataset = dc.forecastCleaner()
    fig = px.scatter(dataset, x='Temperature', y='Time', height=400)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('homepage.html', graphJSON=graphJSON)
    


@app.route('/home')
def home():
    environment = jinja2.Environment()
    template = environment.from_string("Hello {{ }}")
    ## FLASK & PLOTLY & VIRTUAL ENV
    # 

    ## ACTIVATE VENV -> ./.venv/Scripts/activate
    ## DEACTIVATE VENV -> deactivate

    ## run flask -> flask --app nameOfFile(app) run
    #return (f'<p>{dc.dataCleaner()}</p>')