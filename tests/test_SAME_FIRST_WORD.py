import pandas as pd
import random

import sys
sys.path.insert(1, '..')
from check_data_consistency import DataConsistencyChecker

from utils import synth_test, synth_test_all_cols, kropt_test

test_id = 'SAME_FIRST_WORD'
random.seed(0)

synth_patterns_cols = ['"same_start_word rand_a" AND "same_start_word all_a"',
                       '"same_start_word all_a" AND "same_start_word rand_a"',
                       '"same_start_word rand_b" AND "same_start_word all_b"',
                       '"same_start_word all_b" AND "same_start_word rand_b"',
                       ]
synth_exceptions_cols = ['"same_start_word rand_a" AND "same_start_word most_a"',
                         '"same_start_word all_a" AND "same_start_word most_a"',
                         '"same_start_word most_a" AND "same_start_word rand_a"',
                         '"same_start_word most_a" AND "same_start_word all_a"',
                         '"same_start_word rand_b" AND "same_start_word most_b"',
                         '"same_start_word all_b" AND "same_start_word most_b"',
                         '"same_start_word most_b" AND "same_start_word rand_b"',
                         '"same_start_word most_b" AND "same_start_word all_b"',
                         ]


def test_synthetic_no_nulls():
	synth_test(
		test_id,
		'none',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_one_row_nulls():
	synth_test(
		test_id,
		'one-row',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_in_sync_nulls():
	synth_test(
		test_id,
		'in-sync',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_random_nulls():
	synth_test(
		test_id,
		'random',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_80_percent_nulls():
	synth_test(
		test_id,
		'80-percent',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_no_nulls():
	synth_test_all_cols(
		test_id,
		'none',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_one_row_nulls():
	synth_test_all_cols(
		test_id,
		'one-row',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_in_sync_nulls():
	synth_test_all_cols(
		test_id,
		'in-sync',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_random_nulls():
	synth_test_all_cols(
		test_id,
		'random',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_synthetic_all_cols_80_percent_nulls():
	synth_test_all_cols(
		test_id,
		'80-percent',
		synth_patterns_cols,
		synth_exceptions_cols)


def test_fetch_kropt():
	kropt_test(
		test_id,
		[],
		[]
	)