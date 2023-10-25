import doctest

import api.serializers.utils
import api.utils.request
import api.utils.files


def load_tests(loader, tests, ignore):  # pylint: disable=W0613
    tests.addTests(
        [
            doctest.DocTestSuite(api.serializers.utils),
            doctest.DocTestSuite(api.utils.request),
            doctest.DocTestSuite(api.utils.files),
            doctest.DocTestSuite(api.utils.accessors),
        ]
    )
    return tests
