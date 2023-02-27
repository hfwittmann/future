"""
This is a boilerplate pipeline 'evaluate'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import getPeople, myevaluate


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                getPeople,
                inputs=["params:people", "parameters"],
                outputs="params_people",
            ),
            node(
                myevaluate,
                inputs=[
                    "params:predictions",
                    "params_people",
                    "params:realised",
                    "params:weights",
                    "params:out_path",
                ],
                outputs="results",
            ),
        ]
    )
