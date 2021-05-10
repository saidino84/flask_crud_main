from . import db


class ImageModel(db.Model):
    def __init__(self, image, nome, description):
        assert(image !=None)
        self.image = image
        self.nome=nome
        self.description=description
