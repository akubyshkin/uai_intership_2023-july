import os


class ClassInfo:
    def __init__(self, class_value, class_dir_name):
        self.class_value = class_value
        self.class_dir_name = class_dir_name


MATERIAL = 'material'
RIM_TYPE = 'rim_type'


CLASS_INFO_DICT = {
    MATERIAL: [
        ClassInfo('комбинированный', 'combined'),
        ClassInfo('металл', 'metal'),
        ClassInfo('пластик', 'plastic'),
    ],
    RIM_TYPE: [
        ClassInfo('ободковая', 'with_rim'),
        ClassInfo('безободковая', 'rimless'),
        ClassInfo('леска', 'string')
    ]
}


class OfferPath:
    def __init__(self, dir_name, offer_id_prefix):
        self.dir_name = dir_name
        self.offer_id_prefix = offer_id_prefix

class _OfferPathBuilder:
    def __init__(self, root_dir, task_name_dir, param_attr_name):
        self.root_dir = root_dir
        self.task_name_dir = task_name_dir
        self.param_attr_name = param_attr_name

    def _build_path(self, offer):
        if self.param_attr_name not in offer.params:
            print(f'Для оффера {offer.id} не найден параметр {self.param_attr_name}')
            return None
        for class_info in CLASS_INFO_DICT[self.task_name_dir]:
            if offer.params[self.param_attr_name].lower() == class_info.class_value:
                return OfferPath(os.path.join(
                    self.root_dir,
                    self.task_name_dir,
                    class_info.class_dir_name
                ), offer.id)
        return None


class OfferPathBuilders:
    def __init__(self, root_dir):
        self.PATH_BUILDERS_DICT = [
            _OfferPathBuilder(root_dir, MATERIAL, 'Материал'),
            _OfferPathBuilder(root_dir, RIM_TYPE, 'Строение оправы')
        ]

    def build_paths(self, offer):
        result = []
        for path_builder in self.PATH_BUILDERS_DICT:
            path = path_builder._build_path(offer)
            if path == None:
                continue
            result.append(path)
        return result
