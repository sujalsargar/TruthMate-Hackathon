from datetime import datetime
import uuid
from extensions import db

class Verification(db.Model):
    __tablename__ = 'verifications'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    
    content_type = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_preview = db.Column(db.String(500))
    
    accuracy_score = db.Column(db.Float)
    verdict = db.Column(db.String(20))
    ai_probability = db.Column(db.Float)
    
    sources = db.Column(db.JSON)
    description = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'content_type': self.content_type,
            'content_preview': self.content_preview,
            'accuracy_score': self.accuracy_score,
            'verdict': self.verdict,
            'ai_probability': self.ai_probability,
            'sources': self.sources,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }