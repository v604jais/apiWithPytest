import json
from typing import Any, List, Union


class Utility:
    #find the value by passing key


       def get_value(self, json_obj: Union[dict, list], key: str) -> List[Any]:
        value_list = []
        self._get_value_helper(json_obj, key, value_list)
        return value_list

       def _get_value_helper(self, json_obj: Union[dict, list], key: str, value_list: List[Any]):
        try:
            if isinstance(json_obj, dict):
                if key in json_obj:
                    value_list.append(json_obj[key])
                else:
                    for k, v in json_obj.items():
                        if isinstance(v, (dict, list)):
                            self._get_value_helper(v, key, value_list)

            elif isinstance(json_obj, list):
                for item in json_obj:
                    if isinstance(item, (dict, list)):
                        self._get_value_helper(item, key, value_list)

        except Exception as e:
            print(f"Exception Caught: {str(e)}")      