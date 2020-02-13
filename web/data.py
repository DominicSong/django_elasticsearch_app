class SearchRes:
    def __init__(self, data_dict):
        self.title = data_dict['title']
        self.catalogue = data_dict['catalogue']
        self.enterprise = data_dict['enterprise']
        self.keyword = data_dict['keyword']
        self.version = data_dict['version']
        self.answer = data_dict['answer']
        self.relation1 = data_dict['relation1']
        self.relation2 = data_dict['relation2']