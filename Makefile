DATASET=developer-agreement-type
DATASET_URL=https://github.com/digital-land/developer-contributions-collection/raw/main/dataset/$(DATASET).sqlite3

include makerules/makerules.mk
include makerules/render.mk
