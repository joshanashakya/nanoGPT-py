import os


class Config:
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

    DATA_DIR = os.path.join(ROOT_DIR, "data")
    RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
    CORPUS_DIR = os.path.join(DATA_DIR, "corpus")

    REFERENCES_DIR = os.path.join(ROOT_DIR, "references")
    REPORTS_DIR = os.path.join(ROOT_DIR, "reports")
    REPORTS_FIG_DIR = os.path.join(REPORTS_DIR, "figures")
    CHECKPOINTS_DIR = os.path.join(ROOT_DIR, "models")

    # Which config/gptconfig_<name>.json the model and training use.
    # Change it here, or set the GPT_CONFIG_NAME environment variable for one run.
    CONFIG_DIR = os.path.join(ROOT_DIR, "config")
    GPT_CONFIG_NAME = os.environ.get("GPT_CONFIG_NAME", "baseline")


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass