# fits in 1 line
d = {
    'foobar': 1
}


# 1-line fit + end with comma
def wall_indent0(some_param0,
                 some_param1,
                 some_param2,):
    pass


# without comma & length < max-line-length
def wall_indent1(some_param0,
                 some_param1,
                 some_param2):
    pass


# without comma & length > max-line-length
def wall_indent2(some_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa_param0,
                 some_param1,
                 some_param2):
    pass


# dedent of "("
f = wall_indent0(
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',
    'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
