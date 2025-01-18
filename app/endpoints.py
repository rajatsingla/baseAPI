import app.libs.debug as debughelpers

def setup_routes(factory):
    factory.get("echo/{word}")(debughelpers.echo)