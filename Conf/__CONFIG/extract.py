"""
author: @guu8hc
"""

model = {
    "name": "EcuExtract",
    "PDUS" : {
        "ESP_19" : {
            "Length" : 8,
            "ID" : 0x19,
        },

        "LWI_01" : {
            "Length" : 8,
            "ID" : 0x10,
        },

        "TSK_07" : {
            "Length" : 8,
            "ID" : 0x07,
        },

        "MSG_EMG_01" : {
            "Length" : 8,
            "ID" : 0x10,
        },

        "ESP_21" : {
            "Length" : 8,
            "ID" : 0x21,
        },

        "MUX_09" : {
            "Length" : 8,
            "ID" : 0x09,
        }
    }
}