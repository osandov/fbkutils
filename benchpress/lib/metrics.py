#!/usr/bin/env python3
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.


class Metrics(object):
    """Container for metrics that are exported by a job

    Attributes:
        names (list): sorted metric names
    """

    def __init__(self, metrics_dict):
        self.metrics_dict = self.flatten(metrics_dict)
        self.names = sorted(list(self.metrics_dict.keys()))

    def flatten(self, metrics, prefix=''):
        """Flattens given dict using dot separated keys.
        """
        flattened = {}
        if isinstance(metrics, dict):
            for key, metric in metrics.items():
                flattened.update(self.flatten(metric, prefix + key + '.'))
        else:
            flattened = {str(prefix[:-1]): metrics}

        return flattened

    def metrics(self):
        """Get a dictionary of each metric and its value.
        """
        return self.metrics_dict

    def metrics_list(self):
        """Get a list of metric tuples (name, value) sorted by name.
        """
        return [(name, self.metrics_dict[name]) for name in self.names]

    def __getitem__(self, name):
        return self.metrics_dict[name]

    def items(self):
        return self.metrics_dict.items()
