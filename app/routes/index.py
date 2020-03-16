from . import Routes

@Routes.route('/')
def index():
    return "Connected"
