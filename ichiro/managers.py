from django.db import models
from django.db import connection


class ProjectionManager(models.Manager):

    def by_date(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    p.datetime,
                    p.projection,
                    MAX(p.ab) as ab
                FROM ichiro_projection p
                GROUP BY p.datetime, p.projection
                ORDER BY p.datetime, p.projection ASC""")
            return self._dictfetchall(cursor)

    def _dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
