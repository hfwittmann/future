"""
This is a boilerplate pipeline 'evaluate'
generated using Kedro 0.18.4
"""
import pandas as pd
import numpy as np
from pathlib import Path


def getPeople(people, parameters):

    for person in people:
        parameters["people"][person] = parameters[person]

    return parameters["people"]


def myevaluate(predictions, people, realised_with_timestamps, weights, out_path):
    out = {}
    for person_key, person_with_timestamps in people.items():
        D_person, scores_events_sequence = myevaluate_one_person(
            predictions,
            person_key,
            person_with_timestamps,
            realised_with_timestamps,
            weights,
            out_path,
        )
        out[person_key] = {
            "scores": list(scores_events_sequence),
            "total_score": scores_events_sequence.mean(),
        }

    return out


def myevaluate_one_person(
    predictions,
    person_key,
    person_with_timestamps,
    realised_with_timestamps,
    weights,
    out_path,
):

    personlist = list()
    realisedlist = list()

    for timestamp in person_with_timestamps:
        personlist += person_with_timestamps[timestamp]

    for timestamp in realised_with_timestamps:
        realisedlist += realised_with_timestamps[timestamp]

    try:
        assert set(predictions) == set(personlist), "should match"
    except Exception as e:

        for p in predictions:
            assert p in personlist, f"{p} not in personlist for person {person_key}"
        for pl in personlist:
            assert pl in predictions, f"{pl} not in predictions"

    D_person = pd.DataFrame(index=personlist)
    D_person["done"] = False

    scores_events_sequence = np.zeros(shape=(len(realisedlist)))

    for ix, r in enumerate(realisedlist):
        D_person.at[r, "done"] = True

        Events_count = D_person.copy()
        Events_count.loc[:r, "done"] = 0 + D_person.loc[:r, "done"]
        Events_count.loc[r:, "done"] = 1 - D_person.loc[r:, "done"]
        Events_count.loc[r, "done"] = 0.5

        personalised_out_path = out_path.replace("<person_key>", person_key).replace(
            "<event>", r
        )
        directory = Path(personalised_out_path).parent
        Path.mkdir(directory, exist_ok=True)

        Events_count.to_csv(personalised_out_path)

        score_events_sequence = Events_count["done"].mean()
        scores_events_sequence[ix] = score_events_sequence

    return D_person, scores_events_sequence
