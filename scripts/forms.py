from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import InputRequired


class MyForm(FlaskForm):
    user_input = StringField('What should I wear...', validators=[InputRequired()], render_kw={"class": "form-input"})
    item = StringField('Focal item:', render_kw={"class": "form-input"})
    json_file = FileField('Wardrobe data:', render_kw={"class": "form-input"})
