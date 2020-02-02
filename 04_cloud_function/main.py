from flask import jsonify
import sqlalchemy


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

    if request_json and 'user_id' in request_json:
        recs = []
        with db.connect() as conn:
            user_id = request_json['user_id']

            stmt = sqlalchemy.text(
                "SELECT doc_id FROM RECOMMENDATIONS WHERE user_id=:user_id AND prediction > 0.8 ORDER BY prediction DESC"
            )

            rows = conn.execute(stmt, user_id=user_id).fetchall()
            for row in rows:
                recs.append(row[0])

        result = {"items": recs}

        return jsonify(result)
