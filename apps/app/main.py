from controllers.routes import app
from mangum import Mangum

handler = Mangum(app)
