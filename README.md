# Internet of Things Data Analytics Pipeline

[![Build](https://github.com/philem208/IoT-analytics-pipeline/actions/workflows/docker.yml/badge.svg)](https://github.com/philem208/IoT-analytics-pipeline/actions/workflows/docker.yml)
[![Percentage of issues still open](http://isitmaintained.com/badge/open/philem208/IoT-analytics-pipeline.svg)](http://isitmaintained.com/project/philem208/IoT-analytics-pipeline "Percentage of issues still open")
[![GitHub forks](https://img.shields.io/github/forks/philem208/IoT-analytics-pipeline)](https://github.com/philem208/IoT-analytics-pipeline/network)
[![GitHub stars](https://img.shields.io/github/stars/philem208/IoT-analytics-pipeline)](https://github.com/philem208/IoT-analytics-pipeline/stargazers)
[![GitHub license](https://img.shields.io/github/license/philem208/IoT-analytics-pipeline)](https://github.com/philem208/IoT-analytics-pipeline)

## Introduction
The internet of things produces a massive flood of data due to the vast amount of underlying heterogeneous devices. The heterogeneity is a result of the multitude of vendors and diverse upcoming standards and protocols. From a cybersecurity perspective, this heterogeneity presents an enormous challenge. Analyses must cover all temporal dimensions to recognize incidents in real-time. These incidents are based on so-called indicators of compromise, and by identifying and reacting to them, potential damage can be minimized or completely ward off.  Thus, from the underlying data, information must be created, which can lead to knowledge and wisdom. By processing stream and batch data, descriptive, diagnostic, detective, predictive and prescriptive analytics can be engaged.   

## Pipeline
The pipeline shows a visualization of the Docker Compose file. The Viz repository [pmsipilot/docker-compose-viz](https://github.com/pmsipilot/docker-compose-viz).
```docker
docker run --rm -it --name dc -v ${pwd}:/input pmsipilot/docker-compose-viz render -m image docker-compose.yml -f
```
![alt text](https://github.com/philem208/IoT-analytics-pipeline/blob/master/resources/docker-compose.png) was used for this with the following command:

## Tech stack
| Technology      | Version | Description | Task     |
| -       |    :-:   |      -  |       ---- |
| [Apache Kafka](https://kafka.apache.org/)      | latest  | Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.       |  Message broker cluster to structure the amount of heterogeneous data by topics and distribute it to various consumers, including Logstash.   |
| [Apache Zookeeper](https://zookeeper.apache.org/) |   latest    | ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them, which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.  |   Apache Zookeeper takes care of the administration of the distributed systems in the pipeline. In particular, this acts as a coordinator for Apache Kafka.    |
| [Docker](https://www.docker.com/) |       latest  |   Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.    |Serves the underlying infrastructure to link the individual technologies in a modular way to make their use platform-independent and straightforward. This makes the deployment of the "Analytics Pipeline" a breeze.
| [Elasticsearch](https://www.elastic.co/elasticsearch/)    | 7.10.1    | Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data for lightning fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.  |    Elasticsearch represents the data store to index all the data based on a particular topic. Moreover, the use of Elasticsearch in IoT is appropriate to make the data search more efficient.   |
| [EMQ X](https://www.emqx.io/) |        latest  |   Scalable and Reliable Real-time MQTT Message Broker for IoT in the 5G Era. EMQ X connects any IoT device via all major IoT communication protocols, including MQTT v5.0, CoAP/LwM2M 1.1 and even LoraWAN, over 3G/4G/5G&NB-IoT networks, and ensures security via TLS/DTLS, X.509 certificate, and diverse authentication mechanism.    |EMQ X is the messaging broker and the gateway into the analytics pipeline. EMQ X acts as a broker and connects all IoT devices and edge nodes using the MQTT protocol and specific topics.|
| [Kafdrop](https://github.com/obsidiandynamics/kafdrop) |        latest  |      Kafdrop is a web UI for viewing Kafka topics and browsing consumer groups. The tool displays information such as brokers, topics, partitions, consumers, and lets you view messages. | Kafrop simplifies the administration of a Kafka cluster by visualizing the Topics, Consumers, Producers and Brokers. 
| [Kibana](https://www.elastic.co/kibana) |        7.10.1  |  Kibana is a free and open user interface that lets you visualize your Elasticsearch data and navigate the Elastic Stack. Do anything from tracking query load to understanding the way requests flow through your apps.     |Kibana is used for pure visualization of incoming data streams and batch data. Besides, users could also use machine learning algorithms to gain essential insights from the data. |
| [Logstash](https://www.elastic.co/logstash) |        7.10.1 |   Logstash is a free and open server-side data processing pipeline that ingests data from a multitude of sources, transforms it, and then sends it to your favorite stash.    | Logstash collects the messages from the individual Kafka topics and, using various filters, can preprocess the data before it is stored in Elasticsearch. |
| [MQTT-Kafka-Bridge](https://github.com/nodefluent/mqtt-to-kafka-bridge) |       latest  |  mqtt-to-kafka-bridge allows you to quickly setup a fast (about messages 2 million/sec) and lightweight (about 100 MB RAM) bridge that subscribes to your MQTT Broker and produces messages to your Apache Kafka cluster. You can configure routing (move messags from MQTT topics to certain Kafka topics) or filtering, as well as ETL functions on MQTT consume, as well as on Kafka produce. You just pass everything in a simple JSON/JS config object.     | This bridge is used to efficiently transfer the topics of the MQTT broker to the topics of the Kafka broker and synchronize their contents. |


## Deploy

### Build the infrastructure
The simple variant of deployment without changing the configuration files: 
```docker
docker-compose up
```
If the Logstash pipeline files or the installation commands of individual plugins for Logstash have changed, it is recommended to initiate a rebuild of the infrastructure:
```docker
docker-compose up --build --force-recreate
```
### Run the MQTT message producer
#### Dependencies
TODO
#### Command
```python
py /python-mqtt-client/client.py
```

### Call the UIs
```html
http://localhost:5601 (Kibana)
http://localhost:9000 (Kafdrop)
```

Happy analyzing!
## Authors
* **Philip Empl** - [Department of Information Systems](https://www.uni-regensburg.de/wirtschaftswissenschaften/wi-pernul/team/philip-empl/index.html)  *@ University of Regensburg*

## License
This project is available under the MIT license. 