from flask import escape
import sqlalchemy

def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))


def recommend(request):
    db = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username='rec-db',
            password='rec-db',
            database='rec-db',
            query={"unix_socket": "/cloudsql/danicat:us-west1:recsys-db"}
        ))

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'user_id' in request_json:
        recs = []
        with db.connect() as conn:
            user_id = request_json['user_id']

            stmt = sqlalchemy.text(
                "SELECT doc_id FROM RECOMMENDATIONS WHERE user_id=:user_id"
            )

            result = conn.execute(stmt, user_id=user_id).fetchall()
            for row in result:
                recs.append(row[0])

        return str(recs)
