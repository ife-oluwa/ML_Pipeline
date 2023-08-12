<!-- @format -->

### A Full Stack MLOPs Project

---

This repository demonstrates the design, implementation, training, deployment and monitoring of an ML batch system using MLOps best practices.
In this project, I built a production-ready model forecasting energy connsumption levels in 24-hour time intervas across multple cosumer types from Denmark.

Also, the project demonstrates integrating an experiment tracker, model registry, a feature store (Hopsworks), Docker, Airflow and Github Actions.
Below is the proposed pipeline architecture:
![](./Pipeline%20architecture.png)

### The Data

---

I used an open API that provides hourly energy consumption values for all the energy consumer types in Denmark.
They provide an intuitive interface which allows you to easily query and visualize the data [here](https://www.energidataservice.dk/tso-electricity/ConsumptionDE35Hour).

The data has 4 main attributes:

- **Hour UTC**: the UTC datetime when the data point was observed.
- **Price Area**: Denmark is divided into price areas: DK1 and DK; divided by the Great Belt.
- **Consumer Type**: The consumer type is the industry code DE35, owned and maintained by Danish Energy.
- **Total consumption**: Total electricity consumption in kWh.

The data points have an hourly resolution. For example: "2023–04–15 21:00Z", "2023–04–15 20:00Z", "2023–04–15 19:00Z", etc.

We will model the data as multiple time series. Each unique price area and consumer type tuple represents its unique time series.

Thus, we will build a model that independently forecasts the energy consumption for the next 24 hours for every time series.

### Code Structure

---

The code is split into two main components: the <code>pipeline</code> and the <code>web app</code>.
The pipeline consists of 3 modules:

- <code>feature-pipeline</code>
- <code>training-pipeline</code>
- <code>batch-prediction-pipeline</code>

The web app consists of 3 other modules:

- <code>app-api</code>
- <code>app-frontend</code>
- <code>app-monitoring</code>

Also, we have the following folders:

- <code>airflow</code>: Airflow files | Orchestration
- <code>.github</code>: Github Actiions files | CI/CD
- <code>deploy</code>: Build & Deploy
