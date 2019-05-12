# mnist-flask-cassandra
Overview:
        This project is based on tensorflow, Cassandra，python-Flask and docker. The model was built and trained through tensorflow. And deploy it to the web through the python-flask framework, so that others can invoke my service and save the user's usage information in the Cassandra database. In the end, all the code and the environment on which the code depends are deployed into docker for the convenience of others to use directly in different operating environments.
Details:
        if you want to invoke the service, you first need to install docker locally. (The specific installation method can be found on the official website）
        And then we start the container（docker start container_id)
        now you can use the "curl post" to upload images. and then you can look it up on the web. (http://127.0.0.1:5000/numbers)
        This information is also recorded synchronously in Cassandra.
        If you want to view the information in Cassandra, here are the steps.
        1. docker exec -it some-cassandra cqlsh
        2. USE mnist;
        3. select* from predictions;
Presentation. GIF is the presentation of video.
