from main import db

class Card(db.Model):
    # NAME OF THE TABLE/MODEL
    __tablename__ = "cards"
    # CREATE THE COLUMNS/ATTRIBUTES
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    date = db.Column(db.Date())
    # deadline = db.Column(db.Date())
    status = db.Column(db.String())
    priority = db.Column(db.String())
    # DECLARE user_id FOREIGN KEY COLUMN
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    comments = db.relationship(
        "Comment",
        backref="card",
        cascade="all, delete"
    )
