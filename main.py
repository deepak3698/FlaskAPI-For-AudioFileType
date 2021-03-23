from flask import Flask, request, jsonify
import json
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
# Reading Data from Json
with open('config.json', 'r') as data:
    params = json.load(data)["params"]

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Song Class/Model
class Song(db.Model):
    ID = db.Column(db.Integer,primary_key=True)    # ID	Name	Duration	Uploaded_time
    Name = db.Column(db.String(100), nullable=False)
    Duration = db.Column(db.Integer, nullable=False)
    UploadedTime = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, ID, Name, Duration, UploadedTime):
        self.ID = ID
        self.Name = Name
        self.Duration = Duration
        self.UploadedTime = UploadedTime

# Podcast Class/Model
class Podcast(db.Model):
    ID = db.Column(db.Integer,primary_key=True)     # ID	Name	Duration	Uploaded_time	Host	Participants	
    Name = db.Column(db.String(100), nullable=False)
    Duration = db.Column(db.Integer, nullable=False)
    Uploaded_time = db.Column(db.DateTime, nullable=False)
    Host = db.Column(db.String(100), nullable=False)
    Participants = db.Column(db.String(500), nullable=True)
    
    def __init__(self, ID, Name, Duration, Uploaded_time,Host,Participants):
        self.ID = ID
        self.Name = Name
        self.Duration = Duration
        self.Uploaded_time = Uploaded_time
        self.Host = Host
        self.Participants = Participants

# Audiobook Class/Model
class Audiobook(db.Model):
    ID = db.Column(db.Integer, primary_key=True)  # ID	Title	Author	Narrator	Duration	Uploaded_time		
    Title = db.Column(db.String(100), nullable=False)
    Author = db.Column(db.String(100), nullable=False)
    Narrator = db.Column(db.String(100), nullable=False)
    Duration = db.Column(db.Integer, nullable=False)
    Uploaded_time = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, ID, Title, Author, Narrator,Duration,Uploaded_time):
        self.ID = ID
        self.Title = Title
        self.Author = Author
        self.Narrator = Narrator
        self.Duration = Duration
        self.Uploaded_time = Uploaded_time

# Song Schema
class SongSchema(ma.Schema):
  class Meta:    # ID	Name	Duration	Uploaded_time
    fields = ('ID', 'Name', 'Duration', 'Uploaded_time')
# Podcast Schema
class PodcastSchema(ma.Schema):
  class Meta:   # ID	Name	Duration	Uploaded_time	Host	Participants	
    fields = ('ID', 'Name', 'Duration', 'Uploaded_time','Host', 'Participants')
# Audiobook Schema
class AudiobookSchema(ma.Schema):
  class Meta:     # ID	Title	Author	Narrator	Duration	Uploaded_time		
    fields = ('ID', 'Title', 'Author', 'Narrator','Duration','Uploaded_time')

# Init schema for Song
song_schema = SongSchema()
songs_schema = SongSchema(many=True)
# Init schema for Podcast
podcast_schema = PodcastSchema()
podcasts_schema = PodcastSchema(many=True)
# Init schema for Audiobook
audiobook_schema = AudiobookSchema()
audiobooks_schema = AudiobookSchema(many=True)

# Create a audioFileType
@app.route('/AddAudioFile', methods=['POST'])
def addAudioFile():
    try:
        audioFileType = request.json['audioFileType']
        audioFileMetadata = request.json['audioFileMetadata']
        if audioFileType=="song":   # ID	Name	Duration	Uploaded_time
            newSong=Song(audioFileMetadata["ID"],audioFileMetadata["Name"],audioFileMetadata["Duration"],audioFileMetadata["Uploaded_time"])
            db.session.add(newSong)
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200
        elif audioFileType=="podcast":  # ID	Name	Duration	Uploaded_time	Host	Participants	
            newPodcast=Podcast(audioFileMetadata["ID"],audioFileMetadata["Name"],audioFileMetadata["Duration"],
            audioFileMetadata["Uploaded_time"],audioFileMetadata["Host"],audioFileMetadata["Participants"])
            print(audioFileMetadata["Uploaded_time"])
            db.session.add(newPodcast)
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200
        elif audioFileType=="audiobook": # ID	Title	Author	Narrator	Duration	Uploaded_time	
            newAudiobook=Audiobook(audioFileMetadata["ID"],audioFileMetadata["Title"],audioFileMetadata["Author"],
            audioFileMetadata["Narrator"],audioFileMetadata["Duration"],audioFileMetadata["Uploaded_time"])
            db.session.add(newAudiobook)
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200
        else:
            return jsonify({"The request is invalid":" 400 bad request"}),400
    except:
        return jsonify({"Any error": "500 internal server error"}),500
        

