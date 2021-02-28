from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField

class UploadForm(FlaskForm):
    img = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'img', 'Please Upload a valid image type (jpg/png)'])])
