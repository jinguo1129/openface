#!/usr/bin/env python3
#
# Copyright 2016 Carnegie Mellon University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Brandon Amos
# 2016-07-29

import argparse
import base64
import csv
import os
# import magic # Detect image type from buffer contents (disabled, all are jpg)

parser = argparse.ArgumentParser()
parser.add_argument('croppedTSV', type=str)
parser.add_argument('--outputDir', type=str, default='raw')
args = parser.parse_args()

with open(args.croppedTSV, 'r') as tsvF:
    reader = csv.reader(tsvF, delimiter='\t')
    i = 0
    for row in reader:
        MID, faceID, data = row[0], row[4], base64.b64decode(row[-1])

        saveDir = os.path.join(args.outputDir, faceID)
        savePath = os.path.join(saveDir, MID+'.jpg')

        # assert(magic.from_buffer(data) == 'JPEG image data, JFIF standard 1.01')

        os.makedirs(saveDir, exist_ok=True)
        with open(savePath, 'wb') as f:
            f.write(data)

        i += 1

        if i % 1000 == 0:
            print("Extracted {} images.".format(i))
