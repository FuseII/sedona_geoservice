from sedona.spark import *

config = (
    SedonaContext.builder()
    .config(
        "spark.jars.packages",
        "org.apache.sedona:sedona-spark-3.3_2.12:1.9.1,"
        "org.datasyslab:geotools-wrapper:1.9.1-33.5",
    )
    .config(
        "spark.jars.repositories",
        "https://artifacts.unidata.ucar.edu/repository/unidata-all",
    )
    .getOrCreate()
)
sedona = SedonaContext.create(config)

wkt = "POINT(1 1)"
sedona.sql(
 f"SELECT ST_GeomFromWKT('{wkt}') AS geom"
).show()