@app.route('/<string:audioFileType>/<int:audioFileID>', methods=['DELETE'])
def deleteAudioFile(audioFileType,audioFileID):
    try:
        if audioFileType=="song":
            song = Song.query.get(audioFileID)
            db.session.delete(song)
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200
        elif audioFileType=="podcast": 
            podcast = Podcast.query.get(audioFileID)
            db.session.delete(podcast)
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200
        elif audioFileType=="audiobook": 	
            audiobook = Audiobook.query.get(audioFileID)
            db.session.delete(audiobook)
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200

        else:
            return jsonify({"The request is invalid":" 400 bad request"}),400
    except:
        return jsonify({"Any error": "500 internal server error"}),500 

@app.route('/<string:audioFileType>', methods=['GET'])
@app.route('/<string:audioFileType>/<int:audioFileID>', methods=['GET'])
def getAudioFile(audioFileType,audioFileID=0):
    try:
        if audioFileType=="song":   
            if audioFileID==0:
                all_songs = Song.query.all()
                result = songs_schema.dump(all_songs)
                return jsonify(result)
            else:
                song=Song.query.get(audioFileID)
                return song_schema.jsonify(song)

        elif audioFileType=="podcast": 	
            if audioFileID==0:
                all_podcast = Podcast.query.all()
                result = podcasts_schema.dump(all_podcast)
                return jsonify(result)
            else:
                podcast=Podcast.query.get(audioFileID)
                return song_schema.jsonify(podcast)
        elif audioFileType=="audiobook": 
            if audioFileID==0:
                all_audiobook = Audiobook.query.all()
                result = songs_schema.dump(all_audiobook)
                return jsonify(result)
            else:
                audiobook=Audiobook.query.get(audioFileID)
                return song_schema.jsonify(audiobook)
        else:
            return jsonify({"The request is invalid":" 400 bad request"}),400
    except:
        return jsonify({"Any error": "500 internal server error"}),500


@app.route('/<string:audioFileType>/<int:audioFileID>', methods=['PUT'])
def updateAudio(audioFileType,audioFileID):
    try:
        audioFileMetadata = request.json['audioFileMetadata']
        if audioFileType=="song":
            song = Song.query.get(audioFileID)
            song.ID=audioFileMetadata["ID"]
            song.Name=audioFileMetadata["Name"]
            song.Duration=audioFileMetadata["Duration"]
            song.Uploaded_time=audioFileMetadata["Uploaded_time"]
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200
        elif audioFileType=="podcast": 
            podcast=Podcast.query.get(audioFileID)
            podcast.Name=audioFileMetadata["Name"]
            podcast.Duration=audioFileMetadata["Duration"]
            podcast.Uploaded_time=audioFileMetadata["Uploaded_time"]
            podcast.Host=audioFileMetadata["Host"]
            podcast.Participants=audioFileMetadata["Participants"]
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200

        elif audioFileType=="audiobook": 
            audiobook=Audiobook.query.get(audioFileID)
            audiobook.ID=audioFileMetadata["ID"]
            audiobook.Title=audioFileMetadata["Title"]
            audiobook.Author=audioFileMetadata["Author"]
            audiobook.Narrator=audioFileMetadata["Narrator"]
            audiobook.Duration=audioFileMetadata["Duration"]
            audiobook.Uploaded_time=audioFileMetadata["Uploaded_time"]
            db.session.commit()
            return jsonify({"Action is successful": "200 OK"}),200
        else:
            return jsonify({"The request is invalid":" 400 bad request"}),400
    except:
        return jsonify({"Any error": "500 internal server error"}),500 



# Run Server
if __name__ == '__main__':
    app.run(debug=True)