from django.db import models
from django.db import connection


class ProjectionManager(models.Manager):

    def by_date(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    p.projection,
                    MAX(date_trunc('day', p.datetime)),
                    MAX(p.ab) as ab
                FROM ichiro_projection p
                GROUP BY 1
                ORDER BY 1, 2 ASC""")
            return self._dictfetchall(cursor)

    def _dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
