import pytest
import one_hot_encoder


def test_args():
    exp = [
        ('a', [0, 0, 1]),
        ('b', [0, 1, 0]),
        ('c', [1, 0, 0]),
    ]
    res_args = one_hot_encoder.fit_transform('a', 'b', 'c')
    res_list = one_hot_encoder.fit_transform(['a', 'b', 'c'])
    assert exp == res_args
    assert exp == res_list


def test_empty_arg():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()


def test_empty_arglist():
    res = one_hot_encoder.fit_transform([])
    assert [] == res


def test_similar_args():
    exp = [
        ('a', [1]),
        ('a', [1]),
    ]
    res_args = one_hot_encoder.fit_transform('a', 'a')
    res_list = one_hot_encoder.fit_transform(['a', 'a'])
    assert exp == res_args
    assert exp == res_list


def test_not_string_input():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform(1, 2.0)
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform([1, 2.0])


def test_return_type():
    res = one_hot_encoder.fit_transform('a', 'b', 'c')
    assert isinstance(res, list)
    assert all(isinstance(x, tuple) for x in res)
