import pytest
import copy

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_dict,result",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }],
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ),
        (
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },

        )
    ]
)
def test_restore(
        user_dict: list, result: dict
) -> None:
    restore_names(user_dict)
    for dic in user_dict:
        new_dict = copy.deepcopy(dic)
        assert new_dict == result
