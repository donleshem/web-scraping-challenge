from flask import Flask, render_template
from flask_pymongo import PyMongo
from scrape_mars import scrape_nasa
import pymongo
import scrape_mars

###############p##################################
# Flask Setup
#################################################
app = Flask(__name__)

conn = 'mongodb://localhost:27017/marsdb'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def index():
    mars = client.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars.drop()
    mars_data = scrape_mars.scrape_nasa()
    print (mars_data)
    mars.insert(mars_data)
    return "scrape done!"
    

if __name__ == '__main__':
    app.run(debug=True)
