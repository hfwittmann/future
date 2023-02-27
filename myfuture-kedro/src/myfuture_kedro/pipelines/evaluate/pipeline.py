"""
This is a boilerplate pipeline 'evaluate'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import myevaluate


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                myevaluate,
                inputs=[
                    "params:predictions",
                    "params:people",
                    "params:realised",
                    "params:weights",
                    "params:out_path",
                ],
                outputs="results",
            )
        ]
    )
