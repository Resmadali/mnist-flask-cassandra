import logging

log = logging.getLogger()

log.setLevel('INFO')

handler = logging.StreamHandler()

handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))

log.addHandler(handler)

#from cassandra.cluster import Cluster

#from cassandra import ConsistencyLevel

from cassandra.cluster import Cluster

from cassandra.query import SimpleStatement

KEYSPACE = "mykeyspace"

def createKeySpace():

   cluster = Cluster(contact_points=['127.0.0.1'],port=9042)

   session = cluster.connect()

   log.info("Creating keyspace...")

   try:

       session.execute("""

           CREATE KEYSPACE %s

           WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }

           """ % KEYSPACE)

       log.info("setting keyspace...")

       session.set_keyspace(KEYSPACE)

       log.info("creating table...")

       session.execute("""

           CREATE TABLE mytable (

               id text,

               file_name text,

               time text,
               
               prediction text,

               PRIMARY KEY (id, file_name)

           )

           """)

   except Exception as e:

       log.error("Unable to create keyspace")

       log.error(e)
def insertData(session,id,file_name,time,prediction):
   cluster = Cluster(contact_points=['127.0.0.1'],port=9042)

   session = cluster.connect()

   session.execute(
   """

           INSERT INTO mytable(id, file_name, time, prediction)

           VALUES(%s,%s,%s,%s)
           """,
           )


createKeySpace();
