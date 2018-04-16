from django.db import models
from django.db import connection


class ProjectionManager(models.Manager):

    def by_date(self):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT
                distinct_dates.projection,
                distinct_dates.date,
                max_ab.ab
            FROM (
                SELECT DISTINCT
                    p.projection,
                    date_trunc('day', p.datetime) as date
                FROM ichiro_projection p
                GROUP BY 1
                ORDER BY 1, 2 ASC
            ) as distinct_dates
            INNER JOIN (
                SELECT
                    p.projection,
                    date_trunc('day', p.datetime) as date,
                    MAX(p.ab) as ab
                FROM ichiro_projection p
                GROUP BY 1, 2
                ORDER BY 1, 2 ASC
            ) as max_ab
            ON distinct_dates.projection = max_ab.projection
            AND distinct_dates.date = max_ab.date
            """)
            return self._dictfetchall(cursor)

    def _dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
