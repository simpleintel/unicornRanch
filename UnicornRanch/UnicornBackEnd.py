from flask import Flask
import request
app = Flask(__name__)

#Ranch Coordinates
unicornLocation = {}

class UnicornRanch:

    @app.route('/processunicorn')
    def getUnicorncoordinates():
        # Error check for valid id
        returnCoordinate = ''
        for id in unicornLocation:
            print(id)
            returnCoordinate = returnCoordinate + unicornLocation[id] + "\t"
        return returnCoordinate

    @app.route('/updatecoordiantes/<id>/<coordinates>')
    def UpdateUnicornCoordinated(id, coordinates):
        #update The datebase
        unicornLocation[id] = coordinates
        return unicornLocation[id]

