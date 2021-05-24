class Page:
    def __init__(self, id, created_time, last_edited_time, properties, archived, object):
        self.id = id
        self.created_time = created_time
        self.last_edited_time = last_edited_time
        self.properties = properties
        self.archived = archived
        self.object = "page"
