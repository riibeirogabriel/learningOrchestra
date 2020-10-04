**Wondering how to combine your various library and infrastructure needs for your latest data mining project? Just pick the bricks to build your pipeline and learningOrchestra will take care of the rest.**

<p align="center">
    <img src="./learning-orchestra.png">
    <img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square" href="https://shields.io/" alt="build-passing">
    <img src="https://img.shields.io/github/v/tag/riibeirogabriel/learningOrchestra?style=flat-square" href="https://github.com/riibeirogabriel/learningOrchestra/tags" alt="tag">
    <img src="https://img.shields.io/github/last-commit/riibeirogabriel/learningOrchestra?style=flat-square" href="https://github.com/riibeirogabriel/learningOrchestra/tags" alt="last-commit">
    <img src="https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square" href="#contributors-" alt="All Contributors">
</p>

# learningOrchestra

## Introduction

### Context

Nowadays, **data science relies on a wide range of computer science skills**, from data management to algorithm design, from code optimization to cloud infrastructures. Data scientists are expected to have expertise in these diverse fields, especially when working in small teams or for academia.

This situation can constitute a barrier to the actual extraction of new knowledge from collected data, which is why the last two decades have seen more efforts to facilitate and streamline the development of data mining workflows. The tools created can be sorted into two categories: **high-level** tools facilitate the building of **automatic data processing pipelines** (e.g. :question:) while **low-level** ones support the setup of appropriate physical and virtual infrastructure (e.g. :question:).

However, this landscape is still missing a tool that **encompasses all steps and needs of a typical data science project**. This is where learningOrchestra comes in.

### The learningOrchestra system

learningOrchestra aims to facilitate the development of complex data mining workflows by **seamlessly interfacing different data science tools and services**. From a single interoperable Application Programming Interface (API), users can **design their analytical pipelines and deploy them in an environment with the appropriate capabilities**.

learningOrchestra is designed for data scientists from both engineering and academia backgrounds, so that they can **focus on the discovery of new knowledge** in their data rather than library or maintenance issues.

<!-- TOC depthFrom:2 depthTo:4 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Introduction](#introduction)
	- [Context](#context)
	- [The learningOrchestra system](#the-learningorchestra-system)
- [Quick-start](#quick-start)
- [How do I install learningOrchestra?](#how-do-i-install-learningorchestra)
	- [Setting up your cluster](#setting-up-your-cluster)
	- [Deploy learningOrchestra](#deploy-learningorchestra)
- [How do I use learningOrchestra?](#how-do-i-use-learningorchestra)
	- [Using the microservices REST API](#using-the-microservices-rest-api)
	- [Using the Python package](#using-the-python-package)
	- [Check cluster status](#check-cluster-status)
- [About learningOrchestra](#about-learningorchestra)
	- [Research background](#research-background)
	- [Future steps](#future-steps)
	- [Contributors](#contributors)
- [Frequently Asked Questions](#frequently-asked-questions)
	- [On using learningOrchestra](#on-using-learningorchestra)
	- [On the languages and frameworks used by learningOrchestra](#on-the-languages-and-frameworks-used-by-learningorchestra)
	- [On contributing to learningOrchestra](#on-contributing-to-learningorchestra)
- [Requirements](#requirements)
- [Deployment](#deployment)
- [Cluster State](#cluster-state)
- [Microservices REST APIs](#microservices-rest-apis)
	- [Spark Microservices](#spark-microservices)
- [Database GUI](#database-gui)
- [Contributors ✨](#contributors-)

<!-- /TOC -->

## Quick-start

Installation instructions:
1. learningOrchestra runs on Linux hosts. Install [Docker Engine](https://docs.docker.com/engine/install/) on all instances of your cluster. Configure your cluster in [swarm mode](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/). Install [Docker Compose](https://docs.docker.com/compose/install/) on your manager instance.
2. Clone repo on your manager instance. `https://github.com/learningOrchestra/learningOrchestra.git`
3. `cd learningOrchestra`
4. Deploy with `sudo ./run.sh`

learningOrchestra provides two options to access its features: a microservice REST API and a Python package.

Microservice REST API: We recommand using a GUI REST API caller like [Postman](https://www.postman.com/product/api-client/) or [Insomnia](https://insomnia.rest/). Check the [list of available microservices](https://learningorchestra.github.io/learningOrchestra-docs/usage/#microservices-rest-apis) for requests details.

Python package:
- Python3 package
- Install with `pip install learning-orchestra-client`
- Start your scripts by import the package and providing the IP address of one of the instances of your cluster:
```
from learning_orchestra_client import *
cluster_ip = "xx.xx.xxx.xxx"
Context(cluster_ip)
```
- Each microservice is wrapped into a class. Check the [package documentation](https://learningorchestra.github.io/learningOrchestra-docs/python-apis/) for a list of available functions and parameters.

## How do I install learningOrchestra?

### Setting up your cluster

### Deploy learningOrchestra

## How do I use learningOrchestra?

learningOrchestra provides two options to access its features: a microservice REST API and a Python package.

### Using the microservices REST API

### Using the Python package

### Check cluster status

## About learningOrchestra

### Research background

### Future steps

### Contributors

## Frequently Asked Questions

###### What is this website linked to the repo?

###### Who is doing this?

### On using learningOrchestra

###### I have a question/a feature request/some feedback, how do I contact you?
Please use the [**Issues** page]() of this repo. Check out the [Contributing](##Contributing) section for more details.

###### Can I copy your code for my project?

###### How do I cite learningOrchestra in my paper?

###### Where can I find data?

###### My computer runs on Windows/OSX, can I still use learningOrchestra?

###### I have a single computer, can I still use learningOrchestra?

### On the languages and frameworks used by learningOrchestra

###### Method X is very useful and should be included, why is it not there?

### On contributing to learningOrchestra

##### I'm not a developer, can I contribute?





**learningOrchestra** facilitates and streamlines iterative processes in a Data Science project pipeline like:

* Data Gathering
* Data Cleaning
* Model Building
* Validating the Model
* Presenting the Results

With learningOrchestra, you can:

* load a dataset from an URL (in CSV format).
* accomplish several pre-processing tasks with datasets.
* create highly customised model predictions against a specific dataset by providing their own pre-processing code.
* build prediction models with different classifiers simultaneously using a spark cluster transparently.

And so much more! Check the [usage section](#usage) for more.

# Installation

## Requirements

* Linux hosts
* [Docker Engine](https://docs.docker.com/engine/install/) must be installed in all instances of your cluster
* Cluster configured in swarm mode, check [creating a swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/)
* [Docker Compose](https://docs.docker.com/compose/install/) must be installed in the manager instance of your cluster

*Ensure that your cluster environment does not block any traffic such as firewall rules in your network or in your hosts.*

*If in case, you have firewalls or other traffic-blockers, add learningOrchestra as an exception.*

Ex: In Google Cloud Platform each of the VMs must allow both http and https traffic.

## Deployment

In the manager Docker swarm machine, clone the repo using:

```
git clone https://github.com/riibeirogabriel/learningOrchestra.git
```

Navigate into the `learningOrchestra` directory and run:

```
cd learningOrchestra
sudo ./run.sh
```

That's it! learningOrchestra has been deployed in your swarm cluster!

## Cluster State

`CLUSTER_IP:80` - To visualize cluster state (deployed microservices and cluster's machines).
`CLUSTER_IP:8080` - To visualize spark cluster state.

*\** `CLUSTER_IP` *is the external IP of a machine in your cluster.*

# Usage

learningOrchestra can be used with the [Microservices REST API](#microservices-rest-apis) or with the `learning-orchestra-client` [Python package](https://pypi.org/project/learning-orchestra-client/).

## Microservices REST APIs

[Database API](https://riibeirogabriel.github.io/learningOrchestra/database_api)- Download and handle datasets in a database.

[Projection API](https://riibeirogabriel.github.io/learningOrchestra/projection)- Make projections of stored datasets using Spark cluster.

[Data type API](https://riibeirogabriel.github.io/learningOrchestra/data_type_handler)- Change dataset fields type between number and text.

[Histogram API](https://riibeirogabriel.github.io/learningOrchestra/histogram)- Make histograms of stored datasets.

[t-SNE API](https://riibeirogabriel.github.io/learningOrchestra/t_sne)- Make a t-SNE image plot of stored datasets.

[PCA API](https://riibeirogabriel.github.io/learningOrchestra/pca)- Make a PCA image plot of stored datasets.

[Model builder API](https://riibeirogabriel.github.io/learningOrchestra/model_builder)- Create a prediction model from pre-processed datasets using Spark cluster.

### Spark Microservices

The Projection, t-SNE, PCA and Model builder microservices uses the Spark microservice to work.

By default, this microservice has only one instance. In case your data processing requires more computing power, you can scale this microservice.

To do this, with learningOrchestra already deployed, run the following in the manager machine of your Docker swarm cluster:

`docker service scale microservice_sparkworker=NUMBER_OF_INSTANCES`

*\** `NUMBER_OF_INSTANCES` *is the number of Spark microservice instances which you require. Choose it according to your cluster resources and your resource requirements.*

## Database GUI

NoSQLBooster- MongoDB GUI performs several database tasks such as file visualization, queries, projections and file extraction to CSV and JSON formats.
It can be util to accomplish some these tasks with your processed dataset or get your prediction results.

Read the [Database API docs](https://riibeirogabriel.github.io/learningOrchestra/database_api) for more info on configuring this tool.

See the [full docs](https://riibeirogabriel.github.io/learningOrchestra/usage/) for detailed usage instructions.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://www.linkedin.com/in/riibeirogabriel/"><img src="https://avatars0.githubusercontent.com/u/33736256?v=4" width="100px;" alt=""/><br /><sub><b>Gabriel Ribeiro</b></sub></a><br /><a href="https://github.com/learningOrchestra/learningOrchestra/commits?author=riibeirogabriel" title="Code">💻</a> <a href="#infra-riibeirogabriel" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#projectManagement-riibeirogabriel" title="Project Management">📆</a> <a href="#maintenance-riibeirogabriel" title="Maintenance">🚧</a></td>
    <td align="center"><a href="http://navendu.me"><img src="https://avatars1.githubusercontent.com/u/49474499?v=4" width="100px;" alt=""/><br /><sub><b>Navendu Pottekkat</b></sub></a><br /><a href="https://github.com/learningOrchestra/learningOrchestra/commits?author=navendu-pottekkat" title="Documentation">📖</a> <a href="#design-navendu-pottekkat" title="Design">🎨</a> <a href="#ideas-navendu-pottekkat" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/hiperbolt"><img src="https://avatars2.githubusercontent.com/u/14186706?v=4" width="100px;" alt=""/><br /><sub><b>hiperbolt</b></sub></a><br /><a href="https://github.com/learningOrchestra/learningOrchestra/commits?author=hiperbolt" title="Code">💻</a> <a href="#ideas-hiperbolt" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
