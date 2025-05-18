# DevOps Test Requirements

This README.md provides an explanation of the requirements for a simple DevOps test, including Dockerizing the application, deploying with Kubernetes, setting up Prometheus monitoring, and integrating with the ELK stack.

## 1. Dockerize the Application

### Dockerfile
Create a Dockerfile for the Python application. This file should include instructions to install all necessary dependencies, expose the correct port, and incorporate configurations managed by an appropriate .env file.

### Answer
The dockerfile is in the root directory and the image was built using the environment variables that was set in the .env file

### Build and Test Locally
Use Docker commands to build an image from the Dockerfile and run a container locally. Ensure the application functions correctly within the container.

### Answer
The Pod was run and tested and i exec into it for confirmation, you can find the screenshot in the screenshot directory

## 2. Deploy with Kubernetes

### Kubernetes Deployment YAML File
Write a YAML file to describe how Kubernetes should deploy the Docker container. Include specifications such as the container image, resource requirements, number of replicas, and other configurations.

### Answer
The file is named deployment.yaml is it can be found in the kube folder, the screenshot of the running pod can also be found in the screenshot director

### LoadBalancer Service
Configure a LoadBalancer service in Kubernetes to enable external access to the application.

### Answer
The file is named service.yaml, it can be found in the kube folder

### Horizontal Pod Autoscaler (HPA)
Include a configuration for Horizontal Pod Autoscaler (HPA) to automatically scale the application based on CPU usage.

### Answer
The file is named hpa.yaml, it can be found in the kube folder

## 3. Setup Prometheus Monitoring

### Prometheus Configuration
Configure Prometheus to monitor the application by specifying which metrics to scrape. This may include system metrics or custom application metrics.

### Deploy Prometheus within Kubernetes Cluster
Deploy Prometheus as a container within the Kubernetes cluster to enable scraping metrics from the application.

### Answer
The prometheus artifact can be found in the prometheus directory and the prometheus running pod screenshots can be found in the screenshot directory

### Visualize Metrics
Visualize the Prometheus metrics through a simple dashboard

### Answer
The metrics from prometheus was use to build a dashboard using grafana, the grafana artifact can be found in the grafana directory and the screenshot of the grafana runnning pod can be found in the screenshot artifact

## 4. Integrate with ELK Stack

### Filebeat Configuration
Configure Filebeat to watch the application's log files and ship them to Elasticsearch.

### Answer
The Filebeat artifact can be found in the elk directory and the filebeat running pod screenshots can be found in the screenshot directory

### Elasticsearch
Ensure Elasticsearch is running within the environment to store and index the logs sent from Filebeat.

### Answer
The Elasticsearch artifact can be found in the elk directory and the elasticsearch running pod screenshots can be found in the screenshot directory

### Kibana
Set up Kibana to visualize the logs stored in Elasticsearch. Create a dashboard in Kibana to display key information from the application's logs.

### Answer
The Kibana artifact can be found in the elk directory and the Kibana running pod screenshots can be found in the screenshot directory

By following these steps, you'll effectively Dockerize your application, deploy it using Kubernetes, set up monitoring with Prometheus, and integrate logging with the ELK stack, enabling efficient management, monitoring, and troubleshooting of your application in a DevOps environment.

## Evaluation Criteria

- Code quality, structure and organization
- Docker & Kubernetes best practices
- Application metrics, collect and visualize.
- Logs Managment, collect and visualize logs

## Submission

Please create a public GitHub repository and send the link to your repository once you have completed the project to <development@united-remote.com>.

