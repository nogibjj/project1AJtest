from databricks import sql
import os


def querydb(query):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

def release_year(N):
    query = "select release_year from netflix_titles where title = N"
    return querydb(query)


def duration(N):
    query = "select duration from netflix_titles where title = N"
    return querydb(query)
