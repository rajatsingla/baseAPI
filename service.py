import hug
from app.cors import CORSMine

from apphelpers.rest.hug import APIFactory
from app.endpoints import setup_routes
from app.models import db
from converge import settings

def make_app():
    hug.not_found()(lambda: "Not Found")

    router = hug.route.API(__name__)

    api = hug.API(__name__)
    api.http.add_middleware(
        CORSMine(
            api, allow_origins=["*"], max_age=10000
        )
    )

    api_factory = APIFactory(router, urls_prefix=settings.URL_PREFIX)
       
    sessiondb_conn = dict(
        host=settings.SESSIONSDB_HOST,
        port=settings.SESSIONSDB_PORT,
        password=settings.SESSIONSDB_PASSWD,
        db=settings.SESSIONSDB_NO,
    )
    api_factory.setup_session_db(sessiondb_conn)
    api_factory.setup_db_transaction(db)
    setup_routes(api_factory)
    # either use peewee or db.evolve
    # peewee.setup_db_from_basemodel(db, CommonModel)
    db.evolve(interactive=False)


make_app()
