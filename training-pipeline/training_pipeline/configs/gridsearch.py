# Note: In production, this would be in a YAML file 
# and we could use random or bayesian search + early stopping to speed up process.

sweep_configs = {
    "method": "grid",
    "metric": {"name": "validation.MAPE", "goal": "minimize"},
    "parameters": {
        "forecaster__estimator__n_jobs": {"values": [-1]},
        "forecaster__estimator__n_estimators": {"values": [1000, 2000, 3000]},
        "forecaster__estimator__learning_rate": {"values": [0.1, 0.15]},
        "forecaster__estimator__max_depth": {"values": [-1, 5]},
        "forecaster__estimator__reg_lambda": {"values": [0, 0.01, 0.015]},
        "daily_season_transformers__window_summarizer__lag_feature__lag": {
            "values": [list(range(1, 73))]
        },
        "forecaster_transformers__window_summarizer__lag_feature__mean": {
            "values": [[[1, 24], [1, 48], [1, 72]]]
        },
        "forecaster_transformers__window_summarizer__lag_feature__std": {
            "values": [[[1,24], [1, 48]]]
        },
        "forecaster_transformers__window_summarizer__n_jobs": {"values": [1]},
    },
}