import streamlit as st

def import_verbs():
    verb_vocab = {
        "sum": {
            "voice": "act",
            "conj": None,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {1: "sum",
                                        2: "es",
                                        3: "est"},
                                "pl": {1: "sumus",
                                        2: "estis",
                                        3: "sunt"}},
                            "subj": {"sg": {1: "sim",
                                            2: "sīs",
                                            3: "sit"},
                                    "pl": {1: "sīmus",
                                            2: "sītis",
                                            3: "sint"}},
                            "impv": {"sg": {2: "es"},
                                    "pl": {2: "este"}},
                            "inf": "esse"}
                            },
                    "impf": {
                        "act": {
                            "ind": {
                                "sg": {1: "eram",
                                    2: "erās",
                                    3: "erat"},
                                "pl": {1: "erāmus",
                                        2: "erātis",
                                        3: "erant"}
                                }
                            }
                        },
                    "fut": {
                        "act": {
                            "ind": {
                                "sg": {1: "erō",
                                        2: "eris",
                                        3: "erit"},
                                "pl": {1: "erimus",
                                        2: "eritis",
                                        3: "erunt"}
                            },
                            "impv": {
                                "sg": {
                                    2: "estō",
                                    3: "estō"
                                },
                                "pl": {
                                    2: "estōte",
                                    3: "suntō"
                                }
                            }
                        }
                    },                
                }
            },
            # regular information
            "perf": "fu",
            "fap": "futūr",
            "pap": None
            },
        "ferō": {
            "voice": "act",
            "conj": 3,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "ferō",
                                    2: "fers",
                                    3: "fert"
                                    },
                                "pl": {
                                    1: "ferimus",
                                    2: "fertis",
                                    3: "ferunt"
                                    }
                                },
                            "inf": "ferre",
                            "impv": {
                                "sg": {2: "fer"},
                                "pl": {2: "ferte"}
                            }
                        },
                        "pass": {
                            "ind": {
                                "sg": {
                                    1: "feror",
                                    2: "ferris",
                                    3: "fertur"
                                    },
                                "pl": {
                                    1: "ferimur",
                                    2: "feriminī",
                                    3: "feruntur"
                                }
                            },
                            "inf": "ferrī",
                            "impv": {
                                "sg": {2: "ferre"},
                                "pl": {2: "feriminī"}
                            }
                        }
                    },
                    "fut": {
                        "act": {
                            "impv": {
                                "sg": {
                                    2: "fertō",
                                    3: "fertō"
                                },
                                "pl": {
                                    2: "fertōte",
                                    3: "feruntō"
                                }
                            }
                        },
                        "pass": {
                            "impv": {
                                "sg": {
                                    2: "fertor",
                                    3: "fertor"
                                },
                                "pl": {
                                    3: "feruntor"
                                }
                            }
                        }
                    }
                }
            },
            "pres": "fer",
            "perf": "tul",
            "ppp": "lāt"
        },
        "eō": {
            "voice": "act",
            "impers_pass_only": True,
            "conj": 3,
            "irreg": {
                "forms": {
                    "pres": {
                        "act": {
                            "ind": {
                                "sg": {
                                    1: "eō",
                                    2: "īs",
                                    3: "it"
                                },
                                "pl": {
                                    1: "īmus",
                                    2: "ītis",
                                    3: "eunt"
                                }
                            },
                            "inf": "īre",
                            "impv": {
                                "sg": {2: "ī"},
                                "pl": {2: "īte"}
                            }
                        },
                        "pass": {
                            "ind": {
                                "sg": {
                                    3: "ītur"
                                }
                            }
                        }
                    },
                    "fut": {
                        "act": {
                            "ind": {
                                "sg": {1: "ībō",
                                    2: "ībis",
                                    3: "ībit"},
                                "pl": {1: "ībimus",
                                    2: "ībitis",
                                    3: "ībunt"}
                            },
                            "impv": {
                                "sg": {
                                    2: "ītō",
                                    3: "ītō"
                                },
                                "pl": {
                                    2: "ītōte",
                                    3: "euntō"
                                }
                            }
                        },
                        "pass": {
                            "ind": {
                                "sg": {
                                    3: "ībitur"
                                }
                            }
                        }
                    },
                },
                "stems": {
                    "pres": {
                        "subj": "e"
                    }
                }
            },
            "pres": "ī",
            "perf": "īv", # need to figure out how to do alternative forms of perfect
            "ppp": "it"
        },

        # add irregular verbs: possum, fio, volo, nolo, malo

        ## REGULAR VERBS

        # when adding duco, dico, and facio, don't forget the irregular singular imperative

        "amō": {"voice": "act",
                "conj": 1,
                "pres": "am",
                "perf": "amāv",
                "ppp": "amāt"},
        "habeō": {"voice": "act",
                "conj": 2,
                "pres": "hab",
                "perf": "habu",
                "ppp": "habit"},
        "regō": {"voice": "act",
                "conj": 3,
                "pres": "reg",
                "perf": "rēx",
                "ppp": "rect"},
        "capiō": {"voice": "act",
                "conj": "3io",
                "pres": "cap",
                "perf": "cēp",
                "ppp": "capt"},
        "audiō": {"voice": "act",
                "conj": 4,
                "pres": "aud",
                "perf": "audīv",
                "ppp": "audīt"},
        "cōnor": {"voice": "dep",
                "conj": 1,
                "pres": "cōn",
                "ppp": "cōnāt"},
        "fateor": {"voice": "dep",
                "conj": 2,
                "pres": "fat",
                "ppp": "fass"},
        "sequor": {"voice": "dep",
                "conj": 3,
                "pres": "sequ",
                "ppp": "secūt"},
        "morior": {"voice": "dep",
                "conj": "3io",
                "pres": "mor",
                "ppp": "mortu",
                "fap": "moritūr"},
        "experior": {"voice": "dep",
                "conj": 4,
                "pres": "exper",
                "ppp": "expert"},
        "audeō": {"voice": "semidep",
                "conj": 2,
                "pres": "aud",
                "ppp": "aus"}
    }
    return verb_vocab


def import_nouns():
    noun_vocab = {
                "puella": {"decl": 1,
                         "stem": "puell"},
                "puer": {"decl": "2_er",
                         "stem": "puer"},
                "servus": {"decl": "2_us",
                           "stem": "serv"},
                "agricola": {"decl": 1,
                             "stem": "agricol"},
                "cīvis": {"decl": "3_istem",
                          "stem": "cīv"},
                "leo": {"decl": 3,
                        "stem": "leōn"},
                "manus": {"decl": 4,
                          "stem": "man"},
                "senātus": {"decl": 4,
                            "stem": "senāt"},
                "rēs": {"decl": "5_consonant",
                        "stem": "r"},
                "diēs": {"decl": "5_vowel",
                         "stem": "di"},
                "animal": {"decl": "3_istem_neut",
                           "stem": "animāl"},
                "mīles": {"decl": 3,
                          "stem": "mīlit"},
                "cornū": {"decl": "4_neut",
                           "stem": "corn"},
                "nōmen": {"decl": "3_neut",
                           "stem": "nōmin"},
                "templum": {"decl": "2_neut",
                           "stem": "templ"},
                "ager": {"decl": "2_er",
                         "stem": "agr"},
                "equus": {"decl": "2_us",
                          "stem": "equ"}
            }
    return noun_vocab