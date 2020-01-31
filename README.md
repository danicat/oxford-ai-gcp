# oxford-ai-gcp

This is the supporting material for my talk "Data Engineering on GCP" presented at Oxford University as part of the course [Artificial Inteligence: Cloud and Edge Implementations](https://www.conted.ox.ac.uk/courses/artificial-intelligence-cloud-and-edge-implementations).

## Presentation Slides

Available [here](https://docs.google.com/presentation/d/e/2PACX-1vRitdzbQmzKWs0wyneOqN9jfdOwDpWGaVwZJLKAPyKEGmIao3_P0KSwr7uRz6FMvSbuAKnkJoHxzvIa/pub?start=false&loop=false&delayms=3000).

## Getting Started

This repo has been tested on Linux Ubuntu and Mac OS X.

If you are using Windows 10 you may use Ubuntu through the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

The following steps assume you have [python3](https://www.python.org/downloads/) installed.

## Setup

Install Java 8 (required for PySpark):

```sh
sudo apt install openjdk-8-jdk
```

Create a python3 virtual env before running any of the sample code:

```sh
python3 -m venv venv
```

If the module `python3-venv` is not available, you may need to install it.

On Ubuntu:

```sh
sudo apt-get install python3-venv
```

To active the environment, use:

```sh
source venv/bin/activate
```

With the virtual env activated, install the requirements file:

```sh
pip install -r requirements.txt
```

To deactivate the environment, after finishing your work, use the command `deactivate`.

## References

1. [Why performance matters](https://developers.google.com/web/fundamentals/performance/why-performance-matters)
1. [Spark BigQuery connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector)
