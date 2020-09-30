class AlaskaConfig:
    ALASKA = 'http://0.0.0.0:6000'
    ALASKA_INFO = ALASKA + '/info'
    ALASKA_BEAR = ALASKA + '/bear'
    ALASKA_SPECIFIC_BEAR = ALASKA_BEAR + '/{id}'
    AVAILABLE_BEAR_TYPES = ["POLAR", "BROWN", "BLACK"]
