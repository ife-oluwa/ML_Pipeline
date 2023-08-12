<!-- @format -->

### A Full Stack MLOPs Project

This repository demonstrates the design, implementation, training, deployment and monitoring of an ML batch system using MLOps best practices.
In this project, I built a production-ready model forecasting energy connsumption levels in 24-hour time intervas across multple cosumer types from Denmark.

Also, the project demonstrates integrating an experiment tracker, model registry, a feature store (Hopsworks), Docker, Airflow and Github Actions.
Below is the proposed pipeline architecture:
![](./Pipeline%20architecture.png)

### The Data

---

I used an open API that provides hourly energy consumption values for all the energy consumer types in Denmark.
They provide an intuitive interface which allows you to easily query and visualize the data [here](https://www.energidataservice.dk/tso-electricity/ConsumptionDE35Hour).
